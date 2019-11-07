# bot.py
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import random
import json
import aiohttp
import asyncio
import youtube_dl
from datetime import *
import praw
import pickle
import time
import math
import copy
from pokeballs import *
from typechart import *

# gets pre-cached move data
cache_path = 'move_cache'
dbfile = open(cache_path, 'rb')
move_cache = pickle.load(dbfile)
dbfile.close()

# gets bot token from .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    bot.add_cog(Battle(bot))
    battle_init = bot.get_cog('Battle')
    for guild in bot.guilds:
        battle_init.add_guild(guild.id)  # creates a new battle instance for each server upon start
        print(
            f'{bot.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )
        if guild.name == GUILD:
            break

@bot.command(name='99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        'Cool. Cool cool cool cool cool cool cool, no doubt no doubt no doubt no doubt.'
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

@bot.command(name='bitcoin')
async def bitcoin(ctx):
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await ctx.send("Bitcoin price is: $" + response['bpi']['USD']['rate'])

@bot.command(name='B',
                description="SPAMS THE 🅱️ EMOJI",
                brief="🅱️rief",
                aliases=['B_Emoji', '🅱️', '🅱️_Emoji'])
async def B(ctx):
    await ctx.send('🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️' +
                   '🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️' +
                   '🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️' +
                   '🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️' +
                   '🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️🅱️')

@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int = 1, number_of_sides: int = 6):
    dice = [str(random.choice(range(1, number_of_sides + 1))) for _ in range(number_of_dice)]
    await ctx.send(', '.join(dice))

@bot.command(pass_context=True)
async def brandon(ctx):
    await ctx.send('...Nah')

@bot.command(pass_context=True)
async def deez_nuts(ctx):
    await ctx.send('DEEZ NUTS!')

@bot.command(pass_context=True)
async def creeper(ctx):
    lyrics = ['Aw', 'man', 'So', 'we', 'back', 'in', 'the', 'mine', 'Got', 'our', 'pickaxe', 'swinging',
              'from', 'side', 'to', 'side', 'Side', 'side', 'to', 'side', 'This', 'task', 'a', 'grueling', 'one',
              'Hope', 'to', 'find', 'some', 'diamonds', 'tonight', 'night', 'night', 'Diamonds', 'tonight', 'Heads',
              'up', 'You', 'hear', 'a', 'sound', 'turn', 'around', 'and', 'look', 'up', 'Total', 'shock', 'fills',
              'your', 'body', 'Oh', 'no', 'it', 's', 'you', 'again', 'I', 'can', 'never', 'forget', 'those', 'eyes',
              'eyes', 'eyes', 'Eyes', 'eye', 'eyes', 'Cause', 'baby', 'tonight', 'The', 'creeper', 's', 'tryna',
              'steal', 'all', 'our', 'stuff', 'again', 'Cause', 'baby', 'tonight', 'You', 'grab', 'your', 'pick',
              'shovel', 'and', 'bolt', 'again', 'Bolt', 'again', 'gain', 'And', 'run', 'run', 'until', 'it', 's',
              'done', 'done', 'Until', 'the', 'sun', 'comes', 'up', 'in', 'the', 'morn', 'Cause', 'baby', 'tonight',
              'The', 'creeper', 's', 'tryna', 'steal', 'all', 'our', 'stuff', 'again', 'Stuff', 'again', 'gain', 'Just',
              'when', 'you', 'think', 'you', 're', 'safe', 'Overhear', 'some', 'hissing', 'from', 'right', 'behind',
              'Right', 'right', 'behind', 'That', 's', 'a', 'nice', 'life', 'you', 'have', 'Shame', 'it', 's', 'gotta',
              'end', 'at', 'this', 'time', 'time', 'time', 'Time', 'time', 'time', 'time', 'Blows', 'up', 'Then',
              'your', 'health', 'bar', 'drops', 'and', 'you', 'could', 'use', 'a', 'one', 'up', 'Get', 'inside', 'don',
              't', 'be', 'tardy', 'So', 'now', 'you', 're', 'stuck', 'in', 'there', 'Half', 'a', 'heart', 'is', 'left',
              'but', 'don', 't', 'die', 'die', 'die', 'Die', 'die', 'die', 'Cause', 'baby', 'tonight', 'The', 'creeper',
              's', 'tryna', 'steal', 'all', 'our', 'stuff', 'again', 'Cause', 'baby', 'tonight', 'You', 'grab', 'your',
              'pick', 'shovel', 'and', 'bolt', 'again', 'Bolt', 'again', 'gain', 'And', 'run', 'run', 'until', 'it',
              's', 'done', 'done', 'Until', 'the', 'sun', 'comes', 'up', 'in', 'the', 'morn', 'Cause', 'baby',
              'tonight', 'The', 'creeper', 's', 'tryna', 'steal', 'all', 'our', 'stuff', 'again', 'Creepers', 'you',
              're', 'mine', 'haha', 'Dig', 'up', 'diamonds', 'and', 'craft', 'those', 'diamonds', 'And', 'make', 'some',
              'armor', 'get', 'it', 'baby', 'Go', 'and', 'forge', 'that', 'like', 'you', 'so', 'MLG', 'pro', 'The',
              'sword', 's', 'made', 'of', 'diamonds', 'so', 'come', 'at', 'me', 'bro', 'huh', 'Training', 'in', 'your',
              'room', 'under', 'the', 'torchlight', 'Hone', 'that', 'form', 'to', 'get', 'you', 'ready', 'for', 'the',
              'big', 'fight', 'Every', 'single', 'day', 'and', 'the', 'whole', 'night', 'Creeper', 's', 'out',
              'prowlin', 'hoo', 'alright', 'Look', 'at', 'me', 'look', 'at', 'you', 'Take', 'my', 'revenge', 'that',
              's', 'what', 'I', 'm', 'gonna', 'do', 'I', 'm', 'a', 'warrior', 'baby', 'what', 'else', 'is', 'new',
              'And', 'my', 'blade', 's', 'gonna', 'tear', 'through', 'you', 'bring', 'it', 'Cause', 'baby', 'tonight',
              'The', 'creeper', 's', 'tryna', 'steal', 'all', 'our', 'stuff', 'again', 'Gather', 'your', 'stuff',
              'yeah', 'let', 's', 'take', 'back', 'the', 'world', 'Yeah', 'baby', 'tonight', 'Haha', 'Grab', 'your',
              'sword', 'armor', 'and', 'go', 'It', 's', 'on', 'Take', 'your', 'revenge', 'Woo', 'oh', 'oh', 'oh', 'oh',
              'So', 'fight', 'fight', 'like', 'it', 's', 'the', 'last', 'last', 'night', 'Of', 'your', 'life', 'life',
              'show', 'them', 'your', 'bite', 'Woo', 'Cause', 'baby', 'tonight', 'The', 'creeper', 's', 'tryna',
              'steal', 'all', 'our', 'stuff', 'again', 'Cause', 'baby', 'tonight', 'You', 'grab', 'your', 'pick',
              'shovel', 'and', 'bolt', 'again', 'Bolt', 'again', 'gain', 'woo', 'And', 'run', 'run', 'until', 'it', 's',
              'done', 'done', 'Until', 'the', 'sun', 'comes', 'up', 'in', 'the', 'morn', 'Cause', 'baby', 'tonight',
              'Come', 'on', 'swing', 'your', 'sword', 'up', 'high', 'The', 'creeper', 's', 'tryna', 'steal', 'all',
              'our', 'stuff', 'again', 'Come', 'on', 'jab', 'your', 'sword', 'down', 'low', 'Woo']

    # the commented out blocks are supposed to stream 'Revenge' by Captain Sparkles in the Discord voice channels but
    # Youtube compatability was recently lowkey removed from Discord bots so I commented it out so the bot doesn't
    # connect to voice channels everytime this command is called

    '''
    voice_channel = ctx.author.voice
    if voice_channel != None:
        if voice_channel != None:
            # create StreamPlayer
            voice_channel = ctx.author.voice.channel
            vc = await voice_channel.connect()

            song_there = os.path.isfile("song.mp3")
            try:
                if song_there:
                    os.remove("song.mp3")
            except PermissionError:
                await ctx.send("Wait for the current playing music end or use the 'stop' command")
                return

            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download(['https://www.youtube.com/watch?v=NeI-1Aq5CJw'])
            for file in os.listdir("./"):
                if file.endswith(".mp3"):
                    os.rename(file, 'song.mp3')

            vc.play(discord.FFmpegPCMAudio("song.mp3"))
    '''
    
    # sends the next lyric from 'lyrics' every 0.25 seconds
    for word in lyrics:
        await ctx.send(word)
        time.sleep(0.25)

    '''
    server = ctx.message.guild.voice_client
    if server:
        await server.disconnect()
    '''


@bot.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

@bot.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.guild.voice_client
    await server.disconnect()

@bot.command(description='Plays some stuff')
async def play(ctx, *content):
    
    ### So this bot worked when I implemented it, but now doesn't work anymore due to Youtube cracking down on Discord bots.
    ### If I had the time, I would try to implement queues and stuff but I can't really work on Youtube player now
    ### because all Discord bots don't work with Youtube :(
    
    # grab the user who sent the command
    user = ctx.message.author
    voice_channel = ctx.author.voice
    channel = None

    # only play music if user is in a voice channel
    if voice_channel!= None:
        # grab user's voice channel
        voice_channel = ctx.author.voice.channel
        channel = voice_channel.name
        await ctx.send('User is in channel: '+ channel)
        await ctx.send(voice_channel)

        # create StreamPlayer
        vc = await voice_channel.connect()

        if str(content).find("https://www.youtube.com") == -1:
            new_string = ('+'.join(content)).lower()
            await ctx.send(new_string)
            api_url1, api_url2 = 'https://www.googleapis.com/youtube/v3/search?part=snippet&order=relevance&q=', '&type=video&videoCategoryId=10&key=' + os.getenv('YOUTUBE_API_KEY')
            api_url = api_url1 + new_string + api_url2
            async with aiohttp.ClientSession() as session:  # Async HTTP request
                raw_response = await session.get(api_url)
                response = await raw_response.text()
                response = json.loads(response)
                await ctx.send(response["items"][0]["id"]["videoId"])
                song_id = response["items"][0]["id"]["videoId"]
                url = "https://www.youtube.com/watch?v=" + song_id
                if url == None:
                    await ctx.send("Song not found")
                    return
        else:
            url = str(content)

        song_there = os.path.isfile("song.mp3")
        try:
            if song_there:
                os.remove("song.mp3")
        except PermissionError:
            await ctx.send("Wait for the current playing music end or use the 'stop' command")
            return

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, 'song.mp3')

        vc.play(discord.FFmpegPCMAudio("song.mp3"))
        while vc.is_playing():
            await asyncio.sleep(1)

        # disconnect after the player has finished
        server = ctx.message.guild.voice_client
        await server.disconnect()
    else:
        await ctx.send('User is not in a channel.')

