import discord
import os
import sys
import inspect
import functools


EventNamesInUse = []

oldevent = discord.Client.event

def newevent(self, coro, /):
    global EventNamesInUse
    if coro.__name__ in EventNamesInUse:
        print(f"Duplicate event for {coro.__name__} found. Please find the duplicate event and remove it. Not doing so will cause one of the events to no longer function correctly.")
    else:
        EventNamesInUse += [coro.__name__]
    return oldevent(self, coro)

discord.Client.event = newevent

intents = discord.Intents.all()
client = discord.Client(intents=intents)

plugins = []


os.chdir(os.path.dirname(__file__) or '.')

for folder in [x[0] for x in os.walk(os.getcwd())]:
    sys.path.insert(0, folder)


async def LoadPlugins():
    global plugins
    pluginLibs = []
    print("Loading plugins")
    for folder in [x[0] for x in os.walk(os.getcwd())]:
            files = os.listdir(folder)
            for filename in files:
                if filename.endswith(".py") and filename.startswith("plugin-"):
                    pluginLibs += [__import__(filename.split(".")[0])]

    for lib in pluginLibs:
        try:
            plugins += [lib.GetPlugin()]
        except:
            print(f"Could not get plugin class of {lib.__name__}")
    
    for plugin in plugins:
        try:
            if inspect.iscoroutinefunction(plugin.OnLoad):
                await plugin.OnLoad()
            else:
                plugin.OnLoad()
        except:
            print(f"Something went wrong while loading plugin {plugin.name} ({plugin.version})")

@client.event
async def on_ready():
    await LoadPlugins()
token = ""
try:
    with open("token", "r") as file:
        token = file.read().strip()
except:
    print("Could not read discord token.")
    sys.exit()

try:
    client.run(token)
except discord.errors.LoginFailure:
    print("Improper token on startup.")

import plugins