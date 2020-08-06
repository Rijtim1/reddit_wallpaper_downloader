import os
import shutil
import praw
import requests

CLIENT_ID = ''
CLIENT_SECRET = ''
PASSWORD = ""
USER_AGENT = ""
USERNAME = ""

reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                     username=USERNAME, password=PASSWORD, user_agent=USER_AGENT)

subreddit = reddit.subreddit('wallpaper')
hot_wallpaper = subreddit.top("all")
url_list = []

for hot in hot_wallpaper:
    name_url = (hot.title, hot.url)
    url_list.append(name_url)

count = 1
image_name = []

for i in range(len(url_list)):
    response = requests.get(url_list[i][1], stream=True)
    file_name = "images_" + str(count) + ".jpg"
    image_name.append(file_name)
    try:
        file = open(file_name, "wb")
        file.write(response.content)
        file.close()
    except Exception as e:
        print(e)
        print("Exception happened, but was caught")
    count += 1

try:
    os.mkdir("images")
except Exception as e:
    print(e)
    pass

for images in image_name:
    destination = "images/{}".format(images)
    shutil.move("{}".format(images), destination)