#gets Reddit API keys from .env file
reddit = praw.Reddit(client_id=os.getenv('REDDIT_CLIENT_ID'),
                     client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
                     user_agent=os.getenv('REDDIT_USER_AGENT'))

@bot.command()
async def okbuddy(ctx):
    memes_submissions = reddit.subreddit('okbuddyretard').hot()
    post_to_pick = random.randint(1, 12)  # chooses a random post to pick

    # finds specified non-stickied post
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied) # gets posts

    await ctx.send(submission.url)


@bot.command(name = 'Reddit', aliases=['reddit', 'reddit_posts'])
async def reddit_posts(ctx, sub: str = 'all', number: int = 3):
    assert number < 11, await ctx.send('Choose less posts!')
    submissions = reddit.subreddit(sub).hot()  # gets posts
    # sends specified number of posts
    for i in range(0, number):
        submission = next(x for x in submissions if not x.stickied)
        await ctx.send(submission.url)

@bot.command(name = 'go_bears', aliases=['bears'])
async def GO_BEARS(ctx):
    sent = [0, 1, 2, 'GO BEARS!']
    for word in sent:
        time.sleep(1)
        await ctx.send(word)


@bot.command(name = 'denero', aliases=['john, john_denero, John_Denero, John, Denero'])
async def denero(ctx):
    await ctx.send('https://i.ytimg.com/vi/AaWzN16M3LY/maxresdefault.jpg')
    await ctx.send('A N N O U N C E M E N T S')

