from datetime import datetime
from itertools import dropwhile, takewhile
import instaloader

L = instaloader.Instaloader()

posts = instaloader.Profile.from_username(L.context, "instagram")

SINCE = datetime(2021, 5, 12)
UNTIL = datetime(2022, 6, 20)

for post in takewhile(lambda p: p.date > UNTIL, dropwhile(lambda p: p.date > SINCE, posts)):
    print(post.date)
    L.download_post(post, "instagram")