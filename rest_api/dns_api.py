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

description = "DNS measurements"

def subparse_cmd_args(subparser):

    subparser.add_argument("-i", "--interval",
                           metavar = "INTERVAL",
                           dest = "definitions.interval",
                           type = int,
                           help = "In normal (not one-off) measurements, this "
                           "value represents the number of seconds between "
                           "measurements by a single probe (default=300).")

    subparser.add_argument("-u", "--use-probe-resolver",
                           dest = "definitions.use_probe_resolver",
                           action = "store_true",
                           help = "Use the probe's resolver (default=false).")

    subparser.add_argument("-n", "--use-nsid",
                           dest = "definitions.use_NSID",
                           action = "store_true",
                           help = "Use NISD (default=false).")

    subparser.add_argument("-c", "--query-class",
                           metavar = "CLASS",
                           dest = "definitions.query_class",
                           default = "IN",
                           type = str,
                           help = "Must be either \"IN\" or \"CHAOS\" "
                           "(default=\"IN\").")

    subparser.add_argument("-y", "--query-type",
                           metavar = "TYPE",
                           dest = "definitions.query_type",
                           default = "A",
                           type = str,
                           help = "Varies with the query_class "
                           "(default=\"A\").")

    subparser.add_argument("definitions.query_argument",
                           metavar = "domain",
                           type = str,
                           help = "The domain to resolve.")

    subparser.add_argument("-r", "--recursion-desired",
                           dest = "definitions.recursion_desired",
                           action = "store_true",
                           help = "For privacy reasons, when "
                           "use_probe_resolver is true, this property is "
                           "silently set to true (default=false).")

    subparser.add_argument("-p", "--protocol",
                           metavar = "PROTOCOL",
                           dest = "definitions.protocol",
                           type = str,
                           default = "UDP",
                           help = "Must be either \"TCP\" or \"UDP\" "
                           "(default=\"UDP\").")
