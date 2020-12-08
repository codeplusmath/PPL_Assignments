
from __future__ import division
import math
import time
import cairo
import gi; gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
from gi.repository.GdkPixbuf import Pixbuf
import random

class Brush(object):
    def __init__(self, width, rgba_color):
        self.width = width
        self.rgba_color = rgba_color
        self.stroke = []

    def add_point(self, point):
        self.stroke.append(point)

class Canvas(object):
    def __init__(self):
        self.draw_area = self.init_draw_area()
        self.brushes = []

    def draw(self, widget, cr):
        da = widget
        cr.set_source_rgba(0, 0, 0, 1)
        cr.paint()
        #cr.set_operator(cairo.OPERATOR_SOURCE)#gets rid over overlap, but problematic with multiple colors
        for brush in self.brushes:
            cr.set_source_rgba(*brush.rgba_color)
            cr.set_line_width(brush.width)
            cr.set_line_cap(1)
            cr.set_line_join(cairo.LINE_JOIN_ROUND)
            cr.new_path()
            for x, y in brush.stroke:
                cr.line_to(x, y)
            cr.stroke()

    def init_draw_area(self):
        draw_area = Gtk.DrawingArea()
        draw_area.connect('draw', self.draw)
        draw_area.connect('motion-notify-event', self.mouse_move)
        draw_area.connect('button-press-event', self.mouse_press)
        draw_area.connect('button-release-event', self.mouse_release)
        draw_area.set_events(draw_area.get_events() |
            Gdk.EventMask.BUTTON_PRESS_MASK |
            Gdk.EventMask.POINTER_MOTION_MASK |
            Gdk.EventMask.BUTTON_RELEASE_MASK)
        return draw_area

    def mouse_move(self, widget, event):
        if event.state & Gdk.EventMask.BUTTON_PRESS_MASK:
            curr_brush = self.brushes[-1]
            curr_brush.add_point((event.x, event.y))
            widget.queue_draw()

    def mouse_press(self, widget, event):
        if event.button == Gdk.BUTTON_PRIMARY:
            rgba_color = (random.random(), random.random(), random.random(), 0.5)
            brush = Brush(12, rgba_color)
            brush.add_point((event.x, event.y))
            self.brushes.append(brush)
            widget.queue_draw()
        elif event.button == Gdk.BUTTON_SECONDARY:
            self.brushes = []

    def mouse_release(self, widget, event):
        widget.queue_draw()

class DrawingApp(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.window = Gtk.Window()
        self.window.set_border_width(8)
        self.window.set_default_size(self.width, self.height)
        self.window.connect('destroy', self.close)
        self.box = Gtk.Box(spacing=6)
        self.window.add(self.box)
        self.canvas = Canvas()
        self.box.pack_start(self.canvas.draw_area, True, True, 0)
        self.window.show_all()

    def close(self, window):
        Gtk.main_quit()

if __name__ == "__main__":
    DrawingApp(400, 400)
    Gtk.main()
