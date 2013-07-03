#! /usr/bin/python2

# -*- coding: utf-8 -*-

#
# module gen_map.py for project breath_of_time
# Made by tinh <thms.n@gmail.com>
#

UNABLE_WRITING =    "can't write on %s\nPlease change permissions \
on it\nExiting"

DIR_MAP =           'maps/'
NAME_MAP =          '%s_%d.map'

from os import (listdir, mkdir, getcwd, curdir)

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
    ~   _________ water"""

    def __init__(self):
        self.map_file = None
        self.design = None
        self.size = None
        self.gen_map = None
        self.view_size = {
        'length': 640,
        'width': 480,
        'ratio': 4/3
        }
        self.elem_map = {
        'non_access_zone': 'x',
        'wall_right_side': '/',
        'wall_left_side': '\\',
        'wall_ver': '|',
        'wall_hor': '-',
        'tree': 'o',
        'ground': ' ',
        'gate': 'H',
        'water': '~'
        }
        self.design_map = {
        'forest': getattr(self, 'forest_design'),
        'dungeon': getattr(self, 'dungeon_design'),
        'desert': getattr(self, 'desert_design'),
        'snow': getattr(self, 'snow_design')
        }

    def create_file_map(self, design, size):
        """method to create/read maps rep.
        allow MapGen class to create coherent map files"""

        if self.design_map.has_key(design):
            self.design = design
            self.gen_map = self.design_map[design]
        else:
            print 'unknown map design, exiting'
            return

        root = listdir(curdir)
        
        if not DIR_MAP[:-1] in root:
            try:
                mkdir(DIR_MAP[:-1], 0755)
            except OSError:
                print UNABLE_WRITING % getcwd()
                return
        rep_map = listdir(DIR_MAP)
        map_nb = 0

        for i in rep_map:
            if self.design in i:
                map_nb += 1

        self.map_file = DIR_MAP + NAME_MAP % (self.design, map_nb)
        open(self.map_file, 'w').write("hey you build a %s file map" % self.design)
        self.gen_map()

    def forest_design(self):
        print "forest_design method"

    def dungeon_design(self):
        print "dungeon_design method"
        
    def desert_design(self):
        print "desert_design method"
        
    def snow_design(self):
        print "snow_design method"

    def design_show(self):
        return self.design_map