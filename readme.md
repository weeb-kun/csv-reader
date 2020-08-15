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

## Examples
The examples can also be found at 

### openWithName()

```python
with Reader.openWithName("test.csv") as file:
    for line in file:
        print(line)
```
<br>
note: when used in a `for` loop, each `line` is a list of values in each line of the file.

### openWithFile()
``` python
with Reader.openWithFile(open("test.csv" newline="")) as file:
    for line in file:
        print(line)
```
<br>
note: when used in a `for` loop, each `line` is a list of values in each line of the file.

### readFromName()

```python
with Reader.readFromName("test.csv") as file:
    for line in file:
        print(line)
```
<br>
note: `line` is a string.

### readFromFile()

```python
with Reader.readFromFile(open("test.csv", newline="")) as file:
    for line in file:
        print(line)
```
<br>
note: `line` is a string.