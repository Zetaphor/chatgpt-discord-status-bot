import discord
import requests
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize the Discord client
client = discord.Client()

# URL of the webpage to check
url = "https://chat.openai.com/chat"

# String to search for
string_to_search = "ChatGPT is at capacity right now"

# ID of the channel to send messages to
channel_id = "1234567890"

# Variable to keep track of whether the string was previously found
string_previously_found = False

@client.event
async def on_ready():
    print("Bot is ready.")

    # Check the webpage every 30 seconds
    while True:
        try:
            # Make a GET request to the webpage
            response = requests.get(url)

            if response.status_code != 200:
                raise ValueError("Request returned a non-200 status code: {}".format(response.status_code))

            # Check if the string is present in the page
            string_found = string_to_search in response.text

            if string_found:
                if not string_previously_found:
                    # Send a message to the channel
                    channel = client.get_channel(channel_id)
                    await channel.send("ChatGPT appears to be down!")

                string_previously_found = True
            else:
                if string_previously_found:
                    # Send a message to the channel
                    channel = client.get_channel(channel_id)
                    await channel.send("ChatGPT appears to be back online!")

                string_previously_found = False
        except Exception as e:
            # Send a message to the channel with the error
            channel = client.get_channel(channel_id)
            await channel.send("An error occurred while checking the webpage: {}".format(str(e)))
        finally:
            # Wait 30 seconds before checking the webpage again
            await asyncio.sleep(30)

# Load the Discord bot token from the .env file
token = os.getenv("DISCORD_TOKEN")
client.run(token)
