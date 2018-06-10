import tkinter as tk
from thomson import ThomsonRestart
from dir import DirRestart

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Thomson restart button
        self.thomson_btn = tk.Button(self)
        self.thomson_btn["text"] = "Restart Thomson"
        self.thomson_btn["command"] = self.restartThomsonRouter
        self.thomson_btn.pack(side="top", padx="10", pady="5")



        # DIR restart button
        self.dir_btn = tk.Button(self)
        self.dir_btn["text"] = "Restart DIR"
        self.dir_btn["command"] = self.restartDirRouter
        self.dir_btn.pack(side="top", padx="10", pady="5")

        # "Quit" button
        self.quit = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
        self.quit.pack(side="bottom", padx="10", pady="5")

        # Confirmation textfield
        self.confirmation = tk.Canvas(root, width=300, height=500)
        self.confirmationID = self.confirmation.create_text(300/2-10, 10, text="", state=tk.DISABLED)
        self.confirmation.pack(side="bottom", padx="10", pady="5")

    def restartDirRouter(self):
        dir = DirRestart
        dir.restart(dir,self)

    def restartThomsonRouter(self):
        th = ThomsonRestart
        th.restart(th, self)

    def updateInformationField(self,text):
        self.confirmation.itemconfigure(self.confirmationID, text=text)


windowWidth = 300
windowHeight = 200

root = tk.Tk()
root.geometry("%dx%d+400+400" % (windowWidth, windowHeight))

app = Application(master=root)
app.master.title("Restart my wifi routers")
app.mainloop()


