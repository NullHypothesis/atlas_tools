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

import pprint

class MetaParser(object):

    def load(self):
        """
        Parses and returns measurement-specific data.
        """
        pass

    def dump(self, raw_measurement):

        print "---\n"

        # Print general measurement information.
        print pprint.pprint(raw_measurement)

        # Print specific (DNS, X.509, ...) measurement information.
        print self.load(raw_measurement)
        print
