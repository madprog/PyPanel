# vim: ts=4 sw=4 et list

"""
PyPanel v2.4 - Lightweight panel/taskbar for X11 window managers
Copyright (c) 2003-2005 Jon Gelo (ziljian@users.sourceforge.net)
Copyright (c) 2011 Paul Morelle (paul.morelle@gmail.com)

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
"""

import Xlib

import views

#----------------------------------------------------------------------------
class BaseController:
#----------------------------------------------------------------------------
    EVENT_MAPPING = {
            Xlib.X.ButtonRelease:   'on_button_release',
            Xlib.X.DestroyNotify:   'on_destroy_notify',
            Xlib.X.PropertyNotify:  'on_property_notify',
            Xlib.X.ConfigureNotify: 'on_configure_notify',
            Xlib.X.ClientMessage:   'on_client_message',
            Xlib.X.EnterNotify:     'on_enter_notify',
            Xlib.X.FocusIn:         'on_focus_in',
            Xlib.X.Expose:          'on_expose',
            }
    #------------------------------------------------------
    def __init__(self, display):
    #------------------------------------------------------
        self.display = display

        self.view = views.DefaultView(display, self.x, self.y, self.width, self.height)

    #-------------
    def run(self):
    #-------------
        while True:
            while self.display.pending_events():
                event = self.display.next_event()
                handler_name = BaseController.EVENT_MAPPING.get(event.type, '')
                handler = getattr(self, handler_name, None)
                if handler:
                    handler(event)

#----------------------------------------------------------------------------
class BottomController(BaseController):
#----------------------------------------------------------------------------
    #------------------------------------------------------
    def __init__(self, display, thickness, length, shift, spacer):
    #------------------------------------------------------
        self.spacer = spacer

        if length == 0:
            length = display.screen().width_in_pixels

        if shift == -1:
            shift = (display.screen().width_in_pixels - length) >> 1

        self.x = shift
        self.y = display.screen().height_in_pixels - thickness
        self.width = length
        self.height = thickness

        print 'BottomController', self.x, self.y, self.width, self.height
        BaseController.__init__(self, display)

#----------------------------------------------------------------------------
class LeftController(BaseController):
#----------------------------------------------------------------------------
    #------------------------------------------------------
    def __init__(self, display, thickness, length, shift, spacer):
    #------------------------------------------------------
        self.spacer = spacer

        if length == 0:
            length = display.screen().height_in_pixels

        if shift == -1:
            shift = (display.screen().height_in_pixels - length) >> 1

        self.x = 0
        self.y = shift
        self.width = thickness
        self.height = length

        print 'LeftController', self.x, self.y, self.width, self.height
        BaseController.__init__(self, display)

#----------------------------------------------------------------------------
class RightController(BaseController):
#----------------------------------------------------------------------------
    #------------------------------------------------------
    def __init__(self, display, thickness, length, shift, spacer):
    #------------------------------------------------------
        self.spacer = spacer

        if length == 0:
            length = display.screen().height_in_pixels

        if shift == -1:
            shift = (display.screen().height_in_pixels - length) >> 1

        self.x = display.screen().width_in_pixels - thickness
        self.y = shift
        self.width = thickness
        self.height = length

        print 'RightController', self.x, self.y, self.width, self.height
        BaseController.__init__(self, display)

#----------------------------------------------------------------------------
class TopController(BaseController):
#----------------------------------------------------------------------------
    #------------------------------------------------------
    def __init__(self, display, thickness, length, shift, spacer):
    #------------------------------------------------------
        self.spacer = spacer

        if length == 0:
            length = display.screen().width_in_pixels

        if shift == -1:
            shift = (display.screen().width_in_pixels - length) >> 1

        self.x = shift
        self.y = 0
        self.width = length
        self.height = thickness

        print 'TopController', self.x, self.y, self.width, self.height
        BaseController.__init__(self, display)

BOTTOM = 0
LEFT   = 1
RIGHT  = 2
TOP    = 3

CONTROLLERS = {
        BOTTOM: BottomController,
        LEFT:   LeftController,
        RIGHT:  RightController,
        TOP:    TopController,
        }

