import json
# import dfflib for best match of the string and suggestion  
from difflib import get_close_matches 

data = json.load(open("data.json"))
# print(data)
def translate(word):
    #2. Here we nee to convert the word in lowercase
    word= word.lower()
    #1. here we checking If the word present in the data 
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys()))>0 :
        yn=  input("Did you mean %s instead ? Enter Y if or enter N if no " % get_close_matches(word,data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn== "N":
            return"sorry the word not found please double check it"
        else:
            return"sorry We did't understand your entry."
         
        

    else:
        return"sorry the word not found please double check it"
       

word= input("Enter word:")
# print(translate(word))
# 1. Now in output we need to remove list and ""
# 2. But here it iterate every string and list for remove that
output=translate(word) 
if type(output) == list:
    for opt in output:
        print(opt)
else:
    print(output)


