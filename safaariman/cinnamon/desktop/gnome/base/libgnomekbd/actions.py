#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools, shelltools, pisitools, get


def setup():
    shelltools.system('NOCONFIGURE=1 ./autogen.sh')
    autotools.configure('--disable-schemas-compile --disable-static')


def build():
    autotools.make()


def install():
    autotools.rawInstall('DESTDIR=%s' % get.installDIR())

    pisitools.dodoc(
        'AUTHORS', 'ChangeLog', 'ChangeLog.libgswitchit', 'ChangeLog.libkbdraw',
        'ChangeLog.obsolete', 'COPYING.LIB', 'MAINTAINERS', 'NEWS', 'README'
    )
