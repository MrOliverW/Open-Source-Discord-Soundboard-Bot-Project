import discord
from discord.ext import commands
import asyncio

# Replace with your bot's token
BOT_TOKEN = '' 

# Replace with the actual ID of the voice channel you want the bot to join
VOICE_CHANNEL_ID = 

#Other Voice_Channel_ID's:
    #Example of Server 1 
        #7 Days to Die - 
        

    #Example of Server 2 
        #Age of Wonders - 


# Dictionary to map phrases to sound file paths
soundboard_mapping = {
    #King of The Hill
    'hello': 'soundboards\hey-peg-leg-101soundboards.mp3',
    'goodbye': 'soundboards\Voicy_May Be We Should Split Up.mp3',
    'bobby1': 'soundboards/bobby-101soundboards (1).mp3',
    'bobby2': 'soundboards/bobby-101soundboards.mp3',
    'bwaa1': 'soundboards/bwaaah-101soundboards (1).mp3',
    'bwaa2': 'soundboards/bwaaah-101soundboards (2).mp3',
    'bwaaah': 'soundboards/bwaaah-101soundboards.mp3',
    'dallas': 'soundboards/dallas-101soundboards.mp3',
    'thumping': 'soundboards/damn-it-there-it-is-again-where-is-that-thumping-coming-from-101soundboards.mp3',
    'dangit': 'soundboards\dang-it-bobby---king-of-the-hill-made-with-Voicemod.mp3',
    'pegleg': 'soundboards/hey-peg-leg-101soundboards.mp3',
    'nonsense': 'soundboards\ive-had-enough-of-this-nonsense-101soundboards.mp3',
    'no': 'soundboards/no-101soundboards.mp3',
    'weak': 'soundboards\youre-calling-me-weak-101soundboards.mp3',
    'fired': "soundboards\youre-fired-101soundboards.mp3",
    'myson': "soundboards/youre-my-son-101soundboards.mp3",
    'takeback': "soundboards\you-take-that-back-101soundboards.mp3",
    'shutup': 'soundboards\shut-the-hell-up-101soundboards.mp3',
    'puffin': 'soundboards/start-puffin-boy-hank-hill.mp3',
    'comeon': "soundboards\Voicy_Come On Baby Don't Be That Way.mp3", 
    'getaway': 'soundboards\Voicy_Get Away From Me.mp3',
    'bwaa3': 'soundboards\Voicy_hank hill bwaaa.mp3',
    'dontknow': "soundboards\Voicy_I Don't Know You.mp3", 
    'fish': "soundboards\Voicy_If You Want To Catch A Fish You Have To Think Like Fish.mp3",
    'nosex': "soundboards\Voicy_I'm Never Gonna Have Sex.mp3",
    'splitup': "soundboards\Voicy_May Be We Should Split Up.mp3", 
    'propane': 'soundboards\Voicy_Propane Accessories.mp3',
    'impossible': 'soundboards\Voicy_That Is Impossible.mp3',
    'mypurse': "soundboards\Voicy_That's My Purse.mp3", 
    'whathell': 'soundboards\Voicy_What The Hell Is That_.mp3',
    'grownman': "soundboards\Voicy_You Can't Treat A Grown Man Like A Baby.mp3",
    'garfield': "soundboards\Voicy_You ever heard of Garfield_.mp3",
    'yes':"soundboards\yes-101soundboards.mp3",

    #Leather Belt :)
    'leatherbelt': 'soundboards/ventrilo-harassment-world-of-warcraft-nerd-mp3cut.mp3',
    'leather': 'soundboards/ventrilo-harassment-world-of-warcraft-nerd-mp3cut.mp3',
    '4str': 'soundboards/ventrilo-harassment-world-of-warcraft-nerd-mp3cut.mp3',
    '4strength': 'soundboards/ventrilo-harassment-world-of-warcraft-nerd-mp3cut.mp3',
    'leather belt': 'soundboards/ventrilo-harassment-world-of-warcraft-nerd-mp3cut.mp3',
    
    #EDF
    'edf': "soundboards/the-edf-deploys-made-with-Voicemod.mp3",

        #Simpsons
    'okily': "soundboards\okily-dokily-from-youtube-mp3cut.mp3",
    'okilydokily': "soundboards\okily-dokily-from-youtube-mp3cut.mp3",
    'okily dokily': "soundboards\okily-dokily-from-youtube-mp3cut.mp3",
    'ok': "soundboards\okily-dokily-from-youtube-mp3cut.mp3",

    #Starship Troopers
    'everyone fights': "soundboards\Everyone Fights LOUD Soundboard.mp3",
    '1 rule': "soundboards\Everyone Fights Best SoundBoard.mp3",
    'Jean rasczak':"soundboards\Everyone Fights Best SoundBoard.mp3",
    'rasczak':"soundboards\Everyone Fights LOUD Soundboard.mp3",

    #Other
        #The Internship
    'cold one':"soundboards\ill have a cold one with you the internship.mp3",
    'coldone':"soundboards\ill have a cold one with you the internship.mp3",
    'over21':"soundboards\ill have a cold one with you the internship.mp3",
    'yougethigh':"soundboards\ill have a cold one with you the internship.mp3",
    'you get high?':"soundboards\ill have a cold one with you the internship.mp3",
    'yougethigh?':"soundboards\ill have a cold one with you the internship.mp3",
    'vincevaughn':"soundboards\ill have a cold one with you the internship.mp3",
    'vince vaughn':"soundboards\ill have a cold one with you the internship.mp3",

        #It's Always Sunny
    'jean shorts':"soundboards\Jean Shorts Remastered.mp3",
    'Jeanshorts':"soundboards\Jean Shorts Remastered.mp3",
    'jeans':"soundboards\Jean Shorts Remastered.mp3",  
    'gottatakeemoffson':"soundboards\Jean Shorts Remastered.mp3",
    'gotta take em off':"soundboards\Jean Shorts Remastered.mp3",

        #WKYK
    'abelincoln':"soundboards/Now you Fucked Up.mp3",
    'abe':"soundboards/Now you Fucked Up.mp3",
    'nufu':"soundboards/Now you Fucked Up.mp3",
    'now you fucked up':"soundboards/Now you Fucked Up.mp3",
    'you fucked up':"soundboards/Now you Fucked Up.mp3",
    'fuckedup':"soundboards/Now you Fucked Up.mp3",
    'fuckup':"soundboards/Now you Fucked Up.mp3",
    'fucked up':"soundboards/Now you Fucked Up.mp3",

}

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Flag to track if the "not connected" message has been sent
not_connected_message_sent = False

