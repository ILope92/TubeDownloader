import tkinter.ttk as ttk
from tkinter import messagebox as mb
from Libs.youtube import Download


class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Download YouTube Videos")
        self.root.geometry('500x63')
        self.all_links()
        self.links()
        self.root.mainloop()

    def links(self):
        self.link = ttk.Entry(self.root, width=59)
        self.link.grid(row=0, column=0, padx=3, pady=3, ipady=4)
        add = ttk.Button(self.root, text='Add link', command=self.get_link)
        add.grid(row=0, column=1)
        frame = ttk.Frame(self.root)
        frame.grid(row=1, columnspan=2)
        download = ttk.Button(
            frame,
            text='Download',
            width=69,
            command=self.download
            )
        download.grid(row=0, column=0, padx=3)

    def all_links(self):
        self.new_links = []

    def get_link(self):
        txt = self.link.get()
        self.new_links.append(txt)

    def download(self):
        down = Download()
        exc = down.download(links=self.new_links)
        if exc is None:
            pass
        elif 'Error' in exc:
            mb.showerror("Error", "Error in link!")
