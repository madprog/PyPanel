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
import sys

import ppmodule

#----------------------------------------------------------------------------
class BaseView:
#----------------------------------------------------------------------------
    #------------------------------------------------------
    def __init__(self, display, x, y, width, height):
    #------------------------------------------------------
        self.display = display
        self.x       = x
        self.y       = y
        self.width   = width
        self.height  = height

        self.screen  = display.screen()
        self.root    = self.screen.root
        #self.error   = Xlib.error.CatchError()

        self.window = self.root.create_window(self.x, self.y, self.width, self.height,
                0, self.screen.root_depth, window_class=Xlib.X.InputOutput,
                visual=Xlib.X.CopyFromParent, colormap=Xlib.X.CopyFromParent,
                event_mask=(
                    Xlib.X.ExposureMask |
                    Xlib.X.ButtonPressMask |
                    Xlib.X.ButtonReleaseMask |
                    Xlib.X.EnterWindowMask)
                )
        #ppmodule.ppinit(self.window.id, "bitstream vera sans-8")

        self._set_props()
        self.window.map()
        self.display.flush()

    #-------------------------------------
    def _set_props(self):
    #-------------------------------------
        """ Set necessary X atoms and panel window properties """
        self._ABOVE                   = self.display.intern_atom("_NET_WM_STATE_ABOVE")
        self._BELOW                   = self.display.intern_atom("_NET_WM_STATE_BELOW")
        self._BLACKBOX                = self.display.intern_atom("_BLACKBOX_ATTRIBUTES")
        self._CHANGE_STATE            = self.display.intern_atom("WM_CHANGE_STATE")
        self._CLIENT_LIST             = self.display.intern_atom("_NET_CLIENT_LIST")
        self._CURRENT_DESKTOP         = self.display.intern_atom("_NET_CURRENT_DESKTOP")
        self._DESKTOP                 = self.display.intern_atom("_NET_WM_DESKTOP")
        self._DESKTOP_COUNT           = self.display.intern_atom("_NET_NUMBER_OF_DESKTOPS")
        self._DESKTOP_NAMES           = self.display.intern_atom("_NET_DESKTOP_NAMES")
        self._HIDDEN                  = self.display.intern_atom("_NET_WM_STATE_HIDDEN")
        self._ICON                    = self.display.intern_atom("_NET_WM_ICON")
        self._NAME                    = self.display.intern_atom("_NET_WM_NAME")
        self._RPM                     = self.display.intern_atom("_XROOTPMAP_ID")
        self._SHADED                  = self.display.intern_atom("_NET_WM_STATE_SHADED")
        self._SHOWING_DESKTOP         = self.display.intern_atom("_NET_SHOWING_DESKTOP")
        self._SKIP_PAGER              = self.display.intern_atom("_NET_WM_STATE_SKIP_PAGER")
        self._SKIP_TASKBAR            = self.display.intern_atom("_NET_WM_STATE_SKIP_TASKBAR")
        self._STATE                   = self.display.intern_atom("_NET_WM_STATE")
        self._STICKY                  = self.display.intern_atom("_NET_WM_STATE_STICKY")
        self._STRUT                   = self.display.intern_atom("_NET_WM_STRUT")
        self._STRUTP                  = self.display.intern_atom("_NET_WM_STRUT_PARTIAL")
        self._WMSTATE                 = self.display.intern_atom("WM_STATE")
        self._WIN_STATE               = self.display.intern_atom("_WIN_STATE")
        self._MOTIF_WM_HINTS          = self.display.intern_atom("_MOTIF_WM_HINTS")
        self._NET_WM_WINDOW_TYPE      = self.display.intern_atom("_NET_WM_WINDOW_TYPE")
        self._NET_WM_WINDOW_TYPE_DOCK = self.display.intern_atom("_NET_WM_WINDOW_TYPE_DOCK")

        self.window.set_wm_name("PyPanel")

        self.window.set_wm_class("pypanel","PyPanel")

        self.window.set_wm_hints(flags=(
                Xlib.Xutil.InputHint |
                Xlib.Xutil.StateHint),
            input=0, initial_state=1)

        self.window.set_wm_normal_hints(flags=(
                Xlib.Xutil.PPosition |
                Xlib.Xutil.PMaxSize |
                Xlib.Xutil.PMinSize),
            min_width=self.width, min_height=self.height,
            max_width=self.width, max_height=self.height)

        self.window.change_property(self._WIN_STATE, Xlib.Xatom.CARDINAL,32,[1])

        self.window.change_property(self._MOTIF_WM_HINTS, self._MOTIF_WM_HINTS, 32, [0x2, 0x0, 0x0, 0x0, 0x0])

        self.window.change_property(self._DESKTOP, Xlib.Xatom.CARDINAL, 32, [0xffffffffL])
        self.window.change_property(self._NET_WM_WINDOW_TYPE, Xlib.Xatom.ATOM, 32, [self._NET_WM_WINDOW_TYPE_DOCK])

#----------------------------------------------------------------------------
class DefaultView(BaseView):
#----------------------------------------------------------------------------
    #------------------------------------------------------
    def __init__(self, display, x, y, width, height):
    #------------------------------------------------------
        BaseView.__init__(self, display, x, y, width, height)

