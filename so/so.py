import http.client, urllib.request, urllib.parse, urllib.error, base64, time

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

def parse_comments(filename):
    tagsComments = {}
    with open(filename) as f:
        lines = f.readlines()
        mode = 0
        count = 0

        for line in lines:
            if line == "" or line[0] == ",":
                continue
            if mode == 0:
                if line[0] != "<":
                    continue
                tags = line.replace("<", "")
                tags = tags.replace(">", ",")
                tags = tags.split(",")
                tags = tags[:len(tags)-1]
                tagsComments[count] = [tags]
                mode = 1
            else:
                if line == ",":
                    continue
                line = line.replace("\n", "")
                line = line.replace('"', '')
                for x in ['{', '}', '|', '/', '\\', '@', '#', '$', '_', '%', '*']:
                    line = line.replace(x, "")
                line = ''.join([i if ord(i) < 128 else ' ' for i in line])

                tagsComments[count].append(line)
                count += 1
                mode = 0
    #print(tagsComments)
    return tagsComments



def tag_target(db ,tagName):
    commentList = []
    for t in db:
        if tagName in db[t][0]:
            commentList.append(db[t][1])
    return commentList

def send_request(request_body):
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
        print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))


topics = ['excel', 'osx', 'haskell']
# 'jquery', 'css', 'android', 'sql', 'asp.net', 'c#', 'r', 'node.js', 
#topics = ['javascript', 'java', 'c++', 'php', 'ios', 'linux', 'ruby', 'python', 'parsing', 'forms', 'windows']

db= parse_comments("../tc.csv")

for topic in topics:
    cList = tag_target(db, topic)
    with open("topics/" + topic + ".txt", 'w') as f:
        for comment in cList:
                f.write(comment + "\n")
        print(cList)



# d=input()
#
# i = 0
# batchSize = 0
# batch = []
# for comment in cList:
#     if len(comment) > 200:
#         continue
#     if i > 100:
#         break
#     batch.append(comment)
#     batchSize += 1
#     if batchSize >= 10:
#         body = build_request_body(batch)
#         # print(batch)
#         # print(body)
#         # d = input()
#         send_request(body)
#         time.sleep(2)
#
#         batch = []
#         batchSize = 0
#         i += 1
