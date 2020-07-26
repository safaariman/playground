#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools, autotools, pisitools, get


def setup():
    shelltools.system('NOCONFIGURE=1 ./autogen.sh')
    autotools.configure(
        '--enable-cairo=yes '
        '--enable-gdk-pixbuf=yes '
        '--enable-cogl-pango=yes '
        '--enable-cogl-gst=yes '
        '--enable-gl=yes '
        '--enable-glx=yes '
        '--enable-sdl2=yes '
        '--enable-null-egl-platform=yes '
        '--enable-wayland-egl-platform=yes '
        '--enable-kms-egl-platform=yes '
        '--enable-xlib-egl-platform=yes '
        '--enable-wayland-egl-server=yes '
        '--enable-gtk-doc=yes '
        '--enable-introspection=yes '
        '--enable-examples-install=no '
    )


def build():
    autotools.make()


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ChangeLog", "COPYING", "NEWS", "README.in")
