
#   
# class FCApp(Tk):
#     
#     def __init__(self, parent):
#         Frame.__init__(self, parent, background="white")   
#            
#         self.parent = parent
#           
#         self.initUI()
#         
#       
#     def initUI(self):
#         self.parent.title("Flashcard Application")
#         self.pack(fill=BOTH, expand=1)
#         quitButton_x = 15
#         quitButton_y = 560
#         FCApp.quitButton(self, quitButton_x, quitButton_y)
#         
#         # Container is where I stack a bunch of frames
#         # on top of each other, then the one I want visible
#         # will be raised above the others
#         container = Frame(self)
#         
#         
#         self.frames = {}
#         for F in (WelcomeScreen, CreateFlashcards):
#             frame = F(container, self)
#             self.frames[F] = frame
#             
#         self.show_frame(WelcomeScreen)
#         
#           
#     def quitButton(self, x_coordinate, y_coordinate):
#         quitBut = Button(self, text="Quit",
#                          command=self.quit)
#         quitBut.place(x=x_coordinate,y=y_coordinate)
#     
#     def show_frame(self, c):
#         frame = self.frames[c]
#         frame.tkraise()
# '''      
# class Button():
#     def __init__(self, x_coordinate, y_coordinate):
#         self.x_coordinate = x_coordinate
#         self.y_coordinate = y_coordinate
#     def quitButton(self):
#         quitBut = Button(self, text="Quit",
#                          command=close_window())
#         quitBut.place(x=self.x_coordinate,y=self.y_coordinate) 
#     def close_window(self):
#         self.destroy()
# class CommandsWin():
#     '''
#   
# class WelcomeScreen(Frame):
#     def __init__(self, parent, controller):
#         Frame.__init__(self, parent)
#         self.controller = controller
#         label = Label(self, text="Welcome to the Flashcard Application!", font=TITLE_FONT)
#         label.pack(side="bottom", fill="x", pady=10)
#          
#         button1 = Button(self, text="Next", command=lambda: controller.show_frame(Menu))
#         button1.pack()
#          
# class Menu(Frame):
#     def __init__ (self, parent, controller):
#         Frame.__init__(self, parent)
#         self.controller = controller
#         createButton = Button(self, text="Create flash cards", font=MBUT_FONT,
#                       command=lambda: controller.show_frame(CreateFlashcards))
#         createButton.pack()
#          
# class CreateFlashcards(Frame):
#     def __init__ (self, parent, controller):
#         Frame.__init__(self, parent)
#         self.controller = controller
#         label = Label(self, text="Create flash cards.", font=CFLabel_FONT)
#         label.pack(side="top", fill="x", pady=10)
#         
#         text1 = Text(self)
#         text1.pack()
#   
# # def main():
# #     
# #     root = Tk()
# #     root.geometry("600x600+150+50")
# #     app = Window(root)
# #     root.resizable(0,0)
# #     root.mainloop()  
#   
# if __name__ == '__main__':
#     root = Tk()
#     root.geometry("600x600+150+50")
#     app = FCApp(root)
#     root.resizable(0, 0)
#     root.mainloop()

import tkinter as tk
import tkinter.messagebox
from tkinter.ttk import *
from Font import *
from Flashcards import *
from random import *

#Global variable
backEnd = Flashcards()
global messageFront
global messageBack
###There are more


class FC_App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Flashcard Application")
        
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, Menu, CreateFlashcards, Study):
            frame = F(container, self)
            self.frames[F] = frame
            s = Style()
            s.configure(frame, background="white")
            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, c):
        '''Show a frame for the given class'''
        frame = self.frames[c]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Welcome to the flashcard\napplication!",
                          font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        label1 = tk.Label(self, text="Creators: Van Le, Connie Lim, Nhan Pham")
        label1.pack(side="top", pady=10)
        button1 = tk.Button(self, text="Next",
                            command=lambda: controller.show_frame(Menu))
        button1.pack(side="bottom", pady=10)


class Menu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Menu", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Create flashcards",
                           command=lambda: controller.show_frame(CreateFlashcards))
        button.pack()


