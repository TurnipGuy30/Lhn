import os
from discord import ClientUser
import nextcord
from nextcord.ext import commands
from dotenv import load_dotenv
from keep_alive import keep_alive

load_dotenv()
keep_alive()

version = "v0.1.3"
TOKEN = os.getenv('DISCORD_TOKEN')
description = ''
intents = nextcord.Intents.default()
intents.members = True
   
client = commands.Bot(command_prefix="lhn", description=description, intents=intents)

def e(t,d,r):
	nextcord.Embed(
		title=t,
		description=d,
		color=0x00FF00
	).set_author(
		name=f"Lh(n) {version}",
		icon_url="https://avatars.githubusercontent.com/u/83386810?v=4"
	).set_footer(
		text=f"This message was sent because {r}."
	)

@client.event
async def on_ready():
	print(f'Logged in as {client.user} (ID: {client.user.id})')
	await client.change_presence(activity=nextcord.Game(name=f'{version}'))

@client.event
async def on_member_join(ctx, guild, member: nextcord.Member):
	try:
		await member.dm_channel.send(embed=e(f'Hi, {member.name}!',f'Welcome to `{guild.name}`!','you joined a server with Lh(n) installed'))#.add_field(name="Reply to this message!", value="I am a WIP Chat Bot. See what I can do!", inline=False))
		print(f'Welcomed {member.name} to {guild.name}.')
	except:
		print(f'Could not welcome {member.name} to {guild.name}.')

@client.command()
async def on_message(message, ctx):
	if message.author != ClientUser:
		if ClientUser.mentioned_in(message):
			try:
				await message.author.create_dm()
				await ClientUser.message.author.send_message(message.author, f"Hi {message.author}, it's Lh(n) here!")
				await ctx.reply(f"@{message.author}, DM sent!")
			except:
				await ctx.reply(f"@{message.author}, your DMs are blocked!")
		elif isinstance(message.channel, nextcord.DMChannel):
			await client.message.author.send_message(message.author, f"Hi {message.author}, it's Lh(n) here!")
		await client.process_commands(message)

try:
	client.run(TOKEN)
except:
	print('Could not establish connection.')
