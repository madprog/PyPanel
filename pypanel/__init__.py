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

import controllers
import views

#--------------------------------------------------------------------------------
def run(display, side=controllers.BOTTOM, thickness=24, length=0, shift=0, spacer=6):
#--------------------------------------------------------------------------------
    """ Initialize and display the panel """
    controllers.CONTROLLERS[side](display, thickness, length, shift, spacer).run()
