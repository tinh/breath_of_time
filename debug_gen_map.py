#! /usr/bin/python2

# -*- coding: utf-8 -*-

#
# module test_gen_map.py for project breath_of_time
# Made by tinh <thms.no@gmail.com>
#

from gen_map import MapGen
from sys import argv

inst = MapGen()

size = 10

try:
    design = argv[1]
    size = argv[2]
except IndexError:
    design_map_keys = inst.design_show().keys()
    while True:
        try:
            design = raw_input("'forest'\n\
'snow'\n\
'desert'\n\
'dungeon'\n\
>>> ")
        except (EOFError, KeyboardInterrupt):
            print "\nBye"
            exit()
        if design in design_map_keys:
            inst.create_file_map(design, 'small')