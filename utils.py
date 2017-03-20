#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A collection of useful routines to make this tool work

(C) 2017 by Sysmocom s.f.m.c. GmbH
All Rights Reserved

Author: Philipp Maier

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

# Convert list to an printable ascii hex string
def hexdump(array):
	if array:
		return ''.join('{:02x}'.format(x) for x in array)
	else:
		return "(no data)"


# Convert ascii string with decimal numbers to numeric ascii-code list
def ascii_to_list(string):
	rc = []
	for c in string:
		rc.append(ord(c))
	return rc


# Convert an ascii hex string to numeric list
def asciihex_to_list(string):

	string = string.translate(None, ':')
	try:
		return map(ord, string.decode("hex"))
	except:
		print "Warning: Invalid hex string -- ignored!"
		return []


# Pad an ascihex string with a nibble in case it is "incomplete"
def pad_asciihex(string, padding='f'):

	if len(string) % 2 != 0:
		return string + padding
	return string


# Swap nibbles of each byte in an array
def swap_nibbles(array):

	rc = []
	for a in array:
		rc.append(((a & 0xf0) >> 4) | ((a & 0x0f) << 4))
	return rc
