import tkinter as tk
import subprocess

class Menu:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master,bg="black")
        self.button1 = tk.Button(self.frame, text="Rock Paper Scissor", width=825, command=self.run_script1,font=("Times New Roman",20),bg="#8EA4C8")
        self.button2 = tk.Button(self.frame, text="Dice", width=825, command=self.run_script2,font=("Times New Roman",20),bg="#C3B8AA")
        self.button3 = tk.Button(self.frame, text="Coin", width=825, command=self.run_script3,font=("Times New Roman",20),bg="#DEDCE4")
        self.button4 = tk.Button(self.frame, text="Hangman", width=825, command=self.run_script4,font=("Times New Roman",20),bg="#DB93A5")
        self.button5 = tk.Button(self.frame, text="Speedtest", width=825, command=self.run_script5,font=("Times New Roman",20),bg="#C7CDC5")
 
        self.button1.pack(pady=15)
        self.button2.pack(pady=15)
        self.button3.pack(pady=15)
        self.button4.pack(pady=15)
        self.button5.pack(pady=15)
      
        self.frame.pack()

    def run_script1(self):
        subprocess.call(["python", "Final_r,p,s.py"])

    def run_script2(self):
        subprocess.call(["python", "Final_dice.py"])

    def run_script3(self):
        subprocess.call(["python", "Final_coin.py"])
        
    def run_script4(self):
        subprocess.call(["python", "Final_hangman.py"])
        
    def run_script5(self):
        subprocess.call(["python", "Final_speedtesting.py"])    

root = tk.Tk()

root.title("MINI ARCADE")
root.bg ="black"
root.geometry("900x450")
app = Menu(root)
root.mainloop()
