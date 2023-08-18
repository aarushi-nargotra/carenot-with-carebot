# copy paste code DONOT RUN THIS

from tkinter import *
from chatterbot import Chatbot
from chatterbot.trainers import ListTrainer
import os
import pyttsx3 
#import speech_recognition
import threading

data_list=['What are the hours of operation',
'the hours of operation are 9 am to 6 am',
'what modes of payment are accepted here',
'cash/cards/UPI']

bot=ChatBot("Bot")
trainer=ListTrainer(bot)
for files in os.listdir('data/english/'):
    data=open('data/english/'+files,'r',encoding='utf-8').readlines()
    trainer.train(data)

open('greetings.yml','r',encoding='utf-8').readlines()

trainer.train(data)

def botReply():
    question=questionField.get()
    question=question.capitalize()
    answer=bot.get_response(question)
    textarea.insert(END,'YOU: '+question+'\n\n')
    textarea.insert(END,'BOT: '+str(answer)+'\n\n')
    pyttsx3.speak(answer5)
    questionField.delete(0,END)

def audiototext():
    while True:
        sr=speech_recognition.Recognizer()
        try:

            with speech_recognition.Microphone()as m:
                sr.adjust_for_ambient_noise(m,duration=0.2)
                audio=sr.listen(m)
                query=sr.recognize_google(audio)
                


                questionField.delete(0,END)
                questionField.insert(0,query)
                botReply()
        except Exception as e:
            print(e)        


root=Tk()
root.geometry('500x770+100+30')
root.title("NO PROBLEM CUSTOMER CARE")
root.config(bg='light blue')

logoPic=PhotoImage(file='Beige Tan Minimalist Boho Home Decor and Interior Design Logo.png')
logoPiclabel=Label(root,image=logoPic)
logoPiclabel.pack()

centreFrame=Frame(root,height=30)
centreFrame.pack()

scrollbar=Scrollbar(centreFrame)
scrollbar.pack(side=RIGHT)

textarea=Text(centreFrame,font=('times new roman',20,'bold'),height=10,yscrollcommand=scrollbar.set) #yscrollcommand is builtin.
textarea.pack(side=LEFT)

scrollbar.config(command=textarea.yview)

questionField=Entry(root,font=('verdana',20,'bold'))
questionField.pack(pady=15,fill=X)

askPic=PhotoImage(file='images.png')
askbutton=Button(root,image=askPic,command=botReply)
askbutton.pack()

def click(event):
    askbutton.invoke

root.bind('<Return>',click)

thread=threading.Thread(target=audiototext)
thread.setDaemon(True)
thread.start()



root.mainloop()