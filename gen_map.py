#! /usr/bin/python2

# -*- coding: utf-8 -*-

#
# module gen_map.py for project breath_of_time
# Made by tinh <thms.no@gmail.com>
#

from os import (listdir, mkdir, getcwd, curdir)
from random import randint

UNABLE_WRITING =    "can't write on %s\nPlease change \
permissions on it\nExiting"
DIR_MAP =           'maps/'
NAME_MAP =          '%s_%d.map'
MIN_SIZE_MAP =      8

class MapGen(object):
    """
    create map by some criteria:
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

    def __init__(self):
        self.map_file = None
        self.map_fd = None
        self.design = None
        self.size = None
        self.func_map = None
        self.elem_map = {
        'Dzone': 'x',
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
        self.scale = {
        'small': 20,
        'medium': 50,
        'big': 70
        }

    def create_file_map(self, design, size):
        """
        method to create/read maps rep.
        allow MapGen class to create coherent map files
        """

        if self.design_map.has_key(design):
            self.design = design
            self.func_map = self.design_map[design]
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
        self.map_fd = open(self.map_file, 'w')
        self.map_fd.write("%s file map" % self.design)
        self.gen_empty_map(size)
        self.func_map()

    def gen_empty_map(self, size):
        """
        will build a rectangle filled with Dzone carac
        to delimite the surface of the current map
        """
        def scale_map(size):
            """
            choose map scale between scale options definning in __init__
            8*8 - 20*20 max. (small) --> 400 blocks,
            21*21 - 50*50 max (medium) --> 2500 blocks,
            51*51 - 70*70 max. (big) --> 4900 blocks
            """

            if size == 'small':
                return randint(MIN_SIZE_MAP, self.scale['small']), randint(MIN_SIZE_MAP, self.scale['small'])
            elif size == 'medium':
                return randint(self.scale['small'] + 1, self.scale['medium']), randint(self.scale['small'] + 1, self.scale['medium'])
            elif size == 'big':
                return randint(self.scale['medium'] + 1, self.scale['big']), randint(self.scale['medium'] + 1, self.scale['big'])
            else:
                return scale_map('medium')

        length, width = scale_map(size)
        self.map_fd.write("\n========\n\n")
        # debug
        self.map_fd.write(str(length) + " * " + str(width) + "\n\n")
        
        buf_map = [self.elem_map['Dzone'] * length for i in range(width)]

        ### debug
        print buf_map[1].__len__()
        print buf_map[2].__len__() 
        ### debug


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