class CreateFlashcards(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.f = tk.Frame(self,width=300,height=500)
        self.CreateWidgets(controller)
        
    def printAll(self):
        for item in self.listKeys:
            print(item)    
        for item in self.listValues:
            print(item)
    
        
    def CreateWidgets(self, controller):
        global listKeys
        listKeys = []
        global listValues
        listValues = []
        global messageWid
        messageWid = tkinter.StringVar()
        
        #Labels
        label = tk.Label(self, text="Create some flashcards", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        instructions = tk.Label(self, text="Type in the left box to enter one side of the flashcard.")
        instructions.pack(side="top", pady=(10, 0))
        instructions1 = tk.Label(self, text="Type in the right box to enter the other side of the flashcard.")
        instructions1.pack(side="top")
        instructions2 = tk.Label(self, text="Click 'Submit entries' to enter one completed flashcard.")
        instructions2.pack(side="top")
        #Text entry boxes
        self.frontOfCard = tk.Entry(self)
        self.backOfCard = tk.Entry(self)
        self.frontOfCard.config(width=20)
        self.backOfCard.config(width=20)
        self.frontOfCard.place(x=50,y=150)
        self.backOfCard.place(x=330, y=150)
        
        #Buttons
        self.menuButton = tk.Button(self, text="Menu",
                           command=lambda: controller.show_frame(Menu),
                           bg="white")
        self.menuButton.config(width=10)
        self.menuButton.place(x=20, y=260)
        self.submitButton = tk.Button(self, text="Submit entries",
                                 command=self.getKey)
        self.submitButton.config(width=15)
        self.submitButton.place(x=200, y=260)
        self.finishButton = tk.Button(self, text="Finish", command=self.showFinishedBox)
        self.finishButton.place(x=440,y=260)    
                
    def getKey(self):
        listKeys.append(self.frontOfCard.get())
        listValues.append(self.backOfCard.get())
        self.clear_text()
            
    def clear_text(self):
        self.frontOfCard.delete(0, "end")
        self.backOfCard.delete(0, "end")
        self.frontOfCard.insert(0, "")
        self.backOfCard.insert(0, "")
        
    def showFinishedBox(self):
        self.answer = tkinter.messagebox.askquestion('Finish', 'Are you done submitting flashcards?')
        if self.answer == 'yes':
            flag = False #boolean to continue to next scene
            if len(listKeys) > 0 and len(listValues) > 0:
                flag = True
                
            if flag == True:
                side_one = listKeys
                side_two = listValues
                messageStudy= listKeys[0]
                messageWid = listValues[0]
                self.controller.show_frame(Study)
            else:
                tkinter.messagebox.showinfo("Error", "Do not forget to submit entries!\nYou have no flashcards!")
            
            
class Study(tk.Frame):
        
    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.f = tk.Frame(self,width=500,height=300)
        self.CreateWidgets(controller)
        
    def CreateWidgets(self, controller):
        self.y_button_coordinate = 260
        #Random number for printing out flash cards
        self.randomNum = randint(0, len(listKeys))
        self.showLabel = False
        self.makeNewCard = False
        #Title labels
        study_label = tk.Label(self, text="Study Scene", font=TITLE_FONT)
        study_label.pack(side="top")
        
        #Buttons
        self.menuButton = tk.Button(self, text="Menu",
                           command=lambda: controller.show_frame(Menu),
                           bg="white")
        self.menuButton.config(width=10)
        self.menuButton.place(x=20, y=self.y_button_coordinate)
        self.flipButton = tk.Button(self, text="Flip card",
                                    command=self.flip)
        self.flipButton.config(width=12)
        self.flipButton.place(x=140, y=self.y_button_coordinate)
        self.nextCardButton = tk.Button(self, text="Next card", command=self.nextPart)
        self.nextCardButton.config(width=10)
        self.nextCardButton.place(x=270, y=self.y_button_coordinate)
        self.finishButton = tk.Button(self, text="Finish", command=self.quit)
        self.finishButton.config(width=10)
        self.finishButton.place(x=400,y=self.y_button_coordinate)
        self.startButton = tk.Button(self, text="Begin", command=self.initalize)
        self.startButton.config(width=15,height=3)
        self.startButton.place(x=200, y=75)
        
        
    def print_debug(self):
        for item in listKeys:
            print(item)
        message = listKeys[0]
        print(message + ":")   
    def initalize(self):
        self.startButton.destroy()
        message = listKeys[self.randomNum]
        self.frontL0 = tk.Label(self, text=message, font=CFLabel_FONT2)
        self.frontL0.place(x=160, y=75)
    def nextCard(self):
        if self.makeNewCard is True:
            message = listKeys[self.randomNum]
            self.frontL0.config(text=message)
            self.makeNewCard = False
        else:
            message = listKeys[self.randomNum]
            self.frontL0 = tk.Label(self, text=message, font=CFLabel_FONT2)
            self.frontL0.place(x=160, y=75)
    def flip(self):
        if self.showLabel is False: 
            message1 = listValues[self.randomNum]
            self.frontL1 = tk.Label(self, text=message1, font=CFLabel_FONT1)
            self.frontL1.place(x=160, y=125)
            self.showLabel = True
        else:
            self.frontL1.destroy()
            self.showLabel = False
    def nextPart(self):
        self.tempRandomNum = self.randomNum
        self.randomNum = randint(0, len(listKeys))
        if self.tempRandomNum == self.randomNum:
            while (self.randomNum != self.randomNum):
                self.randomNum = randint(0, len(listKeys))
        self.makeNewCard = True
        self.nextCard
        
if __name__ == "__main__":
    app = FC_App()
    app.geometry("500x300+150+50")
    app.resizable(0, 0)
    app.mainloop()
