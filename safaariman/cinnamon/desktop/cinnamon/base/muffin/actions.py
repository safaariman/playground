#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools, shelltools, pisitools, get


def setup():
    shelltools.system('NOCONFIGURE=1 ./autogen.sh')
    autotools.configure(
        '--enable-startup-notification=yes '
        '--disable-silent-rules '
        '--enable-compile-warnings=no '
        '--disable-Werror '
        '--disable-static '
        '--disable-scrollkeeper '
        '--disable-clutter-doc '
        '--disable-wayland-egl-platform '
        '--disable-wayland-egl-server '
        '--disable-kms-egl-platform '
        '--disable-wayland '
        '--disable-native-backend'
    )


def build():
    autotools.make()


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "MAINTAINERS", "NEWS", "README", "README-Mutter")
