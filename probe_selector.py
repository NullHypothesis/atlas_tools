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

import re
import argparse
import urllib2
import json
import random

import logger

log = logger.get_logger()

def parse_cmd_args():

    parser = argparse.ArgumentParser(description="Select and return RIPE "
                                     "Atlas probe IDs in unique ASNs.")

    parser.add_argument("-f", "--file", type=str, default=None,
                        help="Use the given file instead of downloading it.")

    parser.add_argument("area", type=str, default=None,
                        help="Select probes in the given area.")

    parser.add_argument("count", type=int, default=None,
                        help="How many probes to select.")

    return parser.parse_args()

def extract_asn(url):
    """
    Extract the ASN from the following URL:
    <a href='https://stat.ripe.net/AS5719' target='_blank'>5719</a>
    """

    pattern = ".*<a href='[^']*' target='_blank'>([^<]*)</a>.*"

    match = re.match(pattern, url)

    if match is not None:
        return int(match.group(1))
    else:
        return None

def select(area, count, file_name=None):

    probe_ids = []

    url = "https://atlas.ripe.net/contrib/active_probes.json"

    if file_name:
        log.debug("Fetching list of currently active Atlas probes " \
                  "from file \"%s\"." % file_name)
        try:
            active_probes = json.load(open(file_name))
        except ValueError as err:
            log.error(err)
            return 1
    else:
        log.debug("Fetching list of currently active Atlas probes " \
                  "from <%s>." % url)
        response = urllib2.urlopen(url)
        json_blurb = response.read()
        active_probes = json.loads(json_blurb)

    # Key: ASNv4, value: probe JSON.
    relevant_probes = {}

    for probe in active_probes:

        # Skip probes which are not up.
        if probe[0] != u"U":
            continue

        probe_info = probe[3]
        if not ("Country Code" in probe_info):
            continue

        # Skip probes which are not in our desired region.
        country_code = probe_info[probe_info.index("Country Code") + 1]
        if area.lower() != "ww" and (country_code.lower() != area.lower()):
            continue

        # Group all remaining probes by their ASNv4.
        if "IPv4 ASN" in probe_info:
            asnv4 = extract_asn(probe_info[3])

        if not relevant_probes.has_key(asnv4):
            relevant_probes[asnv4] = [probe]
        else:
            (relevant_probes[asnv4]).append(probe)

    asnv4s = relevant_probes.keys()
    random.shuffle(asnv4s)

    for asnv4 in asnv4s:

        probes = relevant_probes[asnv4]
        random.shuffle(probes)

        probe_info = probes[0][3]
        probe_ids.append(probe_info[probe_info.index(u"Probe ID") + 1])

        count -= 1
        if count == 0:
            break

    return probe_ids

if __name__ == "__main__":

    args = parse_cmd_args()

    log.debug("Selecting %d probes in %s." % (args.count, args.area))

    exit(select(args.area, args.count, args.file))
