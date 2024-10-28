import discord
from discord import Intents
import socket
import requests
import os

def get_param(name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, f"{name}.txt")
    with open(file_path, "r") as file:
        return file.read().strip()

def get_token():
    return get_param("token")

def get_channel():
    return int(get_param("ipchannel"))

def get_local_ip():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(("8.8.8.8", 80))
            local_ip = s.getsockname()[0]
        finally:
            s.close()
        return local_ip

def get_public_ip():
    return requests.get("https://api.ipify.org").text

if __name__ == "__main__":
    client = discord.Client(intents = Intents.default())

    @client.event
    async def on_ready():
        print(f'{client.user} is running')
        channel = client.get_channel(get_channel())
        await channel.send(f"local:\t\t{get_local_ip()}\npublic:\t\t{get_public_ip()}")
        await client.close()

    client.run(get_token())
