# Copyright 2020 weebkun

#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

import csv
from contextlib import *
import typing
import os

class CSVWriter(AbstractContextManager):
    """
    the Writer class used to write to csv files. extends contextlib.AbstractContextManager

    :param name: the name of the file
    :type name: str
    :param mode: the mode to open the file in. default is 'a'
    :type mode: str
    """

    def __init__(self, name: str, mode: str = "a"):
        self.file = open(name, mode, newline="")
        self.writer = csv.writer(self.file)

    def write(self, data: list):
        """
        writes a single row to a csv file. the data should be a list of values to write.

        :param data: the list containing values to write
        :type data: list
        :raises Exception: if the file is closed or the writer does not exist
        """
        if self.writer and self.file:
            self.writer.writerow(data)
        else:
            # writer does not exist or file is closed
            raise Exception("Cannot write to a closed file.")

    def writeRows(self, rows: list):
        """
        writes multiple rows to a csv file.

        :param rows: the rows to write to the file
        :type rows: list
        :raises Exception: if the file is closed or the writer does not exist
        """
        if self.writer:
            self.writer.writerows(rows)
        else:
            raise Exception("Cannot write to a closed file.")

    def __enter__(self):
        return self

    def __exit__(self, excType, exc, traceback):
        # close the file and destroy writer.
        self.file.close()
        self.writer = None
        # dont want to propagate the exception but dont want to suppress it either
        return False

    def getFile(self):
        """
        returns the file object attached to this instance.

        :return: the file object
        :rtype: typing.TextIO
        """
        return self.file


class CSVDictWriter(AbstractContextManager):
    """
    a csv writer class for writing dictionaries to csv files. extends contextlib.AbstractContextManager

    :param name: the name of the file to open
    :type name: str
    :param fields: a list of field names to use
    :type fields: list
    :param mode: the mode to open the file in
    :type mode: str
    """

    def __init__(self, name: str, fields: list, mode: str = "a"):
        if os.path.isfile(name):
            # file exists
            with open(name, "r+") as file:
                # seek to beginning of file
                file.seek(0)
                if ", ".join(fields) in file.readline():
                    # fieldnames exist in file
                    # thus i can assume file already has valid data
                    self.file = open(name, mode, newline="")
                    self.writer = csv.DictWriter(self.file, fields)
                else:
                    # fieldnames do not exist
                    if os.path.getsize(name) > 0:
                        # file has random data
                        file.truncate(0)
        else:
            # file does not exist
            self.file = open(name, mode, newline="")
            self.writer = csv.DictWriter(self.file, fields)
            self.writer.writeheader()

    def write(self, data: dict):
        """
        writes a dict to the file as a row.

        :param data: the row to write
        :type data: dict
        :raises Exception: if the file is closed or the writer does not exist
        """
        if self.writer:
            self.writer.writerow(data)
        else:
            raise Exception("Cannot write to a closed file.")

    def writeRows(self, rows: list):
        """
        writes a list of dicts to the file.

        :param rows: the list of dicts to write
        :type rows: list
        :raises Exception: if the file is closed or the writer does not exist
        """
        if self.writer:
            self.writer.writerows(rows)
        else:
            raise Exception("Cannot write to a closed file.")

    def __enter__(self):
        return self

    def __exit__(self, excType, exc, traceback):
        self.file.close()
        self.writer = None
        return False

    def getFile(self):
        """
        returns the file object attached to this instance.

        :return: the file object
        :rtype: typing.TextIO
        """
        return self.file
