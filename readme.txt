Hello and welcome to the Discord Soundboard OSS Bot (working on the name)! 
This was created my MrOliverW (GitHub username) with help from Google Gemini and Chat GPT.

To make this bot work in your server:
Prerequisites: User must be able to run this code and edit 2 lines of code: The BOT_TOKEN - '' line and The VOICE_CHANNEL_ID = line. 

1. Go to https://discord.com/developers/applications/ and Create new applications
2. Tap the "Bot" button on the Settings tab and make sure the following are selected
"Presence Intent", "Server Members Intent", "Message Content Intent"
3. Tap "Reset Token" and copy/paste that private token (DO NOT SHARE THIS) in the soundBot.py file on the BOT_TOKEN = '' line.
4. Tap the "OAuth2" button on the Settings tab and under Scopes check "bot"
5. Select the desired bot permissions (it's a soundboard so you'll need ones related to playing sounds)
6. Copy the generated URL and the bottom and paste it into your brower
7. Add bot to desired server
8. In Discord, Enable "Developer Mode" in the advanced settings section.
9. Find the Channel you want the bot to be active in; right-click it; and tap "Copy Channel ID".
10.Paste the Channel ID in the soundBot.py file on the VOICE_CHANNEL_ID = line.
11. Run the bot and give it < a minute to connect to your server
12. type corresponding commands and have fun!

Note: You will need to disconnect the bot from your voice chat when you are done. This is still in early stages of developmet.
If you are interested in coributing to this open source project, it is welcomed. 

List of Commands you can type when the bot is enabled and in the right Voice Chat (you must type into the discord voice channel chat to get responses):
-KING OF THE HILL (yes I know there's a lot)...
hello
goodbye
chinese
bobby1
bobby2
bwaa1
bwaa2
bwaaah
dallas
thumping
dangit
pegleg
nonsense
no
weak
fired
myson
takeback
shutup
puffin
comeon
getaway
bwaa3
dontknow
fish
nosex
splitup
propane
impossible
mypurse
whathell
grownman
garfield
yes

-LEATHER BELT
leatherbelt
leather
4str
4strength
leather belt

-OTHER
edf
okily
okilydokily
okily dokily
ok
everyone fights
1 rule
Jean Rasczak
rasczak
cold one
coldone
over21
yougethigh
you get high
vincevaughn
vince vaughn
jean shorts
jeanshorts
jeans
gottakeemoffson
gotta take em off
ablelincoln
abe
nufu
now you fucked up
you fucked up
fuckedup
fuckup
fucked up
starvin
thatbrotha

Project Progress

Enabled Discord dev mode
Installed and configured FFmpeg
Installed required libraries
Set up environment variables
Configured bot for specific voice channel
Ensured proper scope and permissions
Corrected MP3 file paths
Fixed multiple response issue
Resolved syntax errors in soundboard file names
Next Steps

Enhance security
Deploy to a repository
Host the repository on AWS or set up files on AWS
Let me know if you'd like any of these points elaborated or if you have other questions!
