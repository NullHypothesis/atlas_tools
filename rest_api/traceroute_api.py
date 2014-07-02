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

description = "traceroute measurements"

def subparse_cmd_args(subparser):

    subparser.add_argument("definitions.target",
                           metavar = "target",
                           type = str,
                           help = "The traceroute's target.")

    subparser.add_argument("-o", "--protocol",
                           metavar = "PROTOCOL",
                           dest = "definitions.protocol",
                           default = "ICMP",
                           type = str,
                           help = "The traceroute protocol which must be "
                                  "ICMP, UDP, or TCP (default=ICMP).")

    subparser.add_argument("-i", "--interval",
                           metavar = "INTERVAL",
                           dest = "definitions.interval",
                           default = 900,
                           type = int,
                           help = "In normal (not one-off) measurements, this "
                                  "value represents the number of seconds "
                                  "between measurements by a single probe "
                                  "(default=900).")

    subparser.add_argument("-d", "--dont-fragment",
                           dest = "definitions.dontfrag",
                           action = "store_true",
                           help = "Don't fragment packets (default=false).")

    subparser.add_argument("-p", "--paris",
                           metavar = "PARIS",
                           dest = "definitions.paris",
                           type = int,
                           help = "Use Paris traceroute.  The given value "
                                  "must be between 1 and 16.")

    subparser.add_argument("-f", "--first-hop",
                           metavar = "FIRST_HOP",
                           dest = "definitions.firsthop",
                           type = int,
                           help = "The given value must be between 1 and 255.")

    subparser.add_argument("-m", "--max-hops",
                           metavar = "MAX_HOPS",
                           dest = "definitions.maxhops",
                           type = int,
                           help = "The given value must be between 1 and 255.")

    subparser.add_argument("-t", "--timeout",
                           metavar = "TIMEOUT",
                           dest = "definitions.timeout",
                           default = 4000,
                           type = int,
                           help = "The given value (in milliseconds) must be "
                                  "between 1 and 60000")

    subparser.add_argument("-s", "--size",
                           metavar = "PACKET_SIZE",
                           dest = "definitions.size",
                           type = int,
                           help = "The size of the packets.  The given value "
                                  "must be between 1 and 2048.")
