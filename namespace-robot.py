#!/usr/bin/env python

from glob import glob
from re import match
from string import split
import sys

args = sys.argv[1:]

if len(args) == 2:
    old_namespace = args[0]
    new_namespace = args[1]
else:
    print " Usage: namespace-robot.py <old_namespace> <new_namespace>"
    sys.exit()


for header_filename in glob("*.h"):
    print "Processing " + header_filename
    header_file = open(header_filename,'r')
    file_data_modified = False
    header_file_data = header_file.readlines()
    
    try:
        namespace_pattern = "namespace"
        for line_index,line in enumerate(header_file_data):
            namespace_match = match(namespace_pattern,line)
            if namespace_match:
                line_words = split(line)
                for word_index in range(len(line_words)):
                    if line_words[word_index] == namespace_pattern:
                        break
                try:
                    if line_words[word_index+1] == old_namespace:
                        #print " Replacing namespace " + old_namespace + " by " + new_namespace
                        line_words[word_index+1] = new_namespace
                        header_file_data[line_index] = " ".join(line_words) + "\n"
                        file_data_modified = True
                        #print " New line look: " + line
                except IndexError:
                    print " Found empty namespace @" + header_filename

    finally:
        if file_data_modified:
            #print "Writing to file ..."
            header_file = open(header_filename,'w')
            header_file.writelines(header_file_data)
        header_file.close()


