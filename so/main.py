import json
from watson_developer_cloud import ToneAnalyzerV3

import random


tone_analyzer = ToneAnalyzerV3(
   username= "1b5caa1e-ac1b-4ae3-9f36-e6d89e0933f5",
   password= "Iprz1kmpJkQj",
   version='2016-05-19 ')
#'css', 'android', 'sql', 'asp.net', 'c#', 'r', 'node.js', 
topics = ['excel', 'osx', 'haskell']
#['javascript', 'java', 'c++', 'php', 'ios', 'linux', 'ruby', 'python', 'parsing', 'forms', 'windows']
for topic in topics:
    with open("topics/" + topic + ".txt") as f:
        comments = []
        for line in f.readlines():
            if len(line) < 300:
                line = line.replace('\n', '')
                comments.append(line)
        #print(comments)
        with open("output/" + topic + ".txt" , 'w') as g:
            for i in range(0,80):
                comment = random.choice(comments)
                s = json.dumps(tone_analyzer.tone(text=comment))
                g.write(s)


#print(json.dumps(tone_analyzer.tone(text='A word is dead when it is said, some say. Emily Dickinson'), indent=2))
