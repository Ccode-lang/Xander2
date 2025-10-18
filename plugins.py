class BasePlugin(object):
    name = "DefaultName"
    version = "0.0.1"
    def __init__(self):
        print(f"Plugin {self.name} ({self.version}) load started.")
    def OnLoad(self):
        print(f"Plugin {self.name} ({self.version}) loaded")

BotVersion = "0.1"

import __main__
from __main__ import *

def GetOtherPlugin(string):
    for plugin in plugins:
        if plugin.name == string:
            return plugin