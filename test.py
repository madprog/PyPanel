import Xlib
import Xlib.display

display = Xlib.display.Display()
screen = display.screen()
root = screen.root

window = root.create_window(
		0, 0, 800, 600,
		0,
		screen.root_depth,
		window_class=Xlib.X.InputOutput,
		visual=Xlib.X.CopyFromParent,
		colormap=Xlib.X.CopyFromParent,
		event_mask=(
			Xlib.X.ExposureMask
			|Xlib.X.ButtonPressMask
			|Xlib.X.ButtonReleaseMask
			|Xlib.X.EnterWindowMask
		)
	)
_WIN_STATE = display.intern_atom("_WIN_STATE")
_MOTIF_WM_HINTS = display.intern_atom("_MOTIF_WM_HINTS")

window.set_wm_name("PyPanel")
window.set_wm_class("pypanel","PyPanel")
window.set_wm_hints(flags=(Xlib.Xutil.InputHint|Xlib.Xutil.StateHint), input=0, initial_state=1)
window.set_wm_normal_hints(flags=(Xlib.Xutil.PPosition|Xlib.Xutil.PMaxSize|Xlib.Xutil.PMinSize),
		min_width=800, min_height=600,
		max_width=800, max_height=600)
window.change_property(_WIN_STATE,Xlib.Xatom.CARDINAL,32,[1])
window.change_property(_MOTIF_WM_HINTS, _MOTIF_WM_HINTS, 32, [0x2, 0x0, 0x0, 0x0, 0x0])
#window.change_property(self._DESKTOP, Xatom.CARDINAL, 32, [0xffffffffL])
#window.change_property(dsp.intern_atom("_NET_WM_WINDOW_TYPE"),
    #Xatom.ATOM, 32, [dsp.intern_atom("_NET_WM_WINDOW_TYPE_DOCK")])
