from plugins import *
import json
def GetPlugin():
    return ConfigPlugin()

class ConfigPlugin(BasePlugin):
    name = "ConfigPlugin_Event_"
    version = BotVersion

    config = None

    async def OnLoad(self):
        try:
            file = open("config.json", "r")
        except:
            print("Failed to load config file.")
            await client.close()
            return
        try:
            self.config = json.loads(file.read())
        except:
            print("Failed to deserialize config json.")
            await client.close()
            return
        file.close()
        await super().OnLoad()