# Discord Webpage Monitor Bot

### **The code and README for this project were 100% written by ChatGPT**

This is a Discord bot that checks the status of the ChatGPT website. If the site is down it will send a message to a specific channel. If the site comes back up, it will send another message to the channel.

## How to use

1. Clone the repository to your local machine.

    ``git clone https://github.com/YOUR-USERNAME/Discord-Webpage-Monitor-Bot.git``

2. Create a new Discord bot and invite it to your server. [This guide](https://discordpy.readthedocs.io/en/latest/discord.html) provides step-by-step instructions on how to do this.

3. Create a new file named .env in the root directory of the cloned repository. This file should contain one line that specifies the Discord bot token, like so:

    ``DISCORD_TOKEN=YourToken``

Make sure to replace YourToken with your actual bot token.

4. Install the required dependencies by running

    ``pip install -r requirements.txt``

5. Modify the script by replacing the `channel_id` variable with the ID of the channel in your server where you want to send messages.

6. Run the script by executing the following command in the terminal

    ``python bot.py``

## Features

* The bot will check the webpage every 30 seconds and send a message to the specified channel if the specified string is found or not found.
* Error handling, if any error occurs in the process of requesting the webpage, it will send a message to the specified channel with the error.
* Uses the dotenv library to load the Discord bot token from a .env file, allowing you to keep your token secure and not hardcoded in the script.

**Please note that the extension and the example server are provided as-is and are intended for educational and informational purposes only. The author is not affiliated with OpenAI and claims no responsibility for any damages that may occur as a result of using the software. The software is provided under the MIT License.**

## Contributions

Feel free to fork this repository, improve the code and submit a pull request.

Please note that this is a simple example, it can be improved for a production setting. I recommend testing this script in a development environment before using it in production.