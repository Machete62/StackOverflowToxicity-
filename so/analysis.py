import json


jsons = []
topics = ['jquery', 'css', 'android', 'sql', 'asp.net', 'c#', 'r']
#topics = ['javascript', 'java', 'c++', 'php', 'ios', 'linux', 'ruby', 'python', 'parsing', 'forms', 'windows']

for name in topics:
    with open('output/' + name + ".txt") as f:
        s = str(f.readlines()[0])
        s = s.split("THISISAFUCKINGDELIMITER")
        for line in s:
            j = line.split("\n")
            for x in j:
                js = json.loads(x)
                jsons.append(js)

    toneMeans = {}
    N = 0
    for comment in jsons:
        N += 1
        #print(name,",", end='')

        toneCats = comment["document_tone"]["tone_categories"]
        for toneCat in toneCats:
            tones = toneCat["tones"]
            for tone in tones:
                score = tone["score"]
                toneName = tone["tone_name"]
                if toneName in toneMeans:
                    toneMeans[toneName] += score
                else:
                    toneMeans[toneName] = score
    print(name, ",",  end = '')
    tonestuff = ['Sadness', 'Openness', 'Conscientiousness',	'Fear',	'Joy', 'Emotional Range','Tentative',	'Extraversion',	'Anger',	'Agreeableness','Analytical' ,'Disgust',	'Confident']
    for k in tonestuff:
        print(toneMeans[k]/N, ",", end = '')
    print()
