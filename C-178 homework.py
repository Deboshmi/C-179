from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import random
root = Tk()
root.title("Random Colour Change App")
root.geometry("800x600")
root.config(bg="orange2")

label_name = Label(root,bg="white", font=("Sylfaen",18,"bold","italic"))
label_name.place(relx=0.05,rely=0.1, anchor= W)
class game :
    
    def __init__ (self):
        self.__score = 0
    def updateGame(self):
        self.text = ["BLACK","PINK","GREEN","BLUE","RED","YELLOW"]
        self.random_number_for_text = random.randint(0,5)
        self.color = ["black","pink","green","blue","yellow","red"]
        self.random_number_for_color = random.radint(0,5)
        label_name["text"] = self.text[self.random_number_for_text]
        label_name["fg"] = self.color[self.random_number_for_color]

obj = game()
def getInput():
    value = input_value.get()
    onj.get_user_value(value)
    obj.updateGame()
    input_value.delete(0,END)
btn = Button(root, text="CHECK" ,command=obj.updateGame, bg="IndianRed1", fg="white", relief=FLAT, padx=10, pady=1, font=("Arial",15))
btn.place(relx=0.35,rely=0.65, anchor= CENTER)
btn = Button(root, text="START" ,command=obj.updateGame, bg="dark olive green", fg="white", relief=FLAT, padx=10, pady=1, font=("Arial",15))
btn.place(relx=0.65,rely=0.65, anchor= CENTER)
root.mainloop()   