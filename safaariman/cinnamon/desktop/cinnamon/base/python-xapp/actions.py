#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules, pisitools


def build():
    pythonmodules.compile()
    pythonmodules.compile(pyVer=3)


def install():
    pythonmodules.install()
    pythonmodules.install(pyVer=3)

    docs = ("AUTHORS", "ChangeLog", "COPYING", "PKG-INFO", "README", "TODO")

    pisitools.dodoc(*docs, destDir='python-xapp')
    pisitools.dodoc(*docs, destDir='python3-xapp')
