"""
Copyright 2020 weebkun

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import csv
import typing
from contextlib import contextmanager

@contextmanager
def openWithName(name: str):
    """
    opens a csv file as a context manager with the name given.
    :param str name: the name of the file to be read from
    :return: the reader iterable object
    """
    f = open(name, newline="")
    resource = csv.reader(f)
    try:
        yield resource
    finally:
        f.close()

@contextmanager
def openWithFile(file: typing.TextIO):
    """
    opens a csv file and returns a context manager that yields the reader object.
    :param typing.TextIO file: the file obj to open
    :return: reader iterable obj
    """
    try:
        yield csv.reader(file)
    finally:
        file.close()

@contextmanager
def readFromName(name: str):
    """
    reads from a csv file and returns a context manager that yields an iterator.
    :param str name: the name of the file to be read
    :return: the iterator
    """
    file = open(name, newline="")
    try:
        yield iterateLines(file)
    finally:
        file.close()

@contextmanager
def readFromFile(file: typing.TextIO):
    """
    reads from a file and returns an context manager that yields an iterator.
    :param typing.TextIO file: the csv file to read from.
    :return: iterator
    """
    try:
        yield iterateLines(file)
    finally:
        file.close()

def iterateLines(file):
    for line in csv.reader(file):
            yield ",".join(line)