@bot.command()
async def say(ctx, *speech):
    sent = (' '.join(speech))
    await ctx.send(sent)

#POKEMON COMMANDS!

class Pokemon():
    iv_spread = [31, 31, 31, 31, 31, 31]  # default IVs were 100 for testing
    nature = None  # may be implemented later
    type1 = None
    type2 = None
    damaging_moves = []

    def __init__(self, info, species, id, level: int = 75):
        self.id = id
        self.api_info = info  # gets pokemon info from api

        # sprite, species, level
        self.sprite = self.api_info["sprites"]["front_default"]
        self.species = species
        self.level = level

        # sets typing
        if len(self.api_info["types"]) == 1:
            self.type1 = self.api_info["types"][0]["type"]["name"]
        else:
            self.type1 = self.api_info["types"][0]["type"]["name"]
            self.type2 = self.api_info["types"][1]["type"]["name"]

        self.get_moves()  # retrieves current valid moves based on level
        self.moveset = {}
        # chooses four most recently-learned moves by level, or less if less moves are valid
        total_moves = 4 if len(self.damaging_moves) >= 4 else len(self.damaging_moves)
        for move_number in range(total_moves):
            self.moveset[move_number + 1] = self.damaging_moves[-move_number]

        # randomizes IVs
        self.iv_spread = [random.choice(range(0, 32)) for _ in range(6)]

        #sets base stats
        self.base_hp = self.api_info["stats"][5]["base_stat"]
        self.base_atk = self.api_info["stats"][4]["base_stat"]
        self.base_df = self.api_info["stats"][3]["base_stat"]
        self.base_satk = self.api_info["stats"][2]["base_stat"]
        self.base_sdf = self.api_info["stats"][1]["base_stat"]
        self.base_spd = self.api_info["stats"][0]["base_stat"]

        self.calculate_stats()  # calculates current stats based on base stats

    def calculate_stats(self):
        # stats calculated using main game formulas with level, IVs, and base stats (no EVs or nature yet)
        self.hp = math.floor((2 * self.base_hp + self.iv_spread[5]) * self.level / 100 + self.level + 10)
        self.atk = math.floor(math.floor((2 * self.base_atk + self.iv_spread[4]) * self.level / 100 + 5) * 1)
        self.df = math.floor(math.floor((2 * self.base_df + self.iv_spread[3]) * self.level / 100 + 5) * 1)
        self.satk = math.floor(math.floor((2 * self.base_satk + self.iv_spread[2]) * self.level / 100 + 5) * 1)
        self.sdf = math.floor(math.floor((2 * self.base_sdf + self.iv_spread[1]) * self.level / 100 + 5) * 1)
        self.spd = math.floor(math.floor((2 * self.base_spd + self.iv_spread[0]) * self.level / 100 + 5) * 1)

    def get_moves(self):
        # gets moves
        valid_moves = []
        damaging_moves = []

        # gets all moves learned by level up which within Pokemon's level
        for move in self.api_info["moves"]:
            learn_details = move["version_group_details"][-1]
            if learn_details["level_learned_at"] <= self.level and learn_details["move_learn_method"][
                "name"] == "level-up":
                valid_moves += [move]
        self.valid_moves = valid_moves

        # gets all level up moves which do damage
        for move in valid_moves:
            move_name = move["move"]["name"]
            move_data = move_cache[move_name]
            damage_type = (move_data["damage_class"]["name"] == "special" or move_data["damage_class"][
                "name"] == "physical") and move_data["power"]
            if damage_type:
                damaging_moves += [move_name]
        self.damaging_moves = damaging_moves


@bot.command(name = 'pokemon_inventory', aliases = ['pokemon_inv', 'inventory'],
             help = 'displays amount of pokeballs')
