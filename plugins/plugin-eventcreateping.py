from plugins import *

def GetPlugin():
    return EventCreatePingPlugin()

class EventCreatePingPlugin(BasePlugin):
    name = "EventCreatePingPlugin"
    version = BotVersion
    async def OnScheduledEventCreate(self, event):
        channel = discord.utils.get(event.guild.text_channels, name="announcement")
        if channel == None:
            return
        await channel.send(f"@everyone new event named \"{event.name}\" was created!")