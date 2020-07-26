#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools, pisitools, get


def setup():
    autotools.autoreconf('-fi')
    autotools.configure('--disable-static')


def build():
    autotools.make()


def check():
    autotools.make('-k check || :')


def install():
    autotools.rawInstall('DESTDIR=%s' % get.installDIR())

    pisitools.dodoc('AUTHORS', 'ChangeLog', 'COPYING', 'COPYING.LGPL', 'NEWS', 'README')
