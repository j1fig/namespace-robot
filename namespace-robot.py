#!/usr/bin/env python

from glob import glob
import re
import string
import sys

def find_pattern(pattern,data_string):
    pattern_match = re.search(pattern,data_string)
    if pattern_match:
        return True
    return False


def replace_pattern(data_string,replaced_string,replacing_string):
    data_string = string.replace(data_string,replaced_string,replacing_string)
    return data_string

def find_and_replace_namespace(header_file_data):
    file_data_modified = False
    namespace_pattern = "namespace" + " " + old_namespace
    namespace_scope_pattern = old_namespace + "::"
    namespace_using_pattern = old_namespace + ";"
    for line_index,line in enumerate(header_file_data):
        init_data = header_file_data[line_index]
        if find_pattern(namespace_pattern, header_file_data[line_index]):
            header_file_data[line_index] = replace_pattern(header_file_data[line_index], 
                                                           old_namespace, 
                                                           new_namespace)
        if find_pattern(namespace_scope_pattern, header_file_data[line_index]):
            header_file_data[line_index] = replace_pattern(header_file_data[line_index], 
                                                           namespace_scope_pattern, 
                                                           new_namespace + "::")
        
        if not (init_data is header_file_data[line_index]):
            file_data_modified = True
            print "Modified line to: " + header_file_data[line_index]

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


