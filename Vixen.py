# ----------------------------------------------------------------------
#  Vixen
#
#  A little chatbot made in python with tkinter and json
#  Made by TheBigEye
# ----------------------------------------------------------------------

import json
import time
import tkinter
from difflib import get_close_matches
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar

Main = Tk()

Cursor_User = "👤: "
Cursor_Fox = "🦊: "
Cursor = "Assets/Cursors/Cursor.cur"

# Colors
Again = 0

Chat_BG = "#030303"
Message_BG = "black"
Input_BG = "#090C0F"
InfoMenu_BG = "white"

####################################################################################################################


# Tree diagram
with open("Assets/Objects/Tree", "r", encoding="UTF-8") as Archive_Tree:
    Tree = Archive_Tree.read()

# Fox 
with open("Assets/Objects/Fox", "r", encoding="UTF-8") as Archive_Fox:
    Fox = Archive_Fox.read()  



# Python logo
with open("Assets/Objects/Logos/Python_logo", "r", encoding="UTF-8") as Python:
    Python_logo = Python.read()

# Anonymous mask logo
with open("Assets/Objects/Logos/Mask_logo", "r", encoding="UTF-8") as Mask:
    Mask_logo = Mask.read()    


###################################################################################################################

# Logo
Logo_image = "Assets/Images/Logo.png"


# Nornal face
Normal_Face = "Assets/Images/States/fox.png"

# Nornal face
Closed_Eyes_Face = "Assets/Images/States/fox_2.png"

# Joy face
Joy_Face = "Assets/Images/States/fox_3.png"

###################################################################################################################

# Progressbar style
Style_Progress = ttk.Style()
Style_Progress.theme_use("clam")
Style_Progress.configure(
    "red.Horizontal.TProgressbar",
    foreground="Black",
    background=InfoMenu_BG,
    borderwidth=0,
    troughcolor=Chat_BG,
    bordercolor=Chat_BG,
    lightcolor=Chat_BG,
    darkcolor=Chat_BG,
)


# Commands progrssbar
progress = Progressbar(
    Main,
    style="red.Horizontal.TProgressbar",
    orient=HORIZONTAL,
    length=100,
    mode="determinate",
)

progress.place(x=550, y=150)


# System (chat) #####################################################################################################


