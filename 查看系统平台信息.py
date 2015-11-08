#usr/bin/env python3
#-*- coding:utf-8 -*-

import platform
def checkPlatformInfo():
    uname=platform.uname()
    print('uname:',uname)
    arch=platform.architecture()
    print('arch:%',arch)
    machine=platform.machine()
    print('machine:',machine)
    node=platform.node()
    print('node:',node)
    platformInfo=platform.platform()
    print('platformInfo:',platformInfo)
    processor=platform.processor()
    print('processor:',processor)
    system=platform.system()
    print('system:',system)
    version=platform.version()
    print('version:',version)


if __name__=='__main__':
    checkPlatformInfo()
