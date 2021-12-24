from re import template
from tkinter import font
import nltk
from nltk import probability
from nltk.stem import WordNetLemmatizer
from tensorflow.python.eager.context import context
from tensorflow.python.tf2 import disable
lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np
import time
import EPL

from keras.models import load_model
model = load_model('chatbot_model.h5')
import json
import random
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))

def clean_up_sentence(sentence):
    # tokenize the pattern - splitting words into array
    sentence_words = nltk.word_tokenize(sentence)
    # stemming every word - reducing to base form
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for words that exists in sentence
def bag_of_words(sentence, words, show_details=True):
    # tokenizing patterns
    sentence_words = clean_up_sentence(sentence)
    # bag of words - vocabulary matrix
    bag = [0] * len(words)
    for s in sentence_words:
        for i,word in enumerate(words):
            if word == s:
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print("found in bag: {}".format(word))
    return(np.array(bag))

def predict_class(sentence):
    # filter below threshold predictions
    p = bag_of_words(sentence, words, show_details=True)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    # sorting strength probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent":classes[r[0]], "probability": str(r[1])})
    print("return_list",return_list)
    return return_list

def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag']==tag):
            result = random.choice(i['responses'])
            break
    return result

# Creating tkinter GUI
import tkinter
from tkinter import *

def send():
    msg =  EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)

    if msg != '':
        ChatBox.config(state=NORMAL)
        ChatBox.insert(END, "You: " + msg + '\n\n')
        ChatBox.config(foreground="#000000", font=("Futura", 12))

        ints = predict_class(msg)
        tag_val = ints[0]['intent']
        response = getResponse(ints, intents)
        res = response
        
        ChatBox.insert(END, "Bot: " + res + '\n\n')
        ChatBox.config(state=DISABLED)
        ChatBox.yview(END)

        if tag_val == "jersey_number" or tag_val == "club_name" or tag_val == "position" or tag_val == "birth_day" \
                        or tag_val == "age" or tag_val == "height" or tag_val == "market_value" or tag_val == "citizenship"\
                        or tag_val == "national_team_caps" or tag_val == "weight":
            keyword = 'of '
            before, keyword, pl_name = msg.partition(keyword)
            if '?' in pl_name:
                pl_name = pl_name[:-1]
            if tag_val == "jersey_number":
                pl_info = EPL.player_info(pl_name,jn=True)
            elif tag_val == "club_name":
                pl_info = EPL.player_info(pl_name,cn=True)
            elif tag_val == "position":
                pl_info = EPL.player_info(pl_name,sp=True)
            elif tag_val == "birth_day":
                pl_info = EPL.player_info(pl_name,bd=True)
            elif tag_val == "age":
                pl_info = EPL.player_info(pl_name,age=True)
            elif tag_val == "height":
                pl_info = EPL.player_info(pl_name,height=True)
            elif tag_val == "market_value":
                pl_info = EPL.player_info(pl_name,mv=True)
            elif tag_val == "citizenship":
                pl_info = EPL.player_info(pl_name,citizenship=True)
            elif tag_val == "national_team_caps":
                pl_info = EPL.player_info(pl_name,ntc=True)
            elif tag_val == "weight":
                pl_info = EPL.player_info(pl_name,weight=True)

            tag_word = tag_val.replace('_',' ')
            main_info = pl_info[0]
            resp = pl_info[1] + "'s " + tag_word + " is: " + main_info
            ChatBox.config(state=NORMAL)
            ChatBox.insert(END, "Bot: " + resp + '\n\n')
            ChatBox.config(state=DISABLED)
            ChatBox.yview(END)
        

root = Tk()
root.title("Chatbot")
root.geometry("400x500")
root.resizable(width=False, height=False)

# Create Chat window
ChatBox = Text(root, bd=0, bg='white', height='8', width='50', font='Arial')

ChatBox.config(state=DISABLED)

# Bind scrollbar to Chat window
scrollbar = Scrollbar(root, command=ChatBox.yview, cursor="heart")
ChatBox['yscrollcommand'] = scrollbar.set

# Create Button to send message
SendButton = Button(root, font=("Futura", 12, 'bold'), text="Send", width=12, height=5, bd=0,
                    bg='#049101', activebackground='#960f00', fg='#000000', command=send)

# Create the box to enter message
EntryBox = Text(root, bd=0, bg='white', width='29', height='5', font='Arial')
# EntryBox.bind("<Return>", send)

# Place all components on the screen
scrollbar.place(x=376, y=6, height=386)
ChatBox.place(x=6, y=6, height=386, width=370)
EntryBox.place(x=128, y=401, height=90, width=265)
SendButton.place(x=6, y=401, height=90)

root.mainloop()