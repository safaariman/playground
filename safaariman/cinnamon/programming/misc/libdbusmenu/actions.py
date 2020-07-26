#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools, shelltools, get

shelltools.export('HAVE_VALGRIND_TRUE', '#')
shelltools.export('HAVE_VALGRIND_FALSE', '')


def setup():
    gtk_version = 2 if get.buildTYPE() == 'gtk2' else 3
    autotools.configure(' '.join([
        '--disable-dumper',
        '--disable-static',
        '--disable-tests',
        '--with-gtk=%s' % gtk_version
    ]))


def build():
    autotools.make()


def install():
    autotools.rawInstall('-j1 -C libdbusmenu-glib DESTDIR=%s' % get.installDIR())
    autotools.rawInstall('-j1 -C libdbusmenu-gtk DESTDIR=%s' % get.installDIR())