async def pokemon_inventory(ctx):
    user_path = 'users/' + str(ctx.message.author.id)
    inventory_path = user_path + '/inventory'
    assert os.path.exists(user_path) and os.path.exists(inventory_path), await ctx.send(
        'Your inventory is empty! Get more Pokeballs with !draw_balls')

    #loads inventory
    dbfile = open(inventory_path, 'rb')
    dict = pickle.load(dbfile)
    dbfile.close()

    #displays inventory
    str1 = 'You have a total of: ' + str(dict['pokeball']) + ' Pokeballs, ' + str(dict['greatball']) + ' Greatballs, ' \
           + str(dict['ultraball']) + ' Ultraballs, and ' + str(dict['masterball']) + ' Masterballs.'
    str2 = 'The last time you drew for pokeballs was: ' + dict['last_draw']

    await ctx.send(str1)
    await ctx.send(str2)


@bot.command(name = 'pokemon_list', aliases = ['list', 'list_pokemon', 'my_pokemon'],
             help = 'lists your pokemon')
async def pokemon_list(ctx):
    path = 'users/' + str(ctx.message.author.id) + '/pokemon'
    assert os.path.exists(path), await ctx.send(
        'You have no Pokemon! Get more pokemon with !pokeball [pokeball]')

    embed = discord.Embed(title="Your Pokemon:", color=0x00ff00)

    for name in range(1, 101):  # checks all numbers from 1 - 100
        pokemon_path = 'users/' + str(ctx.message.author.id) + '/pokemon/' + str(name)  # gets Pokemon based off number
        if os.path.exists(pokemon_path):  # only proceeds if Pokemon exists
            # gets Pokemon from file
            dbfile = open(pokemon_path, 'rb')
            pokemon = pickle.load(dbfile)
            dbfile.close()
            # adds Pokemon info to embed
            species, level, id = pokemon.species, pokemon.level, pokemon.id
            string = species[0].upper() + species[1:] + ', level ' + str(level) + ' [ID: ' + str(id) + ']'
            embed.add_field(name = string, value='\u200b', inline=False)

    await ctx.send(embed = embed)


@bot.command(name = 'pokemon_inspect', aliases = ['inspect', 'pokemon_check', 'check'],
             help = 'inspect a Pokemon with its [ID]')
async def pokemon_inspect(ctx, poke_number: int):
    path = 'users/' + str(ctx.message.author.id) + '/pokemon'
    assert os.path.exists(path), await ctx.send(
        'You have no Pokemon! Get more pokemon with !pokeball [pokeball]')

    pokemon_path = 'users/' + str(ctx.message.author.id) + '/pokemon/' + str(poke_number)
    assert os.path.exists(pokemon_path), await ctx.send(
        'Pokemon not found')

    # opens Pokemon file
    dbfile = open(pokemon_path, 'rb')
    pokemon = pickle.load(dbfile)
    dbfile.close()

    # gets species, level, type
    species_level = pokemon.species.capitalize() + ' [Lv. ' + str(pokemon.level) + ']'
    type = pokemon.type1.capitalize() if not pokemon.type2 else pokemon.type1.capitalize() + ', ' + pokemon.type2.capitalize()

    # gets moves
    move_list_str = ''
    for move_number in range(len(pokemon.moveset.keys())):
        move_list_str += pokemon.moveset[move_number + 1].capitalize() + '\n'
    move_list_str += '\u200b'

    # gets stats
    hp = 'HP: ' + str(pokemon.hp)
    atk = 'Attack: ' + str(pokemon.atk)
    df = 'Defense: ' + str(pokemon.df)
    satk = 'Special Attack: ' + str(pokemon.satk)
    sdf = 'Special Defense: ' + str(pokemon.sdf)
    spd = 'Speed: ' + str(pokemon.spd)

    stats_str = hp + '\n' + atk + '\n' + df + '\n' + satk + '\n' + sdf + '\n' + spd

    embed = discord.Embed(title=species_level, color=0x00ff00)
    embed.add_field(name='Type: ' + type, value='\u200b', inline=False)
    embed.add_field(name='Moves:', value=move_list_str, inline=False)
    embed.add_field(name='Stats:', value=stats_str, inline=False)

    await ctx.send(pokemon.sprite)
    await ctx.send(embed = embed)

@bot.command(name = 'pokemon_release', aliases = ['release', 'Release'],
             help = 'release a Pokemon with its [ID]')
async def pokemon_release(ctx, poke_number: int):
    path = 'users/' + str(ctx.message.author.id) + '/pokemon'
    assert os.path.exists(path), await ctx.send(
        'You have no Pokemon! Get more pokemon with !pokeball [pokeball]')

    pokemon_path = 'users/' + str(ctx.message.author.id) + '/pokemon/' + str(poke_number)
    assert os.path.exists(pokemon_path), await ctx.send(
        'Pokemon not found')

    # makes sure Pokemon isn't in team
    team_path = 'users/' + str(ctx.message.author.id) + '/team'
    if os.path.exists(team_path):
        dbfile = open(team_path, 'rb')
        team = pickle.load(dbfile)
        dbfile.close()
        assert poke_number not in team.values(), await ctx.send('Cannot release a Pokemon in your team!')

    # deletes Pokemon file
    os.remove(pokemon_path)
    await ctx.send('Pokemon released')