class System:
    def __init__(self, Chat):

        Chat.title("Vixen")
        Chat.geometry("600x700")
        Chat.config(background_=Chat_BG)
        Chat.iconbitmap("Assets/Icons/Fox.ico")
        Chat.resizable(0, 0)

        # Cursor config

        Main.config(cursor="@" + Cursor)
        Chat.config(cursor="@" + Cursor)

        self.message_session = Text(
            Chat,
            bd=2,
            relief="flat",
            font=("Consolas", 11),
            undo=True,
            wrap="word",
        )

        self.message_session.config(
            width=65, height=39, bg=Message_BG, fg="orange", state="disabled"
        )

        self.overscroll = Scrollbar(
            Chat,
            command=self.message_session.yview,
            bg="black",
            troughcolor=Chat_BG,
            borderwidth=0,
        )

        self.overscroll.config(width=-1, bg="black", activebackground="black")
        self.overscroll.pack(side=RIGHT, fill=Y)

        self.message_session["yscrollcommand"] = self.overscroll.set
        self.message_position = 1.5

        self.Message_Entry = Entry(
            Chat,
            borderwidth=0.4,
            width=54,
            fg="dark gray",
            bg=Input_BG,
            font=("Consolas", 12),
        )
        self.Message_Entry.config(insertbackground="white")
        self.Message_Entry.bind("<Return>", self.reply_to_you)

        self.message_session.place(x=0, y=0)
        self.Message_Entry.place(x=5, y=697)

        self.Brain = json.load(open("Scripts.json", encoding="UTF-8"))

    def add_chat(self, message):
        self.message_position += 20.0
        self.Message_Entry.delete(0, "end")
        self.message_session.config(state="normal")
        self.message_session.insert(self.message_position, message)
        self.message_session.see("end")
        self.message_session.config(state="disabled")

    def reply_to_you(self, event=None):

        def ProgressBarAnim():

            progress["value"] = 0

            for i in range(25):
                time.sleep(0.2)
                progress["value"] += 4
                Main.update_idletasks()

            progress["value"] = 0

        message = self.Message_Entry.get().lower()
        message = Cursor_User + message + "\n"
        close_match = get_close_matches(message, self.Brain.keys())

        global Again

        # Get replies in the JSON file
        if close_match:
            reply = Cursor_Fox + self.Brain[close_match[0]][0] + "\n"

        # Random replies
        elif Again == 0:
            reply = Cursor_Fox + "Ok? \n"
            Again += 1

        elif Again == 1:
            reply = Cursor_Fox + "Tell me more \n"
            Again += 1

        elif Again == 2:
            reply = Cursor_Fox + "Interesting \n"
            Again += 1

        elif Again == 3:
            reply = Cursor_Fox + "I get it \n"
            Again += 1

        elif Again == 4:
            reply = Cursor_Fox + "Could we talk more?\n"
            Again += 1

        elif Again == 5:
            reply = Cursor_Fox + "hmm ok? \n"
            Again = 0

        else:
            reply = Cursor_Fox + "Good \n"



        # Messages ##########################################################################################################

        # MSG equals Message 
        MSG = self.Message_Entry.get().lower()

        if (MSG == "/test"):

            reply = Cursor_Fox + "test" + "\n"

        # Hi, hello
        if (MSG == "hi"):

            reply = Cursor_Fox + "Hi, welcome" + "\n"


        # F
        if (MSG == "f"):

            reply = Cursor_Fox + "F x2" + "\n"


        # lol
        if (MSG == "lol"):

            reply = Cursor_Fox + "lol, xd" + "\n"

        
        # XD
        if (MSG == "xd"):

            reply = Cursor_Fox + "xddd" + "\n"            


        # are you furry?
        if (MSG == "are you furry?"):

            reply = Cursor_Fox + "\n" + Fox + "\n" + Cursor_Fox + "Yes, i'm furry" + "\n"


        # what programming language are you made in?
        if MSG == "what programming language are you made in?":

            reply = Python_logo + "\n" + Cursor_Fox + "In Python" + "\n"



        # Commands ##########################################################################################################

        CMD = self.Message_Entry.get().lower()

        # /Mask command
        if (CMD == "/start"):

            ProgressBarAnim()

            reply = Cursor_Fox + "\n" + Mask_logo + "\n"            


        # /Tree command
        if (CMD == "/tree"):

            ProgressBarAnim()

            reply = Cursor_Fox + "Use /cd FILENAME" + "\n" + Tree + "\n"


        # /open commands
        if self.Message_Entry.get().lower() == "/cd documents":

            ProgressBarAnim()

            reply = Cursor_Fox + "Use /cd FILENAME" + "\n" + Tree + "\n"

        # Info #############################################################################################################

        self.add_chat(message)
        self.add_chat(reply)

        Status = Label(
            Main,
            width=20,
            height=1,
            bg=Chat_BG,
            fg=InfoMenu_BG,
            font=("Consolas", 8),
            text=message,
        )
        Status.place(x=534, y=128)


# Info panel #######################################################################################################

Main.wait_visibility(Main)


# transparent Chats
Main.wm_attributes("-alpha", 0.96)


# Chat Chat
System(Main)

#if System(Main).Message_Entry.get().lower() == "animate":
#    Logo_IMG = tkinter.PhotoImage(file=Closed_Eyes_Face)

Main.geometry("525x725")

FrameCount = 2
Logo_IMG = [PhotoImage(file='Assets/Images/Fox.gif',format = 'gif -index %i' %(i)) for i in range(FrameCount)]

Phase = 0
def update(ind):

    global Delay 
    Delay = 1000
    Frame = Logo_IMG[ind]
    ind += 1

    if ind == FrameCount:
        ind = 0
    
    if ind == 1:
        Delay = 512
    else:
        Delay = 5000

    Logo = Label(Main, width=59, height=60)
    Logo.place(x=564, y=40)    
    Logo.configure(image = Frame)

    Main.after(Delay, update, ind)


Main.after(0, update, 0)



# text="LT.Fox Vixen"

# Info menu ########################################################################################################


# Open info menu
def Click_Open():
    Main.geometry("675x725")
    time.sleep(0.1)
    Expand_Button_1.place(x=1024, y=1024)
    Expand_Button_2.place(x=498, y=690)


# Close info menu
def Click_Close():
    Main.geometry("525x725")
    time.sleep(0.1)

    Expand_Button_1.place(x=498, y=690)
    Expand_Button_2.place(x=1024, y=1024)


Expand_Button_1 = Button(
    Main,
    borderwidth=0,
    relief=RAISED,
    width=1,
    height=1,
    text=">",
    bg=Message_BG,
    fg="gray",
    font=("Consolas", 12),
    command=Click_Open,
)
Expand_Button_1.place(x=498, y=690)

Expand_Button_2 = Button(
    Main,
    borderwidth=0,
    relief=RAISED,
    width=1,
    height=1,
    text="<",
    bg=Message_BG,
    fg="gray",
    font=("Consolas", 12),
    command=Click_Close,
)
Expand_Button_2.place(x=1024, y=1024)

###################################################################################################################


Main.mainloop()
