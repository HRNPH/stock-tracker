import nextcord
from price_checker import check_price

client = nextcord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
    if message.content.startswith('$pc'):
        msg = message.content.split(' ')
        if len(msg) == 4:
            await message.channel.send('On my way!')
            result = (check_price([msg[1]],msg[2],msg[3]))
            await message.channel.send(result)
        else:
            await message.channel.send('Please enter the target price and the stock ticker.')
        print(msg)

client.run('TOKENS')