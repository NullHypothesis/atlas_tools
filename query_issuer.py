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

import urllib2

import logger

log = logger.get_logger()

def send_query(json_blurb, api_key):
    """
    Send HTTP POST request containing the JSON-formatted Atlas query.

    If successful, Atlas' API should return the JSON-formatted measurement ID.
    """

    url = "https://atlas.ripe.net/api/v1/measurement/?key=" + api_key

    log.debug("Sending %d bytes of JSON blurb to %s." % (len(json_blurb), url))

    request = urllib2.Request(url, json_blurb)
    request.add_header("Content-Type", "application/json")
    request.add_header("Accept", "application/json")

    try:
        response = urllib2.urlopen(request)
    except urllib2.URLError as err:
        log.error("urllib2.urlopen failed: %s" % err)
        return None

    result = response.read()
    log.debug("Received: %s" % result)

    return result
