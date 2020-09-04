Examples
^^^^^^^^

Reader
======

openWithName()
--------------

.. code-block:: python

    with Reader.openWithName("test.csv") as file:
    for line in file:
        print(line)


openWithFile()
--------------

.. code-block:: python

    with Reader.openWithFile(open("test.csv" newline="")) as file:
    for line in file:
        print(line)


readFromName()
--------------

.. code-block:: python

    with Reader.readFromName("test.csv") as file:
    for line in file:
        print(line)


readFromFile()
--------------

.. code-block:: python

    with Reader.readFromFile(open("test.csv", newline="")) as file:
    for line in file:
        print(line)

Writer
======

CSVWriter
---------

.. code-block:: python

    with CSVWriter("test.csv") as file:
    file.write(["test1", "test2"])

CSVDictWriter
-------------

.. code-block:: python

    with CSVDictWriter("test.csv", ["field1", "field2"]) as file:
    file.writeRows([
        {"field1":"test1", "field2":"test2"},
        {"field1": "test3", "field2": "test4"}
    ])