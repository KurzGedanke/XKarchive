# XK Archive

[![license MIT License](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/KurzGedanke/XKarchive/blob/master/LICENSE)
[![Python Version 3.7](https://img.shields.io/badge/Python-3.7-blue.svg)](https://github.com/KurzGedanke/XKarchive)
[![Say Thanks!](https://img.shields.io/badge/Donate%20Bitcoin-💵-lightgrey.svg)](https://kurzgedanke.me/donate/)
[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-🐿️.svg)](https://saythanks.io/to/KurzGedanke)

XK Archive is a python script to download all or a specific range of [XKCD Comics](https://xkcd.com).

## Installation

Git Clone the software to your computer:

```bash
$ git clone https://github.com/KurzGedanke/XKarchive
```

Change directory:

```bash
$ cd XKarchive/
```

OPTINAL: Install a virtualenv

```bash
$ virtualenv venv
```

OPTINAL: Active the virtualenv

```bash
$ source venv/bin/activate
```

pip install the requirements

```bash
$ pip install -r requieremnts.txt
```

## Usage

Run the script and enter the latest XKCD you downloaded. If you didn't have downloaded any comics in the past, please enter 1.

Then it asks you for the latest XKCD released. Enter the number.
At the end just enter a path where to download it. If you enter a new folder, it will be created for you.

```bash
(venv) ╭─asgard@asgard-3 ~/Developer/xkarchive  ‹master*›
╰─$ python xkarchive.py
Enter the latest XKCD you downloaded. If you do not have any XKCD, please enter 1.
1
Please enter the latest XKCD:
5
Please enter the download path:
/Users/asgard/Desktop/archiveXKCD
Download Comic: #1
Download Comic: #2
Download Comic: #3
Download Comic: #4
```

## License XKCD Comics

The XKCD are under a [Creative Commons Attribution-NonCommercial 2.5 License](https://creativecommons.org/licenses/by-nc/2.5/).

This means you are free to:

- Share — copy and redistribute the material in any medium or format
- Adapt — remix, transform, and build upon the material

Under the following term: 

- Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
- NonCommercial — You may not use the material for commercial purposes.

To read the full license please click the link above.

## License XK Archive

Copyright 2018 Thore Jahn

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.