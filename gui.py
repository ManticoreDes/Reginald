import tkinter as tk
from turtle import bgcolor

root = tk.Tk()
main_frame = tk.Frame(master=root,)
tk.Label(root, text='BRAIN FEED', bg="black",
    fg="orange", width=100,).pack()
chat_listbox = tk.Listbox(master=main_frame, height=100, width=100, bg="black",
    fg="red",)
scroll_bar = tk.Scrollbar(master=main_frame)

speak_button = tk.Button(master=root, text='Input', height=100, width=10, command=lambda: None, bg="black",
    fg="blue",)


def set_speak_command(command):
    speak_button.configure(command=command)


speak_button.pack(side=tk.LEFT, anchor=tk.W)


def speak(text):
    chat_listbox.insert('end', f'REG: {text}')


scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
chat_listbox.pack(fill=tk.Y, side=tk.RIGHT)
scroll_bar.configure(command=chat_listbox.yview)
chat_listbox.configure(yscrollcommand=scroll_bar.set)
main_frame.pack(fill=tk.BOTH)
root.geometry('600x450')
root.minsize(400, 250)
root.wm_title('Reginald')
root.resizable(False, True)
mainloop = root.mainloop
root.iconbitmap("REGGY 2.ico")
root.attributes('-alpha', 0.9)