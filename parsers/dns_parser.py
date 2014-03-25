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

import base64

import dns.message

import meta_parser
import logger

log = logger.get_logger()

class Parser(meta_parser.MetaParser):

    def load(self, raw_measurement):

        if not raw_measurement.has_key("result"):
            return None

        # Get the answer payload buffer from the server.

        raw_response = base64.b64decode(raw_measurement["result"]["abuf"])

        try:
            dns_response = dns.message.from_wire(raw_response)
        except Exception as err:
            log.error(err)
            return None

        return dns_response
