from plugins import *
def GetPlugin():
    return GmGnPlugin()

class GmGnPlugin(BasePlugin):
    name = "GmGnPlugin"
    version = BotVersion
    async def OnMessage(self, message):
        if message.content.lower() == "gm":
            await message.channel.send(f"Good morning {message.author.name}!")
        if message.content.lower() == "gn":
            await message.channel.send(f"Good night {message.author.name}!")