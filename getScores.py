import re


subreddits = ['gonewild', 'atheism', 'nfl', 'cringe', 'hiphopheads', 'anime', 'apple', 'Android', 'dataisbeautiful', 'funny']

#['gaming', 'AskReddit', 'videos', 'GlobalOffensive', 'learnprogramming', 'askscience', 'trees', '4chan']

#subreddits = ['The_Donald', 'news', 'Fitness', 'WTF' ]

#['buildapc', 'ShitRedditSays', 'ImGoingToHellForThis', 'politics', 'aww', 'leagueoflegends', 'EarthPorn']

def sr_score(srName):
    filename = srName+"_results.txt"
    ratings = []
    with open(filename) as f:
        for line in f.readlines():
            m = re.findall('"score":[0-9].[0-9]*', line)
            for r in m:
                ratings.append(r[8:])

    Ex = 0
    Ex2 = 0
    N = 0

    for r in ratings:
        Ex += float(r)
        Ex2 += float(r)*float(r)
        N+=1

    Ex /= N
    Ex2 /= N

    print(s, "mean = ", Ex, "var = ", Ex2 - Ex*Ex)

for s in subreddits:
    sr_score(s)
