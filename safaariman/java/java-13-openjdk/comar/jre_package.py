#!/usr/bin/env python

import os

executables = (
    'jaotc', 'java', 'jfr', 'jjs', 'jrunscript', 'keytool', 'pack200', 'rmid', 'rmiregistry', 'unpack200'
)
bin_dir = '/usr/bin'
jvm_dir = '/usr/lib/jvm/java-13-openjdk'


def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    for executable in executables:
        executable_link = os.path.join(bin_dir, executable)
        executable_path = os.path.join(jvm_dir, 'bin', executable)
        try:
            os.system('update-alternatives --install %s %s %s 2' % (executable_link, executable, executable_path))
        finally:
            os.system('update-alternatives --auto %s' % executable)


def postRemove():
    for executable in executables:
        executable_path = os.path.join(jvm_dir, 'bin', executable)
        try:
            os.system('update-alternatives --remove %s %s' % (executable, executable_path))
        finally:
            os.system('update-alternatives --auto %s' % executable)
