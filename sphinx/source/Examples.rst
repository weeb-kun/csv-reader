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

CSVDictWriter
-------------
