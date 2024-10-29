import discord
from discord import Intents
import socket
import requests
import os
from datetime import datetime

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
        
        time = datetime.now().strftime("%b %d %I:%M %p")
        pub_ip = get_public_ip()
        local_ip = get_local_ip()

        await channel.send(
            f">>> **Local IP:**\t  {local_ip}\n"\
            f"**Public IP:**\t{pub_ip}\n"
        )
        
        await client.close()

    client.run(get_token())

