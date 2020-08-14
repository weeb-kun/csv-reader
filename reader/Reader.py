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
    resoure = csv.reader(f)
    try:
        yield f
    finally:
        f.close()

def openWithFile(file: typing.TextIO) -> typing.Iterable:
    """
    opens a csv file and returns the reader object. uses an already opened file.
    :param typing.TextIO file: the file obj to open
    :return: reader iterable obj
    """
    return csv.reader(file)

def readFromName(name: str) -> typing.Iterator:
    """
    reads from a csv file and returns an iterator for it.
    :param str name: the name of the file to be read
    :return: the iterator
    """
    with open(name, newline="") as file:
        for line in csv.reader(file):
            yield ",".join(line)

def readFromFile(file: typing.TextIO) -> typing.Iterator:
    """
    reads from a file and returns an iterator.
    :param typing.TextIO file: the csv file to read from.
    :return: iterator
    """
    for line in csv.reader(file):
        yield ",".join(line)