async def team_lister(ctx, team):
    embed = discord.Embed(title="Your Team:", color=0x00ff00)
    # gets every Pokemon in team
    for number in range(len(team.keys())):
        pokemon_path = 'users/' + str(ctx.message.author.id) + '/pokemon/' + str(team[number + 1])

        # opens Pokemon file
        dbfile = open(pokemon_path, 'rb')
        pokemon = pickle.load(dbfile)
        dbfile.close()

        # displays Pokemon info
        species, level, id = pokemon.species, pokemon.level, pokemon.id
        string = 'Slot ' + str(number + 1) + ': ' + species[0].upper() + species[1:] + ', level ' + str(
            level) + ' [ID: ' + str(id) + ']'
        embed.add_field(name=string, value='\u200b', inline=False)

    await ctx.send(embed=embed)

@bot.command(name = 'team_list', help = 'lists out your Pokemon battling team')
async def team_list(ctx):
    pokelist_path = 'users/' + str(ctx.message.author.id) + '/pokemon'
    assert os.path.exists(pokelist_path), await ctx.send(
        'You have no Pokemon! Get more pokemon with !pokeball [pokeball]')

    team_path = 'users/' + str(ctx.message.author.id) + '/team'
    assert os.path.exists(team_path), await ctx.send(
        'You have no team! Add Pokemon to your team with !add')

    # opens team file
    dbfile = open(team_path, 'rb')
    team = pickle.load(dbfile)
    dbfile.close()

    await team_lister(ctx, team)  # lists team info

def create_team(path):
    dict = {}
    dbfile = open(path, 'ab')
    # source, destination
    pickle.dump(dict, dbfile)
    dbfile.close()

@bot.command(name = 'team_add', aliases = ['add', 'Add'], help = 'adds a Pokemon to your battle team with [ID]')
async def team_add(ctx, poke_number: int):
    pokelist_path = 'users/' + str(ctx.message.author.id) + '/pokemon'
    assert os.path.exists(pokelist_path), await ctx.send(
        'You have no Pokemon! Get more pokemon with !pokeball [pokeball]')

    team_path = 'users/' + str(ctx.message.author.id) + '/team'
    if not os.path.exists(team_path):
        create_team(team_path)  # creates team file if none exists

    # open team file
    dbfile = open(team_path, 'rb')
    team = pickle.load(dbfile)
    dbfile.close()
    assert len(team.keys()) < 6, await ctx.send(
        'You already have 6 Pokemon! Remove one with !team_remove')

    pokemon_path = 'users/' + str(ctx.message.author.id) + '/pokemon/' + str(poke_number)
    assert os.path.exists(pokemon_path), await ctx.send(
        'Pokemon not found')

    assert poke_number not in team.values(), await ctx.send(
        'Pokemon already in party')

    # modifies team file by adding Pokemon to team
    team[len(team.keys()) + 1] = poke_number
    os.remove(team_path)
    dbfile = open(team_path, 'ab')
    # source, destination
    pickle.dump(team, dbfile)
    dbfile.close()

    await team_lister(ctx, team)  # lists team info

@bot.command(name = 'team_remove', help = 'remove [slot number] Pokemon from your battling team')
async def team_remove(ctx, team_number: int):
    pokelist_path = 'users/' + str(ctx.message.author.id) + '/pokemon'
    assert os.path.exists(pokelist_path), await ctx.send(
        'You have no Pokemon! Get more pokemon with !pokeball [pokeball]')

    team_path = 'users/' + str(ctx.message.author.id) + '/team'
    assert os.path.exists(team_path), await ctx.send(
        'You have no team! Add Pokemon to your team with !add')

    # open team file
    dbfile = open(team_path, 'rb')
    team = pickle.load(dbfile)
    dbfile.close()
    assert len(team.keys()) > 1, await ctx.send(
        'You cannot remove your last Pokemon')

    assert team_number in team.keys(), await ctx.send(
        'There is no Pokemon in that team slot')

    # modifies team file by removing Pokemon
    for number in range(team_number, len(team.keys())):
        team[number] = team[number + 1]
    del team[len(team.keys())]
    os.remove(team_path)
    dbfile = open(team_path, 'ab')
    # source, destination
    pickle.dump(team, dbfile)
    dbfile.close()

    await team_lister(ctx, team)  # lists team info

@bot.command(name = 'team_replace',
             help = 'replace [slot number] Pokemon in your battling team with [ID] pokemon')
async def team_replace(ctx, team_number: int, poke_number:int):
    pokelist_path = 'users/' + str(ctx.message.author.id) + '/pokemon'
    assert os.path.exists(pokelist_path), await ctx.send(
        'You have no Pokemon! Get more pokemon with !pokeball [pokeball]')

    team_path = 'users/' + str(ctx.message.author.id) + '/team'
    assert os.path.exists(team_path), await ctx.send(
        'You have no team! Add Pokemon to your team with !add')

    # opens team file
    dbfile = open(team_path, 'rb')
    team = pickle.load(dbfile)
    dbfile.close()

    pokemon_path = 'users/' + str(ctx.message.author.id) + '/pokemon/' + str(poke_number)
    assert os.path.exists(pokemon_path), await ctx.send(
        'Pokemon not found')

    assert team_number in team.keys(), await ctx.send(
        'There is no Pokemon in that team slot')

    # finds associated Pokemon ID and does replacement
    if poke_number in team.values():
        for key, id in team.items():
            if id == poke_number:
                poke_key = key
                break
        team[poke_key] = team[team_number]
    team[team_number] = poke_number
    # modifies team file
    os.remove(team_path)
    dbfile = open(team_path, 'ab')
    # source, destination
    pickle.dump(team, dbfile)
    dbfile.close()

    await team_lister(ctx, team)  # lists team info


