import urllib.request
from config import Config
import json

cfg = Config(open('config.cfg'))
a = 0

key = cfg.ytapi


name = "PewDiePie"
data = urllib.request.urlopen(
        "https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=" + name + "&key=" + key).read()
subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
p = "{:,d}".format(int(subs))
p = p.replace(',', '')
p = int(p)

name = "Tseries"
data = urllib.request.urlopen(
        "https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=" + name + "&key=" + key).read()
subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
t = "{:,d}".format(int(subs))
t = t.replace(',', '')
t = int(t)


b = a
a = p - t

