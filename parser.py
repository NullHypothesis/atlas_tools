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

import sys
import json

import logger

log = logger.get_logger()

def parse(file_name):

    try:
        raw_data = json.load(open(file_name))
    except ValueError as err:
        log.error(err)
        return 1

    # Depending on the measurement type, we load the according parser.

    try:
        data_type  = raw_data[0]["type"]
        parsing_module = __import__("parsers.%s_parser" % data_type,
                                    fromlist=[data_type])
    except ImportError as err:
        log.error(err)
        return 1

    log.info("Successfully imported parser for \"%s\"." % data_type)

    parser = parsing_module.Parser()

    for raw_measurement in raw_data:

        parser.dump(raw_measurement)

    return 0

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print >>sys.stderr, "\nUsage: %s FILE.JSON\n" % sys.argv[0]
        exit(1)

    exit(parse(sys.argv[1]))
