'''Here are steps about how to use python future'''
#1. pip install future

#2. If start a new project with Python3:

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

# Write your python3 code below:


#3. Make existing python 3 code to support python 2
Running "pasteurize -w mypy3module.py"

#4. Make existing python 2 code to support python 3
Stage 1: futurize --stage1 -w mypackage/*.py
Stage 2: futurize --stage2 -w mypackage/*.py