@bot.command(name = 'pokemon_drawballs', aliases = ('draw', 'drawballs', 'draw_balls', 'pokemon_draw'),
             help='get 10 random pokeballs per day (limit disabled for testing)')
async def draw_balls(ctx):
    user_path = 'users/' + str(ctx.message.author.id)
    inventory_path = user_path + '/inventory'

    # makes inventory if inventory doesn't exist
    if not os.path.exists(user_path):
        os.makedirs(user_path)

    if not os.path.exists(inventory_path):
        dict = {'last_draw': 'never', 'pokeball': 0, 'greatball': 0, 'ultraball': 0, 'masterball': 0, 'rare_candy': 0}
        dbfile = open(inventory_path, 'ab')
        # source, destination
        pickle.dump(dict, dbfile)
        dbfile.close()

    # loads inventory file
    dbfile = open(inventory_path, 'rb')
    dict = pickle.load(dbfile)
    dbfile.close()

    today = date.today()
    # dd/mm/YY
    today_date = str(today.strftime("%d/%m/%Y"))
    #assert dict['last_draw'] != today_date, await ctx.send('Already drew today, wait for tomorrow')
    # above line implemets the daily draw limit. Currently disabled for testing.

    # randomly draws 10 balls
    pokeballs, greatballs, ultraballs, masterballs = 0,0,0,0
    for _ in range(0, 10):
        rarity_roll = random.choice(range(1, 101))
        if rarity_roll in range(1, 51):
            dict['pokeball'] += 1
            pokeballs += 1
        elif rarity_roll in range(51, 81):
            dict['greatball'] += 1
            greatballs += 1
        elif rarity_roll in range(81, 96):
            dict['ultraball'] += 1
            ultraballs += 1
        else:
            dict['masterball'] += 1
            masterballs += 1

    dict['last_draw'] = today_date  # logs last draw date for daily draw limit

    # modifies inventory file
    os.remove(inventory_path)
    dbfile = open(inventory_path, 'ab')
    # source, destination
    pickle.dump(dict, dbfile)
    dbfile.close()

    # lists balls recieved and total inventory
    str1 = 'You recieved: ' + str(pokeballs) + ' Pokeballs, ' + str(greatballs) + ' Greatballs, ' + str(ultraballs) \
           + ' Ultraballs, and ' + str(masterballs) + ' Masterballs.'
    str2 = 'You have a total of: ' + str(dict['pokeball']) + ' Pokeballs, ' + str(dict['greatball']) + ' Greatballs, ' \
           + str(dict['ultraball']) + ' Ultraballs, and ' + str(dict['masterball']) + ' Masterballs.'

    await ctx.send(str1)
    await ctx.send(str2)


@bot.command(name = 'Pokeball', aliases = ['catch', 'throw', 'ball', 'pokeball', 'pokemon_catch', 'pokemon_pokeball'],
             help = 'throw a [pokeball] to catch a Pokemon')
async def pokeball(ctx, ball):
    #finds possible pokeballs
    balls = {'pokeball': poke, 'greatball': great, 'ultraball': ultra, 'masterball': master}  # gets pokeball functions
    ball = ball.lower()
    assert ball in balls.keys(), await ctx.send('Choose a ball from:')

    user_path = 'users/' + str(ctx.message.author.id)
    inventory_path = user_path + '/inventory'
    assert os.path.exists(user_path) and os.path.exists(inventory_path), await ctx.send('You must first draw using !draw_balls')

    # loads inventory file
    dbfile = open(inventory_path, 'rb')
    dict = pickle.load(dbfile)
    dbfile.close()
    assert dict[ball], await ctx.send('Need more ' + ball + 's!')

    # creates path to save pokemon
    path = 'users/' + str(ctx.message.author.id) + '/pokemon'
    if not os.path.exists(path):
        os.makedirs(path)
    list = os.listdir(path)  # dir is your directory path
    number_files = len(list)
    assert number_files < 100, await ctx.send(
        'You cannot have over 100 Pokemon. Release some with !release')

    # modifies inventory file by removing respective Pokeball
    dict[ball] -= 1
    os.remove(inventory_path)
    dbfile = open(inventory_path, 'ab')
    # source, destination
    pickle.dump(dict, dbfile)
    dbfile.close()

    # rolls for a pokemon
    pokemon_roll, rarity_name = balls[ball]()

    api_url = 'https://pokeapi.co/api/v2/pokemon/' + pokemon_roll

    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(api_url)
        response = await raw_response.text()
        response = json.loads(response)

    number = 1
    while True:
        pokemon_path = 'users/' + str(ctx.message.author.id) + '/pokemon/' + str(number)
        if not os.path.exists(pokemon_path):
            break
        number += 1
    pokemon_creator = Pokemon(response, pokemon_roll, number)  # creates new instance for Pokemon
    dbfile = open(pokemon_path, 'ab')

    # source, destination
    pickle.dump(pokemon_creator, dbfile)
    dbfile.close()

    dbfile = open(pokemon_path, 'rb')
    db = pickle.load(dbfile)
    pic_url = db.sprite
    dbfile.close()

    # sends picture and Pokemon
    await ctx.send(pic_url)
    await ctx.send('You got ' + rarity_name + ' Pokemon: ' + pokemon_roll)

    string = 'You have a total of: ' + str(dict['pokeball']) + ' Pokeballs, ' + str(dict['greatball']) + ' Greatballs, ' \
           + str(dict['ultraball']) + ' Ultraballs, and ' + str(dict['masterball']) + ' Masterballs left'
    await ctx.send(string)


