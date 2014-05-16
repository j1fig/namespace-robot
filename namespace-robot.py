#!/usr/bin/env python

from glob import glob
import re
import string
import sys

def find_and_replace_namespace(header_file_data):
    file_data_modified = False
    namespace_pattern = "namespace" + " " + old_namespace
    namespace_scope_pattern = old_namespace + "::"
    for line_index,line in enumerate(header_file_data):
        namespace_match = re.search(namespace_pattern,line)
        if namespace_match:
            string.replace(header_file_data[line_index],old_namespace,new_namespace)
            file_data_modified = True
            continue
        namespace_scope_match = re.search(namespace_scope_pattern,line)
        if namespace_scope_match:
            print " Old line: " + header_file_data[line_index]
            string.replace(header_file_data[line_index],namespace_scope_pattern,new_namespace + "::")
            file_data_modified = True
            print " New line: " + header_file_data[line_index]

    return file_data_modified



args = sys.argv[1:]

if len(args) == 2:
    old_namespace = args[0]
    new_namespace = args[1]
else:
    print " Usage: namespace-robot.py <old_namespace> <new_namespace>"
    sys.exit()


for header_filename in glob("*.h"):
    header_file = open(header_filename,'r')
    file_data_modified = False
    header_file_data = header_file.readlines()
    
    try:
        file_data_modified = find_and_replace_namespace(header_file_data)
    finally:
        if file_data_modified:
            print "Namespace changed for file " + header_filename
            header_file = open(header_filename,'w')
            header_file.writelines(header_file_data)
        header_file.close()


