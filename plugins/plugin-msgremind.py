from plugins import *

from datetime import datetime, timezone
def GetPlugin():
    return MsgReminderPlugin()

class MsgReminderPlugin(BasePlugin):
    name = "MsgReminderPlugin"
    version = BotVersion

    lastcheck = datetime.now(timezone.utc)
    lastmessage = lastcheck

    async def OnMessage(self, message):
        if message.content == "xander_msg_reminder":
            if self.lastmessage > self.lastcheck:
                channel = discord.utils.get(message.guild.text_channels, name="reminders")
                if channel == None:
                    return
                allowed_mentions = discord.AllowedMentions(everyone = True)
                await channel.send(content = "@everyone there has been new messages!", allowed_mentions = allowed_mentions)
                self.lastcheck = message.created_at
            return False
        
        self.lastmessage = message.created_at
    