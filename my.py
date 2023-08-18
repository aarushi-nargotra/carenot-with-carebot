from tkinter import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot=ChatBot('Bot')
trainer=ListTrainer(bot)

data=open('y.yml','r',encoding='utf-8').readlines()
trainer.train(data)

def botreply():
    question=questionfield.get()
    answer=bot.get_response(question)
    textarea.insert(END,'You: '+question+'\n\n')
    textarea.insert(END,'Bot: '+str(answer)+'\n\n')
    questionfield.delete(0,END)

# for the box 

root=Tk()
root.geometry("500x570+100+30")
root.title('ChattyBot')
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

root.mainloop()