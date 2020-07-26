#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools, autotools, pisitools, get


def setup():
    shelltools.system('NOCONFIGURE=1 ./autogen.sh')
    autotools.configure(
        '--disable-static '
        '--disable-rpath '
        '--enable-introspection '
        '--enable-gdk-backend '
        '--enable-x11-backend '
        '--enable-egl-backend '
        '--enable-wayland-backend '
        '--enable-evdev-input '
        '--enable-gtk-doc'
    )


def build():
    autotools.make()


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING", "NEWS")
