# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "12648223")

API_HASH = os.environ.get("API_HASH", "3b4e63ca2584c8294cb5f6b5216e2cf0")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6930488421:AAFV5Xn51jSeYt_9wTylplrYmThk_MmX974") 

FORCE_SUB = os.environ.get("FORCE_SUB", "find_hub") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "renamerender24")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://Erichdaniken:Erichdaniken@cluster0.q7rhi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5606411877').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
