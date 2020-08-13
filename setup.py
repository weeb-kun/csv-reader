from setuptools import setup

setup(
    name="csv-reader",
    version="1.0.0",
    description="reader library for csv files.",
    author="weebkun",
    packages=["reader"],
    entry_points={
        "console_scripts": [
            "reader=reader.__main__"
        ]
    },
    license="Apache 2.0"
)
