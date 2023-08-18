from tkinter import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pyttsx3
import speech_recognition
import threading

bot=ChatBot('Bot')
trainer=ListTrainer(bot)

data=open('y.yml','r',encoding='utf-8').readlines()
trainer.train(data)

def botreply():
    question=questionfield.get()
    question=question.capitalize()
    answer=bot.get_response(question)
    textarea.insert(END,'You: '+question+'\n\n')
    textarea.insert(END,'Bot: '+str(answer)+'\n\n')
    pyttsx3.speak(answer)
    questionfield.delete(0,END)

def audioToText():
    while True:
        sr=speech_recognition.Recognizer()
        try:
            with speech_recognition.Microphone() as m:
                sr.adjust_for_ambient_noise(m,duration=0.2)
                audio=sr.listen(m)
                query=sr.recognize_google(audio)  


                questionfield.delete(0,END)
                questionfield.insert(0,query)
                botreply() 
        
        except Exception as e:
            print(e)

# for the box 

root=Tk()
root.geometry("500x570+100+30")
root.title('CareBot')
root.config(bg='yellow')

# for robot top image

logopic=PhotoImage(file="pic.png")
logopiclabel=Label(root,image=logopic,bg="yellow")
logopiclabel.pack(pady=5)

# for frame and scrollbar

centreframe=Frame(root)
centreframe.pack()

scrollbar=Scrollbar(centreframe)
scrollbar.pack(side=RIGHT)

# for text area

textarea=Text(centreframe,font=("Courier New (monospace)",20,'bold'),height=10,yscrollcommand=scrollbar.set,wrap='word')
textarea.pack(side=LEFT)
scrollbar.config(command=textarea.yview)

# for question field/entry field

questionfield=Entry(root,font=("verdana,20"))
questionfield.pack(pady=15,fill=X)

# for button

askpic=PhotoImage(file='ask.png')
askbutton=Button(root,image=askpic,command=botreply)
askbutton.pack()

# connect ask button to enter key
def click(event):
    askbutton.invoke()


root.bind('<Return>',click)        #return=enter

thread=threading.Thread(target=audioToText)
thread.setDaemon(True)
thread.start()

root.mainloop()


# threading - used to run multiple fn simontaneously
# varna ssara time while loop chalti raheagi and bakki code ni chalega
# daemon tvd se pehle thread close hoga fir baaki chalega

