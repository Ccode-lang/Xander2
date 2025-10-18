from plugins import *

def GetPlugin():
    return OnMessagePlugin()

class OnMessagePlugin(BasePlugin):
    name = "OnMessageEvent"
    version = BotVersion

@client.event
async def on_message(message):
    if message.author.id == client.user.id:
        return
    
    go = True

    for plugin in plugins:
        if not hasattr(plugin, "OnMessage_Priority"):
            continue
        try:
            go = await plugin.OnMessage_Priority(message)
        except:
            print(f"An error happened in plugin {plugin.name} during OnMessage_Priority")
    
    for plugin in plugins:
        if not go:
            break
        if not hasattr(plugin, "OnMessage"):
            continue
        try:
            ret = await plugin.OnMessage(message)
            if ret != None:
                go = ret
        except:
            print(f"An error happened in plugin {plugin.name} during OnMessage")