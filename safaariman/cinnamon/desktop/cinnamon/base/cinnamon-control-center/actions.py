#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools, shelltools, pisitools, get


def setup():
    shelltools.system('NOCONFIGURE=1 ./autogen.sh')
    autotools.configure()


def build():
    autotools.make()


def install():
    autotools.rawInstall("-C shell DESTDIR=%s" % get.installDIR(), 'install-libcinnamon_control_center_includeHEADERS')
    autotools.rawInstall("-C shell DESTDIR=%s" % get.installDIR(), 'install-libLTLIBRARIES')
    autotools.rawInstall("-C shell DESTDIR=%s" % get.installDIR(), 'install-pkgconfigDATA')
    autotools.rawInstall("-C panels DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "MAINTAINERS", "NEWS", "README")
