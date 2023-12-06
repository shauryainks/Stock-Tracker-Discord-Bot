import discord
from discord.ext import commands
import yfinance as yf
import matplotlib.pyplot as plt
from io import BytesIO

intents = discord.Intents.default()
intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

# Function to get stock information
def get_stock_info(symbol):
    stock = yf.Ticker(symbol)
    info = stock.info
    return info

# Function to get stock price
def get_stock_price(symbol):
    stock = yf.Ticker(symbol)
    price = stock.history(period='1d')['Close'][-1]
    return price

# Function to get stock history
def get_stock_history(symbol):
    stock = yf.Ticker(symbol)
    history = stock.history(period='5d')
    return history

# Function to plot stock graph
def plot_stock_graph(symbol):
    stock = yf.Ticker(symbol)
    history = stock.history(period='5d')
    plt.plot(history.index, history['Close'])
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.title(f'{symbol} Stock Price')
    image_stream = BytesIO()
    plt.savefig(image_stream, format='png')
    plt.close()
    image_stream.seek(0)
    return image_stream

@bot.command()
async def stock_info(ctx, symbol: str):
    info = get_stock_info(symbol)
    await ctx.send(f"**{symbol} Stock Information:**\n```{info}```")

@bot.command()
async def stock_price(ctx, symbol: str):
    price = get_stock_price(symbol)
    await ctx.send(f"**{symbol} Current Price:**\n${price:.2f}")

@bot.command()
async def stock_history(ctx, symbol: str):
    history = get_stock_history(symbol)
    await ctx.send(f"**{symbol} Stock History:**\n```{history}```")

@bot.command()
async def stock_graph(ctx, symbol: str):
    image_stream = plot_stock_graph(symbol)
    file = discord.File(image_stream, filename=f"{symbol}_graph.png")
    await ctx.send(f"**{symbol} Stock Graph:**", file=file)


# Run the bot
bot.run('bot_token')
