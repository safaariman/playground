#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import kde4
#from pisi.actionsapi import pisitools

# if pisi can't find source directory, see /var/pisi/Homerun/work/ and:
# WorkDir="Homerun-"+ get.srcVERSION() +"/sub_project_dir/"

def setup():
    kde4.configure()

def build():
    kde4.make()

def install():
    kde4.install()

# Take a look at the source folder for these file as documentation.
#    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "COPYING", "README")

# If there is no install rule for a runnable binary, you can 
# install it to binary directory.
#    pisitools.dobin("Homerun")

# You can use these as variables, they will replace GUI values before build.
# Package Name : Homerun
# Version : 1.2.5
# Summary : An application launcher for KDE Plasma desktop

# For more information, you can look at the Actions API
# from the Help menu and toolbar.

# By PiSiDo 2.0.0
