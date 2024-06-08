import os, time

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "")
    API_HASH  = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
   
    # database config
    DB_NAME = os.environ.get("DB_NAME","")     
    DB_URL  = os.environ.get("DB_URL","")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "")
    ADMIN = int(os.environ.get("ADMIN", ""))

    # channels logs
    FORCE_SUB   = os.environ.get("FORCE_SUB", "") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002051680690"))

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))



class Txt(object):
    # part of text configuration
    START_TXT = """<b>🌼 Hᴇʟʟᴏ {} 👋

This Is An Advanced And Yet Powerful Rename Bot. 📚

Using This Bot You Can Rename And Change Thumbnail Of Your Files. 〽️

🌸 Tʀʏ Oᴜʀ Fɪʟᴍ Bᴏᴛ</b> ➜ <a href=https://t.me/TheSilvaFilmBOT><b>The Silva™ × Films 🇱🇰</b></a>

<blockquote><a href=https://t.me/DiniduSilva><b>Pʀɪᴍᴇ සිල්වා Pʀᴇᴍɪᴜᴍ Cʀᴇᴀᴛɪᴏɴ</b></a></blockquote>"""

    ABOUT_TXT = """
╭───────────────⍟
├<b>✯ My Name</b> : {}
├<b>✯ Developer</b> : <a href=https://t.me/DiniduSilva>Pʀɪᴍᴇ සිල්වා</a> 
├<b>✯ Library</b> : <a href=https://github.com/pyrogram>Pyrogram</a>
├<b>✯ Language</b> : <a href=https://www.python.org>Python 3</a>
├<b>✯ Database</b> : <a href=https://cloud.mongodb.com>Mongo DB</a>
├<b>✯ Build Version</b> : <a href=https://t.me/SilvaFilmZone>Rename v4.5.0</a></b>     
╰───────────────⍟

<blockquote><a href=https://t.me/DiniduSilva><b>Pʀɪᴍᴇ සිල්වා Pʀᴇᴍɪᴜᴍ Cʀᴇᴀᴛɪᴏɴ</b></a></blockquote>"""

    HELP_TXT = """
📖 <b><u>How To Set Thumbnail</u></b>
  
➪ /start - Start The Bot And Send Any Photo To Automatically Set Thumbnail.
➪ /del_thumb - Use This Command To Delete Your Old Thumbnail.
➪ /view_thumb - Use This Command To View Your Current Thumbnail.

📑 <b><u>How To Set Custom Caption</u></b>

➪ /set_caption - Use This Command To Set A Custom Caption
➪ /see_caption - Use This Command To View Your Custom Caption
➪ /del_caption - Use This Command To Delete Your Custom Caption

<b>⭕ Example -</b> 
<code>/set_caption 📕 Name ➠ : {filename}
📚 Size ➠ : {filesize} 
⏰ Duration ➠ : {duration}</code>

〽️ <b><u>How To Rename A File</u></b>

<b>➪ Send Any File And Type New File Name And Select The Format [ Document, Video, Audio ].</b>  

<blockquote><a href=https://t.me/DiniduSilva><b>Pʀɪᴍᴇ සිල්වා Pʀᴇᴍɪᴜᴍ Cʀᴇᴀᴛɪᴏɴ</b></a></blockquote>"""

    PROGRESS_BAR = """\n
<b>╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣</b>
<b>┣⪼ 🗃 Sɪᴢᴇ: <code>{1}|{2}</code></b>
<b>┣⪼ ⏳️ Dᴏɴᴇ : <code>{0}%</code></b>
<b>┣⪼ 🚀 Sᴩᴇᴇᴅ: <code>{3}/s</code></b>
<b>┣⪼ ⏰️ Eᴛᴀ : <code>{4}</code></b>
<b>╰━━━━❰ ᴘʀɪᴍᴇ ꜱɪʟᴠᴀ ❱━➣</b>
"""

    DONATE_TXT = """<b>Hey  there 👋</b>

<b>If You have Any problem ? Contact Owner On Telegram 🌼</b>

<b>Thankyou For Using Pʀɪᴍᴇ සිල්වා pʀᴇᴍɪᴜᴍ Cʀᴇᴀᴛɪᴏɴ Bᴏᴛᴢ 〽️</b>

<b>⭕ Contact Owner on Telegram</b> : <a href=https://t.me/DiniduSilva><b>Pʀɪᴍᴇ සිල්වා</b></a>

<blockquote><a href=https://t.me/DiniduSilva><b>Pʀɪᴍᴇ සිල්වා Pʀᴇᴍɪᴜᴍ Cʀᴇᴀᴛɪᴏɴ</b></a></blockquote>"""








# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @JishuBotz
# Developer @JishuDeveloper
