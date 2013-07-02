#! /usr/bin/python2

# -*- coding: utf-8 -*-

#
# module gen_map.py for project breath_of_time
# Made by tinh <thms.n@gmail.com>
#

UNKNOWN_MAP 88

class MapGen(object):
    """create map by some criteria:
    size, global form, rooms, gates, etc.
    Objects use to define map:
    x   _________ non_access_zone
    /   _________ wall_right_side
    \   _________ wall_left_side
    |   _________ wall_ver
    -   _________ wall_hor
    o   _________ tree
   ' '  _________ ground
    H   _________ gate
    ~   _________ water
    """

    elem_map = [
    'non_access_zone':'x',
    'wall_right_side': '/',
    'wall_left_side': '\\',
    'wall_ver': '|',
    'wall_hor': '-',
    'tree': 'o',
    'ground': ' ',
    'gate': 'H',
    'water': '~'
    ]

    design_map = [
    'forest': forest_design,
    'dungeon': dungeon_design,
    'desert': desert_design,
    'snow_desert': snow_desert_design 
    ]
    def __init__(self, design, size):
       if design in design_map.has_key(design):
            self.gen_map = design_map[design]
        else:
            print 'unknown map design, exiting'
            exit(UNKNOWN_MAP)
    
      if size > 2:
            self.size = 1
        else:
            self.size = size
    