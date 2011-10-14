# Watch - program to execute commands after a set interval
# Author: Vaidik Kapoor  <kapoor.vaidik@gmail.com>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys

'''
Gets command-line arguments
'''
def get_arg(arg, size=1):
	argc = len(sys.argv)

	i = 0
	for i in range(0, argc):
		if sys.argv[i] == arg:
			try:
				arg_val = []
				j = 0
				for j in range(1, size+1):
					arg_val.append(sys.argv[i+j])

				if len(arg_val) > 0:
					return arg_val
			except IndexError:
				print "%s option needs a value as an argument." % arg

	return None

