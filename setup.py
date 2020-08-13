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

import pathlib
from setuptools import setup

setup(
    name="csv-reader",
    version="1.0.1",
    long_description= (pathlib.Path(__file__).parent / "readme.md").read_text(),
    long_description_content_type="text/markdown",
    description="reader library for csv files.",
    url="https://github.com/weeb-kun/csv-reader",
    author="weebkun",
    packages=["reader"],
    entry_points={
        "console_scripts": [
            "reader=reader.__main__"
        ]
    },
    license="Apache 2.0"
)
