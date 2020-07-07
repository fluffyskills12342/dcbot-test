import discord
from discord.ext import commands
from discord import member, message, user

TOKEN = 'NzI5NDg2OTIzODE0NTM1MjYw.XwLiqw.Hs1_UE-E15h0Sh20MEs8aYI_MNE'

client = commands.Bot(command_prefix = 'f!')

@client.event
async def on_ready():
    print('Bot ist Bereit')

@client.command(pass_context=True)
async def clear(ctx, amount=10):

    channel = ctx.message.channel

    messages = []

    async for message in channel.history(limit=900000):
        messages.append(message)

    await channel.delete_messages(messages)
    await ctx.send(f'Es wurden {amount} Nachrichten gelöscht!     https://imgur.com/LIyGeCR')


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user, *, reason= None):
    user = discord.Member

    await member.kick(reason=reason)
    await ctx.send(f'User {member} wurde gekickt!')


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason=None):
  await user.ban(reason=reason)
  await ctx.send(f"{user} wurde erfolgreich gebannt!")


@client.command()
async def unban(ctx, *, member):
  banned_users = await ctx.guild.bans()
  member_name, member_discriminator = member.split('#')

  for ban_entry in banned_users:
    user = ban_entry.user
  
  if (user.name, user.discriminator) == (member_name, member_discriminator):
    await ctx.guild.unban(user)
    await ctx.send(f"{user} wurde erfolgreich entbannt!")
    return
    






client.run(TOKEN)