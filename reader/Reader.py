import csv
import typing

def openWithName(name: str) -> typing.Iterable:
    """
    opens a csv file and returns the reader object.
    :param str name: the name of the file to be read from
    :return: the reader iterable object
    """
    with open(name, newline="") as file:
        return csv.reader(file)

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
