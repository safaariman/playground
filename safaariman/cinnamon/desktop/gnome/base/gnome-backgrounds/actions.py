#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import mesontools, pisitools


def setup():
    mesontools.configure()


def build():
    mesontools.build()


def install():
    mesontools.install()

    pisitools.dodoc(
        "AUTHORS", "ChangeLog", "COPYING", "COPYING_CCBY2", "COPYING_CCBYSA2", "COPYING_CCBYSA3", "NEWS", "README"
    )
