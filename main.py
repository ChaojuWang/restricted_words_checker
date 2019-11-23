#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tkinter
from tkinter import messagebox
import lib


def check():
    text_box.tag_remove('tagged','1.0','end')
    l=lib.read_restricted_word_list()
    count=0
    for w in l:
        if w == '':
            continue
        length = tkinter.IntVar()
        cur = 1.0
        while True:
            cur = text_box.search(w,cur,tkinter.END,count=length)
            if not cur:
                break
            match_end = '{}+{}c'.format(cur,length.get())
            text_box.tag_add('tagged',cur,match_end)
            cur = text_box.index(match_end)
            count+=1
    messagebox.showinfo("提示",'发现{}处违禁词'.format(count))

window = tkinter.Tk()
window.title("限制词检测工具")
window.geometry('1366x768')
scrollbar = tkinter.Scrollbar(window)
scrollbar.pack(side=tkinter.RIGHT,fill=tkinter.Y)
text_box = tkinter.Text(window,yscrollcommand=scrollbar.set)
text_box.tag_configure('tagged', background='yellow')
text_box.pack(fill='both',padx=10,pady=10,expand=1)
button_check = tkinter.Button(window,text="检查",command=check)
button_check.pack(padx=10,pady=10)
window.mainloop()