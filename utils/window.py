# -*- coding: utf-8 -*-
'''
Modified version of the code written by Diego Torres Milano
original repository https://github.com/dtmilano/AndroidViewClient
'''

from __future__ import print_function

import sys

DEBUG = False

class Window(object):
    '''
    Window class
    '''

    def __init__(self, num, winId, activity, wvx, wvy, wvw, wvh, px, py, visibility, focused=False):
        '''
        Constructor

        @type num: int
        @param num: Ordering number in Window Manager
        @type winId: str
        @param winId: the window ID
        @type activity: str
        @param activity: the activity (or sometimes other component) owning the window
        @type wvx: int
        @param wvx: window's virtual X
        @type wvy: int
        @param wvy: window's virtual Y
        @type wvw: int
        @param wvw: window's virtual width
        @type wvh: int
        @param wvh: window's virtual height
        @type px: int
        @param px: parent's X
        @type py: int
        @param py: parent's Y
        @type visibility: int
        @param visibility: visibility of the window
        '''

        if DEBUG: print("Window(%d, %s, %s, %d, %d, %d, %d, %d, %d, %d)" % \
                (num, winId, activity, wvx, wvy, wvw, wvh, px, py, visibility), file=sys.stderr)
        self.num = num
        self.winId = winId
        self.activity = activity
        self.wvx = wvx
        self.wvy = wvy
        self.wvw = wvw
        self.wvh = wvh
        self.px = px
        self.py = py
        self.visibility = visibility
        self.focused = focused

    def __str__(self):
        return "Window(%d, wid=%s, a=%s, x=%d, y=%d, w=%d, h=%d, px=%d, py=%d, v=%d, f=%s)" % \
                (self.num, self.winId, self.activity, self.wvx, self.wvy, self.wvw, self.wvh, self.px, self.py, self.visibility, self.focused)

