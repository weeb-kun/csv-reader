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

import Reader

def main():
    print("module started.")

def openWithName(name):
    return Reader.openWithName(name)

def openWithFile(file):
    return Reader.openWithFile(file)

def readFromName(name):
    return Reader.readFromName(name)

def readFromFile(file):
    return Reader.readFromFile(file)

if __name__ == '__main__':
    main()
    print("this is a library for reading from csv files.")
