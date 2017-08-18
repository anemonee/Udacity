#!/usr/bin/env python
# -*- coding: utf-8 -*-
# So, the problem is that the gigantic file is actually not a valid XML, because
# it has several root elements, and XML declarations.
# It is, a matter of fact, a collection of a lot of concatenated XML documents.
# So, one solution would be to split the file into separate documents,
# so that you can process the resulting files as valid XML documents.

import xml.etree.ElementTree as ET
PATENTS = 'patent.data'

def get_root(fname):
    tree = ET.parse(fname)
    return tree.getroot()

def split_file(filename):
    """
    Split the input file into separate files, each containing a single patent.
    As a hint - each patent declaration starts with the same line that was
    causing the error found in the previous exercises.
    
    The new files should be saved with filename in the following format:
    "{}-{}".format(filename, n) where n is a counter, starting from 0.
    """
    fileo = open(filename, "r")
    line = fileo.readlines()
    n = -1
    b = 1
    a = 0
    xml_values = []
    for i in line:
        if "xml version" in i:
            xml_values.append(a)
        a = a+1
    xml_values.append(len(line))
    n = 0
    for j in range(0,len(xml_values)-1):
        start = xml_values[j]
        end = xml_values[j+1]
        content = line[start:end]
        filew = open("{}-{}".format(filename, n), "w")
        for i in content:
            filew.write(i)
        filew.close
        n = n+1

def test():
    split_file(PATENTS)
    for n in range(4):
        try:
            fname = "{}-{}".format(PATENTS, n)
            f = open(fname, "r")
            if not f.readline().startswith("<?xml"):
                print "You have not split the file {} in the correct boundary!".format(fname)
            f.close()
        except:
            print "Could not find file {}. Check if the filename is correct!".format(fname)


test()

