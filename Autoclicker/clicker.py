import tkinter as tk
import mouse
import threading
import time
from pynput import keyboard

#intall pynput and mouse
#use 3.9 python

class Autoclicker():
    def __init__(self, window):

       

        global targetKey
        targetKey = "*"
        global targetKeyPressed
        targetKeyPressed = False
        global clickRate
        clickRate = 1000
        global targetPosition
        targetPosition = (-1, -1)
        global setTargetKey
        setTargetKey = False

        listener = keyboard.Listener(
            on_press = self.on_press,
            on_release = self.on_release)
        listener.start()

        controller = threading.Thread(target = self.clickloop,
                                      args = ())
        controller.start()

        
        #self.myMouse = Mouse()
        #self.myKeyboard = Keyboard(targetKey = self.targetKey)


        
        self.button1 = tk.Button(
            text = "Key",
            relief = tk.RAISED,
            command = self.setTargetKey
            )
        
        self.entry1 = tk.Entry()
        self.Button1 = tk.Button(text="Click Rate(ms)",
                                 command = self.setClickRate)
        self.entry2 = tk.Entry()
        self.Button2 = tk.Button(text="Mouse Position")
        self.entry3 = tk.Entry()
        self.entry4 = tk.Entry()
        
        self.button1.grid(row=0, column = 0)
        self.entry1.grid(row=0, column=1)
        self.Button1.grid(row=1, column=0)
        self.entry2.grid(row=1, column=1)
        self.Button2.grid(row=2, column=0)
        self.entry3.grid(row=2, column=1)
        self.entry4.grid(row=2, column=2)

    def on_release(self, key):
        print("key was released")

    def on_press(self, key):
        print("key was pressed")

        try:
            if key.char == targetKey:
                print("target key was pressed")

                global targetKeyPressed
                targetKeyPressed = not targetKeyPressed

        except:
            if key == keyboard.Key.esc:
                quit()
                
    def clickloop(self):
        while True:
            if targetKeyPressed == True:
                mouse.click()
                time.sleep(clickRate/1000)

    def handle_keypress(self, event):

        global setTargetKey
        if setTargetKey:
            
            global targetKey
            self.entry1.delete(0, tk.END)
            self.entry1.insert(0, event.char)
            setTargetKey = False

            try:

                targetKey = event.char

            except:

                targetKey = "*"

    def setTargetKey(self):

        self.entry1.delete(0, tk.END)
        self.entry1.insert(0, "Please enter a key")
        global setTargetKey
        setTargetKey = True

    def setClickRate(self):

        global clickRate
        try:

            clickRate = int(self.entry2.get())

        except:
            clickRate = 1000

window = tk.Tk()
app = Autoclicker(window)
window.bind("<Key>", app.handle_keypress)
    
