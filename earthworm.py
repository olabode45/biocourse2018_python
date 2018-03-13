import string
import requests
from io import StringIO

url = 'https://raw.githubusercontent.com/pvanheus/biocourse2018_python/master/darwin_earthworms.txt'

def get_page(url):
    response = requests.get(url)
    if response:
        page = StringIO(response.text)
    else:
        page = StringIO('')
    return page

L_SQUOTE = "\u2018"
R_SQUOTE = "\u2019"
L_DQUOTE = "\u201C"
R_DQUOTE = "\u201D"
ACUTE = "\u00B4"
punctuation = string.punctuation[:-4]
punctuation = (punctuation + "|~" + L_SQUOTE + R_SQUOTE +
               L_DQUOTE + R_DQUOTE + ACUTE)
print(punctuation)
punctuation_set = set(punctuation)

def is_punctuation(char):
    if  len(char) == 1 and char in punctuation_set:
        return True
    else:
        return False
        
def is_word(mystring):
    mystring = mystring.strip(punctuation)
    if mystring == '':
        return False
    for character in mystring:
        if not character.isalnum() and not character == '-':
#         if not (character.isalnum() or character == '-'):
            return False
    # the loop has finished, everything is a letter or a number
    # or punctuation
    return True
    
page = get_page(url)
word_count = 0 # make a new basket called word_count and set to 0
for line in page:
    word_list = line.split() # split the line into a list of words and set word_list to this value
    new_word_count = len(word_list) + word_count # count the number of words in word_list and add to word_count
    word_count = new_word_count # store the new total word_count in word_count
print("words in book:", word_count) #  print the word count