### BATTLING ###

class Battle(commands.Cog):
    guild_dict = {}

    def __init__(self, bot):
        self.bot = bot

    def add_guild(self, id):
        self.guild_dict[id] = GuildBattle(self.bot)

    def create(self):
        self.check = True

    def remove(self, ctx):
        self.add_guild(ctx.guild.id)

    @commands.command(name='challenge', aliases=['Challenge'], help = 'initialize a battle challenge')
    async def challenge(self, ctx):
        if ctx.guild.id not in self.guild_dict.keys():
            self.add_guild(ctx.guild.id)  # creates new instance if guild instance isn't already created
        await self.guild_dict[ctx.guild.id].guild_challenge(ctx)

    @commands.command(name='accept', aliases=['Accept'], help = 'accept a battle challenge')
    async def accept(self, ctx):
        await self.guild_dict[ctx.guild.id].guild_accept(ctx)

    @commands.command(name='end', aliases=['End', 'end_battle'], help = 'end a battle you are in')
    async def end(self, ctx):
        await self.guild_dict[ctx.guild.id].guild_end(ctx)

    @commands.command(name='attack', aliases=['Attack'], help = 'attack the defending Pokemon with [move number]')
    async def attack(self, ctx, move_number: int):
        await self.guild_dict[ctx.guild.id].guild_attack(ctx, move_number)

    @commands.command(name='choose', aliases=['Choose'], help = 'choose a new Pokemon to send out with [slot number]')
    async def choose(self, ctx, slot: int):
        await self.guild_dict[ctx.guild.id].guild_choose(ctx, slot)


class GuildBattle(Battle):
    player1 = None
    player2 = None
    check = False
    turn_phase = 0
    choosing = False


    def create_players(self):
        self.player_instance_1 = Player(self.player1)
        self.player_instance_2 = Player(self.player2)

    async def start_game(self, ctx):
        self.create_players()
        self.p1_poke = self.player_instance_1.team[0]
        self.p2_poke = self.player_instance_2.team[0]
        self.attacker = self.p1_poke if self.p1_poke.pokemon.spd > self.p2_poke.pokemon.spd else self.p2_poke
        self.defender = self.p2_poke if self.p1_poke.pokemon.spd > self.p2_poke.pokemon.spd else self.p1_poke
        self.turn_phase = 1
        self.active_player = self.attacker.owner
        await self.game_state(ctx)

    async def next_turn(self, ctx):
        if self.defender.fainted:
            if len(self.defender.owner.team) == 0:
                await self.finish(ctx, self.attacker.owner.player)
                return
            else:
                self.choosing = self.defender.owner
                await self.show_team(ctx)
                return
        elif not self.turn_phase:
            if self.defender.pokemon.spd > self.attacker.pokemon.spd:
                self.attacker, self.defender = self.defender, self.attacker
            self.turn_phase = 1
        else:
            self.attacker, self.defender = self.defender, self.attacker
            self.turn_phase = 0
        self.active_player = self.attacker.owner
        await self.game_state(ctx)

    async def game_state(self, ctx):
        attacker_pokemon = self.attacker.pokemon
        defender_pokemon = self.defender.pokemon

        d_species_level = defender_pokemon.species.capitalize() + ' [Lv. ' + str(defender_pokemon.level) + ']'
        d_hp = 'HP: ' + str(defender_pokemon.hp)

        a_species_level = attacker_pokemon.species.capitalize() + ' [Lv. ' + str(attacker_pokemon.level) + ']'
        a_hp = 'HP: ' + str(attacker_pokemon.hp)

        move_list_str = ''
        for move_number in range(len(attacker_pokemon.moveset.keys())):
            move_list_str += str(move_number + 1) + '. ' + attacker_pokemon.moveset[move_number + 1].capitalize() + '\n'
        move_list_str += 'Attack with !attack [move number]'

        str1 = d_species_level + '\n' + d_hp
        str2 = a_species_level + '\n' + a_hp

        embed = discord.Embed(title='Game State:', color=0x00ff00)
        embed.add_field(name='Defender: ' + str(self.defender.owner.player), value=str1, inline=False)
        embed.add_field(name='Attacker: ' + str(self.attacker.owner.player), value=str2, inline=False)
        embed.add_field(name='Moves:', value=move_list_str, inline=False)

        await ctx.send(embed=embed)

    async def show_team(self, ctx):
        embed = discord.Embed(title="Choose from:", color=0x00ff00)
        for number in range(len(self.choosing.team)):
            pokemon = self.choosing.team[number]

            species, level, id = pokemon.pokemon.species, pokemon.pokemon.level, pokemon.pokemon.id
            string = 'Slot ' + str(number + 1) + ': ' + species[0].upper() + species[1:] + ', level ' + str(level) + ' [ID: ' + str(id) + ']'
            embed.add_field(name=string, value='\u200b', inline=False)
        embed.add_field(name='Choose a new Pokemon to send out using !choose [slot number]', value='\u200b', inline=False)

        await ctx.send(embed=embed)

    async def finish(self, ctx, winner):
        await ctx.send('The winner is: ' + str(winner))
        self.remove(ctx)


    async def guild_challenge(self, ctx):
        assert not self.check, await ctx.send('Battle currently happening. If a challenge has been posed, accept it with !accept')
        team_path = 'users/' + str(ctx.message.author.id) + '/team'
        assert os.path.exists(team_path), await ctx.send(
            'You have no team! Add Pokemon to your team with !add')
        self.create()
        print(self)

        self.player1 = ctx.message.author

        await ctx.send('Battle started, accept ' + str(self.player1) + '\'s challenge with !accept')


    async def guild_accept(self, ctx):
        assert self.check, await ctx.send('No battle started. Start a battle with !challenge')
        assert ctx.message.author != self.player1, await ctx.send('You can\'t accept your own challenge!')
        assert not self.player2, await ctx.send('Challenge already accepted!')
        team_path = 'users/' + str(ctx.message.author.id) + '/team'
        assert os.path.exists(team_path), await ctx.send(
            'You have no team! Add Pokemon to your team with !add')

        self.player2 = ctx.message.author

        await ctx.send('Challenge accepted by ' + str(self.player2))

        await self.start_game(ctx)


    async def guild_end(self, ctx):
        assert self.check and self.player2, await ctx.send('No battle started. Start a battle with !challenge')
        assert ctx.message.author == self.player1 or ctx.message.author == self.player2, await ctx.send('Only battlers can end battles')

        self.remove(ctx)

        await ctx.send('Battle ended by ' + str(ctx.message.author))


    async def guild_attack(self, ctx, move_number):
        assert self.check and self.player2, await ctx.send('No battle started. Start a battle with !challenge')
        assert not self.choosing, await ctx.send('A Pokemon must be chosen with !choose first')
        assert ctx.message.author == self.active_player.player, await ctx.send('It\'s not your turn')
        assert self.attacker.check_moves(move_number), await ctx.send('Move number not found in moveset')

        damage, remaining_hp, modifier = self.attacker.attack(self.defender, move_number)
        str1 = 'Dealt ' + str(damage) + ' damage. '
        if modifier > 1.2:
            str2 = 'Super effective! '
        elif modifier < 1:
            str2 = 'Not very effective... '
        else:
            str2 = ''
        str3 = 'Remaining HP: ' + str(remaining_hp)
        await ctx.send(str1 + str2 + str3)
        await self.next_turn(ctx)


    async def guild_choose(self, ctx, slot):
        assert self.check and self.player2, await ctx.send('No battle started. Start a battle with !challenge')
        assert self.choosing and ctx.message.author == self.choosing.player, await ctx.send('You can\'t choose Pokemon yet')
        assert self.choosing.check_slots(slot), await ctx.send('Team slot not found')

        self.choosing.send(slot)
        self.defender = self.choosing.active_pokemon
        self.turn_phase = 0
        self.choosing = None
        await self.next_turn(ctx)


