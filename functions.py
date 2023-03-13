import urllib.parse, urllib.request, urllib.error, json
import pprint

#pick a word
params = 'hello'
baseurl = 'https://api.dictionaryapi.dev/api/v2/entries/en'
request = baseurl + "/" + params
#print(request)

#print response
f = urllib.request.urlopen(request)
response_str = f.read()
#print(response_str)

#clean up response, load to json
data = json.loads(response_str)
#pprint.pprint(data)

#extract relevant info
#print('word: ' + str(data[0]['word']))
#print('part of speech: ' + str(data[0]['meanings'][0]['partOfSpeech']))
#print('definition: ' + str(data[0]['meanings'][0]['definitions'][0]['definition']))

# function to get dict phrase
def get_dictionary_phrase(word, formatted=0):
    params = {'word': word, 'formatted': formatted}
    paramstr = urllib.parse.urlencode(params)
    baseurl = 'https://api.dictionaryapi.dev/api/v2/entries/en'
    request = baseurl + "/" + params['word']
    f = urllib.request.urlopen(request)
    return json.load(f)

#list with data from API call
pprint.pprint(get_dictionary_phrase(word='hello'))

# function to print definition
def write_definition(word):
    print(word + " (" + str(get_dictionary_phrase(word=word)[0]['meanings'][0]['partOfSpeech']) + ") " + str(get_dictionary_phrase(word=word)[0]['meanings'][0]['definitions'][0]['definition']))

#test code
write_definition('hello')
write_definition('brother')
write_definition('run')

# test if word exists
def write_definition_safe(word):
    try:
        write_definition(word)
    except urllib.error.HTTPError as e:
        print('Word does not exist. Please make sure your spelling is correct.')

#test for nonexistent words
write_definition_safe('bluj')

# pt 2.4
print('Search up a word and its definition:')
x = input()
write_definition_safe(x)