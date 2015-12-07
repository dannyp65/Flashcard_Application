# #!/usr/bin/python
# from tkinter import *
# import Font
# from Font import TITLE_FONT, MBUT_FONT, CFLabel_FONT
#  
# '''
#     Window is 600 by 600 and cannot be resized
# '''
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
from Font import *
from Flashcards import Flashcards

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
        for F in (StartPage, Menu, CreateFlashcards):
            frame = F(container, self)
            self.frames[F] = frame
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
        self.f = tk.Frame(self,width=600,height=600)
        self.CreateWidgets(controller)
        
    def printAll(self):
        for item in self.listKeys:
            print(item)    
        for item in self.listValues:
            print(item)
    
        
    def CreateWidgets(self, controller):
        self.listKeys = list()
        self.listValues = list()
        backEnd = Flashcards()
        
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
        self.finishButton = tk.Button(self, text="Finish",
                                     command=lambda: controller.show_frame(Study))
        self.finishButton.place(x=440,y=260)    
    
    def getKey(self):
        self.listKeys.append(self.frontOfCard.get())
        self.listValues.append(self.backOfCard.get())
    
class Study(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.f = tk.Frame(self,width=600,height=600)
        self.CreateWidgets(controller)
        
    def CreateWidgets(self, controller):
        hello = self
    
if __name__ == "__main__":
    app = FC_App()
    app.geometry("500x300+150+50")
    app.resizable(0, 0)
    app.mainloop()
