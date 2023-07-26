import tkinter as tk
import random


# crate a window with title Würfeln and one button and one img
window = tk.Tk()
window.title("Würfeln")
window.geometry("300x550")
window.resizable(False, False)

class Dice:
    def change_img(self, image):
        self.img = tk.PhotoImage(file=image)
        self.img = self.img.zoom(8, 8)
        self.img_label.configure(image=self.img)
        self.img_label.image = self.img
        
    def __init__(self, ):
        self.active_img = "1-[2,5]"
        self.img = tk.PhotoImage(file="Würfel/1/1-[2,5].png")
        self.img = self.img.zoom(8, 8)
        self.img_label = tk.Label(image=self.img)
        self.img_label.pack()
        self.count = 0
        self.list_of_results = {"1-[2,5]": 0, "1-[3,4]": 0, "2-[1,6]": 0, "2-[3,4]": 0, "3-[1,6]": 0, "3-[2,5]": 0,
                           "4-[1,6]": 0,
                           "4-[2,5]": 0, "5-[1,6]": 0, "5-[3,4]": 0, "6-[2,5]": 0, "6-[3,4]": 0}
        self.rolling = False

    def roll_dice(self, next_img=None):
        # change the img
        if next_img is None:
            next_img = random.randint(1, 3)
        if self.active_img == "1-[2,5]":
            if next_img == 1:
                window.after(250, lambda: self.change_img("Würfel/1/1-1.png"))
                window.after(500, lambda: self.change_img("Würfel/1/1-[3,4].png"))
                self.active_img = "1-[3,4]"
                print("1")
            elif next_img == 2:
                window.after(250, lambda: self.change_img("Würfel/1/1-[2,5]/1-2.png"))
                window.after(500, lambda: self.change_img("Würfel/2/2-[1,6].png"))
                self.active_img = "2-[1,6]"
                print("2")
            elif next_img == 3:
                window.after(250, lambda: self.change_img("Würfel/1/1-[2,5]/1-5.png"))
                window.after(500, lambda: self.change_img("Würfel/5/5-[1,6].png"))
                self.active_img = "5-[1,6]"
                print("5")
        elif self.active_img == "1-[3,4]":
            if next_img == 1:
                window.after(250, lambda: self.change_img("Würfel/1/1-1.png"))
                window.after(500, lambda: self.change_img("Würfel/1/1-[2,5].png"))
                self.active_img = "1-[2,5]"
                print("1")
            elif next_img == 2:
                window.after(250, lambda: self.change_img("Würfel/1/1-[3,4]/1-3.png"))
                window.after(500, lambda: self.change_img("Würfel/3/3-[1,6].png"))
                self.active_img = "3-[1,6]"
                print("3")
            elif next_img == 3:
                window.after(250, lambda: self.change_img("Würfel/1/1-[3,4]/1-4.png"))
                window.after(500, lambda: self.change_img("Würfel/4/4-[1,6].png"))
                self.active_img = "4-[1,6]"
                print("4")
        elif self.active_img == "2-[1,6]":
            if next_img == 1:
                window.after(250, lambda: self.change_img("Würfel/2/2-2.png"))
                window.after(500, lambda: self.change_img("Würfel/2/2-[3,4].png"))
                self.active_img = "2-[3,4]"
                print("2")
            elif next_img == 2:
                window.after(250, lambda: self.change_img("Würfel/2/2-[1,6]/2-1.png"))
                window.after(500, lambda: self.change_img("Würfel/1/1-[2,5].png"))
                self.active_img = "1-[2,5]"
                print("1")
            elif next_img == 3:
                window.after(250, lambda: self.change_img("Würfel/2/2-[1,6]/2-6.png"))
                window.after(500, lambda: self.change_img("Würfel/6/6-[2,5].png"))
                self.active_img = "6-[2,5]"
                print("6")
        elif self.active_img == "2-[3,4]":
            if next_img == 1:
                window.after(250, lambda: self.change_img("Würfel/2/2-2.png"))
                window.after(500, lambda: self.change_img("Würfel/2/2-[1,6].png"))
                self.active_img = "2-[1,6]"
                print("2")
            elif next_img == 2:
                window.after(250, lambda: self.change_img("Würfel/2/2-[3,4]/2-3.png"))
                window.after(500, lambda: self.change_img("Würfel/3/3-[2,5].png"))
                self.active_img = "3-[2,5]"
                print("3")
            elif next_img == 3:
                window.after(250, lambda: self.change_img("Würfel/2/2-[3,4]/2-4.png"))
                window.after(500, lambda: self.change_img("Würfel/4/4-[2,5].png"))
                self.active_img = "4-[2,5]"
                print("4")
        elif self.active_img == "3-[1,6]":
            if next_img == 1:
                window.after(250, lambda: self.change_img("Würfel/3/3-3.png"))
                window.after(500, lambda: self.change_img("Würfel/3/3-[2,5].png"))
                self.active_img = "3-[2,5]"
                print("3")
            elif next_img == 2:
                window.after(250, lambda: self.change_img("Würfel/3/3-[1,6]/3-1.png"))
    
                window.after(500, lambda: self.change_img("Würfel/1/1-[3,4].png"))
                self.active_img = "1-[3,4]"
                print("1")
            elif next_img == 3:
                window.after(250, lambda: self.change_img("Würfel/3/3-[1,6]/3-6.png"))
    
                window.after(500, lambda: self.change_img("Würfel/6/6-[3,4].png"))
                self.active_img = "6-[3,4]"
                print("6")
        elif self.active_img == "3-[2,5]":
            if next_img == 1:
                window.after(250, lambda: self.change_img("Würfel/3/3-3.png"))
                window.after(500, lambda: self.change_img("Würfel/3/3-[1,6].png"))
                self.active_img = "3-[1,6]"
                print("3")
            elif next_img == 2:
                window.after(250, lambda: self.change_img("Würfel/3/3-[2,5]/3-2.png"))
                window.after(500, lambda: self.change_img("Würfel/2/2-[3,4].png"))
                self.active_img = "2-[3,4]"
                print("2")
            elif next_img == 3:
                window.after(250, lambda: self.change_img("Würfel/3/3-[2,5]/3-5.png"))
                window.after(500, lambda: self.change_img("Würfel/5/5-[3,4].png"))
                self.active_img = "5-[3,4]"
                print("5")
        elif self.active_img == "4-[1,6]":
            if next_img == 1:
                window.after(250, lambda: self.change_img("Würfel/4/4-4.png"))
                window.after(500, lambda: self.change_img("Würfel/4/4-[2,5].png"))
                self.active_img = "4-[2,5]"
                print("4")
            elif next_img == 2:
                window.after(250, lambda: self.change_img("Würfel/4/4-[1,6]/4-1.png"))
                window.after(500, lambda: self.change_img("Würfel/1/1-[3,4].png"))
                self.active_img = "1-[3,4]"
                print("1")
            elif next_img == 3:
                window.after(250, lambda: self.change_img("Würfel/4/4-[1,6]/4-6.png"))
                window.after(500, lambda: self.change_img("Würfel/6/6-[3,4].png"))
                self.active_img = "6-[3,4]"
                print("6")
        elif self.active_img == "4-[2,5]":
            if next_img == 1:
                window.after(250, lambda: self.change_img("Würfel/4/4-4.png"))
                window.after(500, lambda: self.change_img("Würfel/4/4-[1,6].png"))
                self.active_img = "4-[1,6]"
                print("4")
            elif next_img == 2:
                window.after(250, lambda: self.change_img("Würfel/4/4-[2,5]/4-2.png"))
                window.after(500, lambda: self.change_img("Würfel/2/2-[3,4].png"))
                self.active_img = "2-[3,4]"
                print("2")
            elif next_img == 3:
                window.after(250, lambda: self.change_img("Würfel/4/4-[2,5]/4-5.png"))
                window.after(500, lambda: self.change_img("Würfel/5/5-[3,4].png"))
                self.active_img = "5-[3,4]"
                print("5")
        elif self.active_img == "5-[3,4]":
            if next_img == 1:
                window.after(250, lambda: self.change_img("Würfel/5/5-5.png"))
                window.after(500, lambda: self.change_img("Würfel/5/5-[1,6].png"))
                self.active_img = "5-[1,6]"
                print("5")
            elif next_img == 2:
                window.after(250, lambda: self.change_img("Würfel/5/5-[3,4]/5-3.png"))
                window.after(500, lambda: self.change_img("Würfel/3/3-[2,5].png"))
                self.active_img = "3-[2,5]"
                print("3")
            elif next_img == 3:
                window.after(250, lambda: self.change_img("Würfel/5/5-[3,4]/5-4.png"))
                window.after(500, lambda: self.change_img("Würfel/4/4-[2,5].png"))
                self.active_img = "4-[2,5]"
                print("4")
        elif self.active_img == "5-[1,6]":
            if next_img == 1:
                window.after(250, lambda: self.change_img("Würfel/5/5-5.png"))
                window.after(500, lambda: self.change_img("Würfel/5/5-[3,4].png"))
                self.active_img = "5-[3,4]"
                print("5")
            elif next_img == 2:
                window.after(250, lambda: self.change_img("Würfel/5/5-[1,6]/5-1.png"))
                window.after(500, lambda: self.change_img("Würfel/1/1-[2,5].png"))
                self.active_img = "1-[2,5]"
                print("1")
            elif next_img == 3:
                window.after(250, lambda: self.change_img("Würfel/5/5-[1,6]/5-6.png"))
                window.after(500, lambda: self.change_img("Würfel/6/6-[2,5].png"))
                self.active_img = "6-[2,5]"
                print("6")
        elif self.active_img == "6-[2,5]":
            if next_img == 1:
                window.after(250, lambda: self.change_img("Würfel/6/6-6.png"))
                window.after(500, lambda: self.change_img("Würfel/6/6-[3,4].png"))
                self.active_img = "6-[3,4]"
                print("6")
            elif next_img == 2:
                window.after(250, lambda: self.change_img("Würfel/6/6-[2,5]/6-2.png"))
                window.after(500, lambda: self.change_img("Würfel/2/2-[1,6].png"))
                self.active_img = "2-[1,6]"
                print("2")
            elif next_img == 3:
                window.after(250, lambda: self.change_img("Würfel/6/6-[2,5]/6-5.png"))
                window.after(500, lambda: self.change_img("Würfel/5/5-[1,6].png"))
                self.active_img = "5-[1,6]"
                print("5")
        elif self.active_img == "6-[3,4]":
            if next_img == 1:
                window.after(250, lambda: self.change_img("Würfel/6/6-6.png"))
                window.after(500, lambda: self.change_img("Würfel/6/6-[2,5].png"))
                self.active_img = "6-[2,5]"
                print("6")
            elif next_img == 2:
                window.after(250, lambda: self.change_img("Würfel/6/6-[3,4]/6-3.png"))
                window.after(500, lambda: self.change_img("Würfel/3/3-[1,6].png"))
                self.active_img = "3-[1,6]"
                print("3")
            elif next_img == 3:
                window.after(250, lambda: self.change_img("Würfel/6/6-[3,4]/6-4.png"))
                window.after(500, lambda: self.change_img("Würfel/4/4-[1,6].png"))
                self.active_img = "4-[1,6]"
                print("4")

    def stop_rolling(self):
        self.rolling = False
        self.list_of_results[self.active_img] += 1
        print(self.list_of_results)



    def button_clicked(self, durations=20):
        if self.rolling:
            return
        if self.count>0:
            self.count = 0
            return
        self.rolling = True
        for i in range(durations):
            window.after(500 * i, self.roll_dice)
        window.after(500 * durations, lambda: self.stop_rolling())
        window.after(500 * durations+20, lambda: self.button_clicked(20))
        self.count+=1


def button_clicked():
    dice_one.button_clicked()
    dice_two.button_clicked()

# if button is clicked
dice_one = Dice()
dice_two = Dice()
# create a button
button = tk.Button(text="Würfeln")
button["command"] = button_clicked
button.pack()

# create a img with 32x32 pixel scale it by 4


# run the window
window.mainloop()
