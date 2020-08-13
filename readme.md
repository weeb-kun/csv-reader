# Introduction
Welcome to my small python project.
This library just provides some functions to read from csv files.
I developed this library for fun.
If anyone wants to contribute, feel free to contact me or open an issue.
This library uses the built-in `csv` module

## Installation
Type this into your command prompt:
`pip install csv-reader`

## usage

at the top of your py files:
```python
import reader
```

in your code:
```python
for line in reader.openWithName("example.csv"):
    print(",".join(line))
```

## Documentation

```python
openWithName(name: str) -> Iterable
```
opens a csv file with the given name and returns the reader object.
`name - the name of the csv file.`

```python
openWithFile(file: TextIO) -> Iterable
```
returns a reader object from an already opened file.
`file - the file object.`

```python
readFromName(name: str) -> Iterator
```
opens a csv file and returns an iterator for that file.
`name - the name of the csv file.`

```python
readFromFile(file: TextIO) -> Iterator
```
returns an iterator from a given file object.
`file - the file object.`