class BattlePokemon():
    hp = 0
    spd = 0
    fainted = False

    def __init__(self, owner, pokemon):
        self.pokemon = copy.copy(pokemon)
        self.owner = owner

    def attack(self, target, move_number):
        move = self.pokemon.moveset[move_number]
        move_data = move_cache[move]
        move_type = move_data["type"]["name"]
        power, damage_class = move_data["power"], move_data["damage_class"]["name"]
        stab = 1.2 if move_type == self.pokemon.type1 or move_type == self.pokemon.type2 else 1
        modifier = 1 * type_chart[move_type].get(target.pokemon.type1, 1) * type_chart[move_type].get(target.pokemon.type2, 1) * stab

        if damage_class == 'physical':
            damage = math.floor(modifier * (((((2 * self.pokemon.level/5 + 2) * self.pokemon.atk * power)/target.pokemon.df)/50)+2))
        else:
            damage = math.floor(modifier * (
                        ((((2 * self.pokemon.level / 5 + 2) * self.pokemon.satk * power) / target.pokemon.sdf) / 50) + 2))

        remaining_hp = target.take_damage(damage)
        return damage, remaining_hp, modifier

    def take_damage(self, damage):
        self.pokemon.hp -= damage
        if self.pokemon.hp <= 0:
            self.owner.faint(self)
        return self.pokemon.hp

    def check_moves(self, move_number):
        if move_number in self.pokemon.moveset.keys():
            return True
        return False

class Player():
    team = []
    active_pokemon = None

    def __init__(self, player):
        self.team = self.team[:]
        self.player = player
        team_path = 'users/' + str(player.id) + '/team'
        dbfile = open(team_path, 'rb')
        self.team_dict = pickle.load(dbfile)
        dbfile.close()

        for _ in range(len(self.team_dict.keys())):
            pokemon_path = 'users/' + str(player.id) + '/pokemon/' + str(self.team_dict[_ + 1])
            dbfile = open(pokemon_path, 'rb')
            pokemon = pickle.load(dbfile)
            dbfile.close()
            self.team += [BattlePokemon(self, pokemon)]

    def send(self, slot):
        self.active_pokemon = self.team[slot-1]

    def faint(self, pokemon):
        self.team = [poke for poke in self.team if poke is not pokemon]
        pokemon.fainted = True

    def check_slots(self, slot):
        if slot - 1 in range(len(self.team)):
            return True
        return False


bot.run(TOKEN)