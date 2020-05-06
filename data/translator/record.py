#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright © 2020 Ismael Belisario

# This file is part of Open Translation.

# Open Translation is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Open Translation is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Open Translation. If not, see <https://www.gnu.org/licenses/>.

"""
Script Name: translator/__init__.py
System of record for OT.
"""


class Record(object):
    """System of save of record for OT in real time."""

    def __init__(self):
        self.__list = {}  # List (dict) of translations.

    def update(self, url, source, target, text, end_text, headers, status_code):
        """Update list of translations."""

        self.__list.update({len(self.__list): {'url': url, 'source': source,
        'target': target, 'text': text, 'end_text': end_text, 'headers': headers,
                                            'status_code': status_code}})

    def search(self, name, data, other_data=''):
        """Search in the list of translations."""

        if name == 'last': name = len(self.__list) - 1
        #print(self.__list)
        try:
            data = self.__list[name][data]
            return eval(f"data{other_data}")
        except KeyError:
            return [f"KeyError: {name}{data}{other_data} not in histori."]

    def del_histori(self, number):
        """Search in the list of translations."""

        return self.__list.pop(number)

    def get_list(self):
        return self.__list.copy()

    def size(self):
        return len(self.__list)

    def include(self, date):
        return date in self.__list