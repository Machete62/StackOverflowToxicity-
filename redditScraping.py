import praw

reddit = praw.Reddit(user_agent='Comment Extraction (by /u/testmas/',
                     client_id='no0VyiHBNhUVsg', client_secret="p4LiaGDpWPshIUxtISIQ9Pre-bg",
                     username='testmas', password='burg45nap')


subreddits = ['gonewild', 'atheism', 'nfl', 'cringe', 'hiphopheads', 'anime', 'apple', 'Android', 'dataisbeautiful', 'funny']

#['gaming', 'AskReddit', 'videos', 'GlobalOffensive', 'learnprogramming', 'askscience', 'trees', '4chan']
#['The_Donald', 'news', 'Fitness', 'WTF' ]
# ['buildapc', 'pcmasterrace', 'ShitRedditSays', 'ImGoingToHellForThis', 'politics', 'aww', 'leagueoflegends', 'EarthPorn']

def scrape_sub(subName):
    links = []
    comments = []
    for submission in reddit.subreddit(subName).hot(limit=25):
        links.append(submission.shortlink)

    for link in links:
        submission = reddit.submission(url=link)
        submission.comments.replace_more(limit=0)
        comment_queue = submission.comments[:]  # Seed with top-level
        while comment_queue:
            comment = comment_queue.pop(0)
            comments.append(comment.body)
            comment_queue.extend(comment.replies)

    return comments

def all_subs():
    for sub in subreddits:
        cList = scrape_sub(sub)
        print("printing:", sub)

        with open(sub + ".txt" , 'w') as f:

            for comment in cList:
                comment = comment.replace("\n", '')
                comment = comment.replace('"', '')
                for x in ['{', '}', '|', '/', '\\', '@', '#', '$', '_', '%', '*', '+', '-', ';', ':', '&', '[', ']']:
                    commment = comment.replace(x, '')
                comment = ''.join([i if ord(i) < 128 else '' for i in comment])
                f.write(comment + "\n")
        print("print completed")

all_subs()
