# Stock-Tracker-Discord-Bot

## Introduction
This Discord bot provides information about US stock market prices and related data. It supports commands to get stock information, current prices, historical data, and stock graphs.

## Features
- **Stock Information:** Retrieve detailed information about a specific stock.
- **Stock Price:** Get the current price of a stock.
- **Stock History:** Fetch historical data for a stock over the last 5 days.
- **Stock Graph:** Display a graph of a stock's closing prices over the last 5 days.

## Commands
- `!stock_info SYMBOL`: Get detailed information about a stock.
- `!stock_price SYMBOL`: Get the current price of a stock.
- `!stock_history SYMBOL`: Get historical data for a stock.
- `!stock_graph SYMBOL`: Display a graph of a stock's closing prices.

## Setup

### Prerequisites
- Python 3.x
- Required Python packages: `discord`, `discord_slash` (or any other library for Discord interactions), `yfinance`, `matplotlib`

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Shauryainks/stock-tracker-discord-bot.git
   cd discord-stock-bot
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Obtain a Discord bot token:

Create a new bot on the Discord Developer Portal.
Copy the bot token.
Configure the bot:

Open project.py in a text editor.
Replace 'YOUR_DISCORD_BOT_TOKEN' with the actual bot token.
Run the bot:

bash
Copy code
python project.py
Usage
Invite the bot to your Discord server using the provided invite link.
Use the commands mentioned in the "Commands" section to interact with the bot.
Contributing
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request.

License
This project is licensed under the MIT License.
