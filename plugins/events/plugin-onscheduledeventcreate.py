from plugins import *

def GetPlugin():
    return OnScheduledEventCreatePlugin()

class OnScheduledEventCreatePlugin(BasePlugin):
    name = "OnScheduledEventCreate_Event_"
    version = BotVersion

@client.event
async def on_scheduled_event_create(event):
    await PluginHook("OnScheduledEventCreate", event)