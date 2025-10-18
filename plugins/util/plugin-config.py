from plugins import *
import json
def GetPlugin():
    return ConfigPlugin()

class ConfigPlugin(BasePlugin):
    name = "ConfigPlugin"
    version = BotVersion

    config = None

    async def OnLoad(self):
        global config
        try:
            file = open("config.json", "r")
        except:
            print("Failed to load config file.")
            await client.close()
            return
        try:
            config = json.loads(file.read())
        except:
            print("Failed to deserialize config json.")
            await client.close()
            return
        file.close()
        super().OnLoad()