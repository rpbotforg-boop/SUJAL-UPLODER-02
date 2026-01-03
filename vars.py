#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "22447622"))
API_HASH = int(environ.get("API_HASH", "543b62d58d3e723e766ba57a984ab65d"))

BOT_TOKEN = int(environ.get("BOT_TOKEN", "8225118430:AAEOFTRcVH3Au1LR0iFyasUb4U5CGATuoT4"))
OWNER = int(environ.get("OWNER", "777756062"))
CREDIT = "Ravindra"

AUTH_USER = os.environ.get('AUTH_USERS', '777756062').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))

# ➕ MongoDB config (Render env se aayega)
MONGO_URI = environ.get("MONGO_URI", "mongodb+srv://niravpatel180503_db_user:vjWNaWhRk0gMSNyQ@cluster0.26bfgmf.mongodb.net/?appName=Cluster0")
DB_NAME = environ.get("DB_NAME", "DevThanos")
COLLECTION_NAME = environ.get("COLLECTION_NAME", "DevThanos")
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set






