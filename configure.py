import urllib.parse as urlparse
import os 

config = {
    "TOKEN": "TOKEN"
}

DATABASE_URL = "DATABASE_URL"
url = urlparse.urlparse(os.environ['DATABASE_URL'])

dbname = url.path[1:]
user = url.username
password = url.password
host = url.hostname
port = url.port
