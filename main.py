import tkinter.messagebox
from tkinter import *


class Game(Tk):
    buttonList = []
    sign = None
    marks = 0
    winner = None

    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe")
        self.geometry("640x360")

    def createButton(self, x, y):
        button = Button(self, text="   ", command=lambda: self.mark(x, y), font="comicsansms 22 bold", padx=29, pady=22)
        button.grid(column=x, row=y)
        self.buttonList.append([button, {"x": x, "y": y}])

    def decideSign(self):
        choices = ["X", "O"]
        self.sign = choices[(self.marks % 2)]
        return self.sign

    def mark(self, x, y):
        for button in self.buttonList:
            if button[1]["x"] == x and button[1]["y"] == y:
                button[0].configure(text=self.decideSign())
                self.checkWinner()
                self.marks += 1
        if self.marks >= 9:
            tkinter.messagebox.showinfo(title="Match Tied!", message="Oh! Seems like this match has been tied!")

    def checkWinner(self):
        if self.buttonList[0][0]["text"] == self.buttonList[3][0]["text"] == self.buttonList[6][0]["text"] != "   ":
            self.highlightWinner(self.buttonList[0][0], self.buttonList[3][0], self.buttonList[6][0])

        elif self.buttonList[0][0]["text"] == self.buttonList[4][0]["text"] == self.buttonList[8][0]["text"] != "   ":
            self.highlightWinner(self.buttonList[0][0], self.buttonList[4][0], self.buttonList[8][0])

        elif self.buttonList[6][0]["text"] == self.buttonList[4][0]["text"] == self.buttonList[2][0]["text"] != "   ":
            self.highlightWinner(self.buttonList[6][0], self.buttonList[4][0], self.buttonList[2][0])

        elif self.buttonList[1][0]["text"] == self.buttonList[4][0]["text"] == self.buttonList[7][0]["text"] != "   ":
            self.highlightWinner(self.buttonList[1][0], self.buttonList[4][0], self.buttonList[7][0])

        elif self.buttonList[2][0]["text"] == self.buttonList[5][0]["text"] == self.buttonList[8][0]["text"] != "   ":
            self.highlightWinner(self.buttonList[2][0], self.buttonList[5][0], self.buttonList[8][0])

        elif self.buttonList[0][0]["text"] == self.buttonList[1][0]["text"] == self.buttonList[2][0]["text"] != "   ":
            self.highlightWinner(self.buttonList[0][0], self.buttonList[1][0], self.buttonList[2][0])

        elif self.buttonList[3][0]["text"] == self.buttonList[4][0]["text"] == self.buttonList[5][0]["text"] != "   ":
            self.highlightWinner(self.buttonList[3][0], self.buttonList[4][0], self.buttonList[5][0])

        elif self.buttonList[6][0]["text"] == self.buttonList[7][0]["text"] == self.buttonList[8][0]["text"] != "   ":
            self.highlightWinner(self.buttonList[6][0], self.buttonList[7][0], self.buttonList[8][0])

    def highlightWinner(self, btn1, btn2, btn3):
        btn1.configure(bg="#a8acbe")
        btn2.configure(bg="#a8acbe")
        btn3.configure(bg="#a8acbe")
        self.winner = btn1["text"]
        tkinter.messagebox.showinfo(title="Match won!", message=f"{self.winner} has won this match!")
        for button in self.buttonList:
            button[0].configure(command=self.falseTurn)

    def falseTurn(self):
        tkinter.messagebox.showerror(title="False Turn", message=f"You cannot give a turn! {self.winner} has already won!")


if __name__ == '__main__':
    window = Game()
    for i in range(0, 3):
        for j in range(0, 3):
            window.createButton(i, j)
    window.mainloop()
