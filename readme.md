# Introduction
Welcome to my small python project.
This library just provides some functions to read from csv files.
I developed this library for fun.
If anyone wants to contribute, feel free to contact me or open an issue.
This library uses the built-in `csv` module

## Installation
Type this into your command prompt:
`pip install csv-reader`

## Usage

at the top of your py files:
```python
from reader import Reader
```

in your code:
```python
with Reader.openWithName("test.csv") as file:
    for line in file:
        print(line)
```

## Documentation
<br>
Visit https://csv-reader.readthedocs.io/en/latest for the documentation.
<br>
<br>

```python
openWithName(name: str)
```
opens a file with the given file name and returns a context manager.<br>
`name - the name of the csv file.`<br>
`throws: FileNotFoundError - when the file could not be found.`
e.g.
```python
with Reader.openWithName("test.csv") as file:
    for line in file:
        print(line)
```
<br>
note: when used in a `for` loop, each `line` is a list of values in each line of the file.

```python
openWithFile(file: TextIO)
```
returns a context manager from an already opened file.<br>
`file - the file object.`<br>
`throws: FileNotFoundError - when the file could not be found.`
e.g.
``` python
with Reader.openWithFile(open("test.csv" newline="")) as file:
    for line in file:
        print(line)
```
<br>
note: when used in a `for` loop, each `line` is a list of values in each line of the file.

```python
readFromName(name: str)
```
opens a file with given name and returns a context manager that yields an iterator that yields each line in the file.<br>
`name - the name of the csv file.`<br>
`throws: FileNotFoundError - when the file could not be found.`
e.g.
```python
with Reader.readFromName("test.csv") as file:
    for line in file:
        print(line)
```
<br>
note: `line` is a string.

```python
readFromFile(file: TextIO)
```
returns an context manager from an already opened file that yields an iterator that yields each line in the file.<br>
`file - the file object.`<br>
`throws: FileNotFoundError - when the file could not be found.`
e.g.
```python
with Reader.readFromFile(open("test.csv", newline="")) as file:
    for line in file:
        print(line)
```
<br>
note: `line` is a string.