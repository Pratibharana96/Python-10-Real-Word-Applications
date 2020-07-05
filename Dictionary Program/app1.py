import json

data = json.load(open("data.json"))
# print(data)
def translate(word):
    #2. Here we nee to convert the word in lowercase
    word= word.lower()
    #3. Now we suggest a word to the user present in our dataset
    
    #1. here we checking If the word present in the data 
    if word in data:
        return data[word][1]
    else:
        return"sorry the word not found please double check it"
       

    

word= input("Enter word:")
print(translate(word))
