from os import environ

# Telegram Account Api Id And Api Hash
API_ID = int(environ.get("API_ID", "25227969"))
API_HASH = environ.get("API_HASH", "d59f6e3de4671401515bd1d8e303329f")

# Your Main Bot Token 
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Owner ID For Broadcasting 
OWNER_ID = int(environ.get("OWNER_ID", "6108939375")) # Owner Id or Admin Id

# Give Your Force Subscribe Channel Id Below And Make Bot Admin With Full Right.
F_SUB = environ.get("F_SUB", "")

# Mongodb Database Uri For User Data Store 
MONGO_DB_URI = environ.get("MONGO_DB_URI", "mongodb+srv://mihaja5084:yeIh95RrMkRNZ3It@cluster0.6voc3fm.mongodb.net/?retryWrites=true&w=majority")

# Port To Run Web Application 
PORT = int(environ.get('PORT', 8080))
