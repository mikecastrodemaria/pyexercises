"""Reading input with the fileinput module.

fileinput reads from the files given on the command line, or from standard
input when there are none. Handy for small tools.
"""

import fileinput

# Run it as:  python3 fileinput_module.py somefile.txt
# or as:      echo "hello" | python3 fileinput_module.py

for line in fileinput.input():
    print(fileinput.filename(), fileinput.lineno(), line.strip())

# What to remember
# 1. fileinput handles "a file, or whatever is piped in" for you
# 2. fileinput.lineno() gives the line number, which is useful in error messages
# 3. For the final project, open() is the tool you will actually use
