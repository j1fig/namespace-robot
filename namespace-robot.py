from glob import glob
from re import match
from string import split
import sys

args = sys.argv[1:]

for arg in args:
    print arg


print glob(".*")


for header_filename in glob("*.h"):
    print header_filename
    header_file = open(header_filename,'r+')

    for line in header_file.readlines():
        #print line
        namespace_match = match("namespace",line)
        if namespace_match:
            print line
            line_words = split(line)
            for word in line_words:
                print word



