#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import mesontools, pisitools


def setup():
    mesontools.configure('-Denable-gtk-doc=true')


def build():
    mesontools.build()


def install():
    mesontools.install()

    pisitools.dodoc("AUTHORS", "COPYING", "COPYING.LIB", "MAINTAINERS", "NEWS", "README")
