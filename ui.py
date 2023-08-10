#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  clase2.py
#
#  Copyright 2023 OEM Configuration (temporary user) <oem@Lenovo>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class MainWindows(Gtk.Window):
	def __init__(self):
		super(MainWindows,self).__init__()
		self.connect("destroy", self.on_destroy)
		self.set_default_size(400,300)

		btn= Gtk.Button(label= "Hola a Todos")
		btn.connect('clicked', self.on_clicked)
		btn2= Gtk.Button(label= "Me cago en Linux")
		vbox= Gtk.HBox()
		vbox.pack_start(btn,False,False,0)
		vbox.pack_start(btn2,False,False,0)

		self.add(vbox)

		self.show_all()
	def on_destroy():
		Gtk.main_quit()
	def on_clicked(self,btn):
		print("Click")
	def run(self):
		Gtk.main()


def main(args):
    mainwdw = MainWindows()
    mainwdw.run()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))