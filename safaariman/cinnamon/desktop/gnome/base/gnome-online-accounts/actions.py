#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools, mesontools


def setup():
    mesontools.configure('-D lastfm=true -D media_server=true -D gtk_doc=true -D man=true')


def build():
    mesontools.build()


def install():
    mesontools.install()

    pisitools.dodoc("COPYING", "NEWS", "README")
