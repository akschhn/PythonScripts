import os
import urllib2
import json

apiKey = <Insert Wordnik Api Key>
def getRandomWord():
	getRandomWordUrl = "http://api.wordnik.com/v4/words.json/randomWord?api_key=" + apiKey
	wordsResult = urllib2.urlopen(getRandomWordUrl).read()
	json_data = json.loads(wordsResult)
	return json_data['word']

def getWordInfo(word):
	pre = "http://api.wordnik.com/v4/word.json/"
	dyn = word + "/definitions?"
	url = pre + dyn + "api_key="+ apiKey
	wordsResult = urllib2.urlopen(url).read()
	json_data = json.loads(wordsResult)
	return json_data

def showNotification():
   word = getRandomWord()
   info = getWordInfo(word)

   definition = info[0]['text']
   pos = info[0]['partOfSpeech']

   # os.system("""osascript -e 'display notification "{0}" with title "{1}" '"""
   # 	.format("Part of Speech - "+ pos + "\n" +"Meaning :"+definition, word, "Part of Speech :"+ pos))

   os.system(""" osascript -e 'display dialog "{0}" with title "{1}" buttons "{2}" '"""
   	.format("Word : "+ word + "\n" + "Part of Speech : "+ pos + "\n" +"Meaning : "+definition, "Word of the day ", "Close"))

showNotification()
