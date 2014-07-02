#!/usr/bin/env python
#
# Copyright 2014 Philipp Winter <phw@nymity.ch>
#
# This file is part of atlas tools.
#
# atlas tools is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# atlas tools is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with atlas tools.  If not, see <http://www.gnu.org/licenses/>.

import argparse
import pkgutil
import json
import pprint

import rest_api
import rest_api.query_issuer
import probe_selector

import logger

log = logger.get_logger()

def args_to_json( args, measurement_type ):
    """
    Convert the given arguments to a JSON dictionary.
    """

    json = {}

    for key in args.keys():

        if not '.' in key:
            continue
        section, var = key.split('.')

        if not json.has_key(section):
            json[section] = [{ var : args[key] }]
        else:
            json[section][0][var] = args[key]

    json["definitions"][0]["type"] = measurement_type

    return json

def parse_cmd_args():

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest = "subparser_name",
                                       help = "Available measurement modules.")

    # See the following web page for the Atlas' REST API:
    # <https://atlas.ripe.net/docs/measurement-creation-api/>

    parser.add_argument("-d", "--description",
                        metavar = "DESCRIPTION",
                        dest = "definitions.description",
                        type = str,
                        default = "Custom measurement",
                        help = "Measurement description.")

    parser.add_argument("-a", "--address-family",
                        metavar = "AF",
                        dest = "definitions.af",
                        type = int,
                        default = 4,
                        help = "The address family.  Must be either 4 or 6.")

    parser.add_argument("-r", "--resolve-probe",
                        dest = "definitions.resolve_on_probe",
                        action = "store_true",
                        help = "Let the probe rather than Atlas resolve "
                        "the domain.")

    parser.add_argument("-o", "--one-off",
                        dest = "definitions.is_oneoff",
                        action = "store_false",
                        help = "Toggle one-off measurement (default=true).")

    parser.add_argument("-v", "--visualize",
                        dest = "definitions.can_visualise",
                        action = "store_true",
                        help = "Let Atlas visualise the results.")

    parser.add_argument("-p", "--public",
                        dest = "definitions.is_public",
                        action = "store_true",
                        help = "Make measurement publicly available.")

    # The following is unrelated to Atlas' REST API.

    parser.add_argument("-f", "--file",
                        dest = "probe_file",
                        type=str,
                        default=None,
                        help="Use the given file to learn about active "
                        "probes.  If not specified, the documented is "
                        "downloaded.")

    parser.add_argument("probe_area",
                        type=str,
                        default=None,
                        help="Select probes in the given area.  A 2-letter "
                        "country code is expected.")

    parser.add_argument("probe_count",
                        type=int,
                        default=None,
                        help="How many probes to select.")

    parser.add_argument("api_key",
                        type = str,
                        help = "The API key for measurement creation.")

    # Let our subparsers (ping, dns, ...) add command line arguments.

    module_names = [name for _, name, _ in pkgutil.iter_modules(["rest_api"])
                    if "api" in name]
    for module_name in module_names:
        module = __import__("rest_api.%s" % module_name,
                            fromlist=[module_name])

        subparser = subparsers.add_parser(module_name.split('_')[0],
                                          help=module.description)
        module.subparse_cmd_args(subparser)

    args = parser.parse_args()
    json_dict = args_to_json(vars(args), args.subparser_name)

    probe_ids = probe_selector.select(args.probe_area, args.probe_count,
                                      args.probe_file)

    json_dict["probes"] = [{
        "requested": args.probe_count,
        "type": "probes",
        "value": ",".join([str(p) for p in probe_ids])
    }]

    # Send JSON query to RIPE Atlas.

    log.debug("Creating JSON blurb from argument list.")
    json_blurb = json.dumps(json_dict)
    rest_api.query_issuer.send_query(json_blurb, args.api_key)

    return 0

if __name__ == "__main__":

    exit(parse_cmd_args())
