class BasePlugin(object):
    name = "DefaultName"
    version = "0.0.1"
    def __init__(self):
        print(f"Plugin {self.name} ({self.version}) load started.")
    async def OnLoad(self):
        print(f"Plugin {self.name} ({self.version}) loaded")

BotVersion = "0.1"

import __main__
from __main__ import *
from traceback import format_exc

def GetOtherPlugin(string):
    for plugin in plugins:
        if plugin.name == string:
            return plugin

async def PluginHook(name, object):
    config = GetOtherPlugin("ConfigPlugin_Event_")
    go = True
    for plugin in plugins:
        if not go:
            break
        try:
            skipplugin = not config.config["enable"][plugin.name]
        except:
            if plugin.name.endswith("_Event_"):
                skipplugin = False
            else:
                skipplugin = True
                print(f"Plugin \"{plugin.name}\" does not have an enable config disabling it by default.")
        if not hasattr(plugin, name) or skipplugin:
            continue
        try:
            ret = await getattr(plugin, name)(object)
            if ret != None:
                go = ret
        except:
            print(f"An error happened in plugin {plugin.name} during {name}:\n{format_exc()}")