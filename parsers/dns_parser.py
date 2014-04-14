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
        
        result_set = []
        returned_messages = []
        
        if raw_measurement.has_key("resultset"):
            result_set = raw_measurement["resultset"]
        elif raw_measurement.has_key("result"):
            result_set = [raw_measurement]
        elif raw_measurement.has_key("error"):
            log.error("Found error in measurement: %s" % raw_measurement['error'])
            return None
        else:
            return None
        
        # Get the answer payload buffer from the server.
        for result_measurement in result_set:
            if not (result_measurement.has_key('error')):
                raw_response = base64.b64decode(result_measurement["result"]["abuf"])
                
                try:
                    dns_response = dns.message.from_wire(raw_response)
                    returned_messages.append(dns_response)
                except Exception as err:
                    log.error(err)
                    return None
        return returned_messages
