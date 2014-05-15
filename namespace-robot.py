from glob import glob
from re import match
from string import split

print glob(".*")


for header_filename in glob("*.h"):
    print header_filename
    header_file = open(header_filename,'r+')

    for line in header_file.readlines():
        #print line
        namespace_match = match("namespace",line)
        if namespace_match:
            print line



