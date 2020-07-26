#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools, pisitools, get


def setup():
    autotools.autoreconf('-fi')
    autotools.configure('--disable-static --disable-systemd --enable-polkit')


def build():
    autotools.make()


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "COPYING.LIB", "MAINTAINERS", "NEWS", "README")