# Flag to indicate if the bot is ready to play sounds
voice_ready = False

@bot.event
async def on_ready():
    global voice_ready
    print(f'Logged in as {bot.user.name}')

    channel = bot.get_channel(VOICE_CHANNEL_ID)
    if channel and isinstance(channel, discord.VoiceChannel):
        retry_delay = 1  # Initial retry delay in seconds
        while not voice_ready: 
            try:
                voice_client = await channel.connect()
                print(f'Connected to voice channel: {channel.name}')
                voice_ready = True
                retry_delay = 1  # Reset delay on successful connection
            except discord.errors.ClientException as e:
                print(f'Error connecting to voice: {e}. Retrying in {retry_delay} seconds...')
                await asyncio.sleep(retry_delay)
                retry_delay *= 2  # Double the delay for the next attempt (exponential backoff)
                if retry_delay > 60:  # Cap the maximum delay to avoid excessive wait times
                    retry_delay = 60
    else:
        print(f'Could not find voice channel with ID {VOICE_CHANNEL_ID}')

@bot.event
async def on_message(message):
    global not_connected_message_sent, voice_ready

    if message.content.lower() in soundboard_mapping:
        sound_file_path = soundboard_mapping[message.content.lower()]
        print(sound_file_path) # Print the file path for debugging

        user_voice_channel = message.author.voice.channel

        if bot.voice_clients and voice_ready:
            voice_client = bot.voice_clients[0]

            if user_voice_channel == voice_client.channel:
                try:
                    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(sound_file_path))
                    voice_client.play(source, after=lambda e: print(f'Player error: {e}') if e else None)
                except Exception as e:
                    print(f'Error playing sound: {e}')
            else:
                await message.channel.send("I'm not in your voice channel!")
        else:
            if not not_connected_message_sent: 
                await message.channel.send("I'm not connected to any voice channel!")
                not_connected_message_sent = True 

bot.run(BOT_TOKEN)