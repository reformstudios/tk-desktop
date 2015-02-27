# Copyright (c) 2013 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

import sgtk

def start_server():
    """
    Starts the desktop server (non-blocking).

    This simple passthrough method is here since access to a framework is not available in the engine.
    """
    '''
    import sys
    sys.path.append('/Users/rivestm/python/3rd/pycharm-debug.egg')
    import pydevd
    pydevd.settrace('localhost', port=49931, stdoutToServer=True, stderrToServer=True)
    '''

    fw = sgtk.platform.get_framework("tk-framework-desktopserver")
    fw.start_server(True, True)
