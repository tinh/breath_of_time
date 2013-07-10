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
        self.gd_area_pc = 0
        self.ground_aera = 0
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
        'lowland': getattr(self, 'lowland_design'),
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
        buf_map = self.gen_empty_map(size)
        i = 0
        wall = 0
        ground = 0
        for j in buf_map:
            for k in buf_map[i]:
                if k == 'x':
                    wall += 1
                else:
                    ground += 1
            print buf_map[i]
            i += 1

        print wall, ground, self.ground_aera
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
                length = randint(MIN_SIZE_MAP, self.scale['small'])
                width =  randint(MIN_SIZE_MAP, self.scale['small'])
            elif size == 'medium':
                length = randint(self.scale['small'] + 1, self.scale['medium']) 
                width = randint(self.scale['small'] + 1, self.scale['medium'])
            elif size == 'big':
                length = randint(self.scale['medium'] + 1, self.scale['big'])
                width = randint(self.scale['medium'] + 1, self.scale['big'])
            else:
                return scale_map('medium')

            return length, width, length*width - (length + width) * 2 + 4

        length, width, self.ground_aera = scale_map(size)
        print "length:", length, "\nwidth:", width, "\nground_aera:", self.ground_aera
        
        # debug
        self.map_fd.write(str(length) + " * " + str(width) + "\n\n")
        #

        buf_map = list()
        for i in range(width):
            if not i or i == width - 1:
                buf_map.append(self.elem_map['Dzone']*length)
            else:
                buf_map.append(self.elem_map['Dzone'] + self.elem_map['ground']\
                    *(length - 2) + self.elem_map['Dzone'])
            
        return buf_map

    def lowland_design(self):
        """forest_design method"""

        self.gd_area_pc = 80
        pass

    def forest_design(self):
        """dungeon_design"""

        self.gd_area_pc = 20
        pass

    def dungeon_design(self):
        """desert_design method"""

        self.gd_area_pc = 95
        pass

    def desert_design(self):
        """snow_design"""

        self.gd_area_pc = 95
        pass

    def snow_design(self):
        """snow_design"""

        self.gd_area_pc = 95
        pass

    def design_show(self):
        return self.design_map
