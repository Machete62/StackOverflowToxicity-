import http.client, urllib.request, urllib.parse, urllib.error, base64, time, random

def build_request_body(comments):
    body = '{ "documents": ['
    count = 0
    for comment in comments:
        body += """
        {
          "language": "en",
          "id": """
        body += str(count) + ", "
        count += 1
        body+= '"text": ' + '"' + comment + '"'
        body += "}"
        if count-1 != len(comments) - 1:
            body += ","
    body += "]}"
    return body


def send_request(request_body, outFileName):
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': '432c3b6e55954af2a1c8d2ede461773a',
    }
    params = urllib.parse.urlencode("")

    try:
        conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/text/analytics/v2.0/sentiment?%s" % params, request_body , headers)
        response = conn.getresponse()
        data = response.read()
        with open(outFileName, 'a') as f:
            f.write(str(data) + "\n")
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

def getComments(filename):
    filename = filename + ".txt"
    comments = []

    with open(filename) as f:
        for line in f.readlines():
            if len(line) > 300 or len(line) < 75:
                continue
            comments.append(line)

        count = 0
        while count < 100:
            comment = random.choice(comments)
            comments.append(comment)
            count+=1
    return comments


subreddits = ['gonewild', 'atheism', 'nfl', 'cringe', 'hiphopheads', 'anime', 'apple', 'Android', 'dataisbeautiful', 'funny']

#subreddits = ['gaming', 'AskReddit', 'videos', 'GlobalOffensive', 'learnprogramming', 'askscience', 'trees', '4chan']

#['The_Donald', 'news', 'Fitness', 'WTF' ]
#['buildapc', 'ShitRedditSays', 'ImGoingToHellForThis', 'politics', 'aww', 'leagueoflegends', 'EarthPorn']

for subName in subreddits:
    cList = getComments(subName)
    print(subName)

    i = 0
    batchSize = 0
    batch = []
    for comment in cList:
        if len(comment) > 200:
            continue
        if i > 100:
            break
        batch.append(comment)
        batchSize += 1
        if batchSize >= 10:
            body = build_request_body(batch)
            send_request(body, subName + "_results.txt")
            time.sleep(2)

            batch = []
            batchSize = 0
            i += 1
