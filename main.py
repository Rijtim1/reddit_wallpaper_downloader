import praw

CLIENT_ID = 'P6lZCiD8Bf4KAQ'
CLIENT_SECRET = 'LAMc1VLORXN1_pDjO6nekKmdH1k'
PASSWORD = "Sujana0512"
USER_AGENT = "praw"
USERNAME = "nipple_cripp"

reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                     username=USERNAME, password=PASSWORD, user_agent=USER_AGENT)


subreddit = reddit.subreddit('wallpaper')
hot_wallpaper = subreddit.hot()

for hot in hot_wallpaper:
    print("Title: {} \nUps: {} \nDowns: {} \nURL: {}".format(
        hot.title, hot.ups, hot.downs, hot.url))
