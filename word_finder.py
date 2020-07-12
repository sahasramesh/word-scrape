import os
import time
import webbrowser
import tkinter as tk
from tkinter import *
from itertools import permutations

#contain full program in a function for GUI
def WordScrape(userLet):

    #define counter and empty lists
    filterWords = []
    finalList = []
    comboPerms = []
    allPerms = []

    #function to convert list to string
    def convert(list):
        s = [str(i) for i in list]
        res = str(", ".join(s))
        return res

    #removes duplicates from list
    def noRepeats(x):
        return list(dict.fromkeys(x))

    #function to remove 2 and 1 letter words
    def removeShortPerms(wordss):
        return [i for i in wordss if len(i) >= 3]

    #interpret user input
    userLen = len(userLet)

    #open words doc and split words into list
    with open("everyword.rtf") as f:
        words = f.read().split()
    words = [x.lower() for x in words]
    wordsLen = len(words)

    #find all permutations of user input
    perms = [''.join(p) for p in permutations(userLet)]
    permsLen = len(perms)

    print("\nLoading permutations...")
    #print("All permutations: ", perms)

    #filter out words longer than the user-submitted letters(or too short)
    for z in range(0, wordsLen):
        if 3 <= len(words[z]) <= userLen:
            filterWords.append(words[z])
    filterLen = len(filterWords)

    #create smaller permutations
    def shorterPerms(num):
        newPerms = []
        for y in range(0, permsLen):
            miniPerm = perms[y]
            miniPerm = miniPerm[num : : ]
            newPerms.append(miniPerm)
        return newPerms

    #add all perm lists depending on number of letters
    if 1 <= userLen <= 3:
        allPerms = perms

    if 4 <= userLen <= 9:
        for i in range(1, userLen):
            comboPerms+= list(dict.fromkeys(shorterPerms(i)))
        allPerms = perms + comboPerms

    allPerms = list(dict.fromkeys(allPerms))
    allPerms = removeShortPerms(allPerms)
    allPermsLen = len(allPerms)

    #find match with perms from word doc
    print("Finding matches...\n")
    for x in range(0, allPermsLen):
        for y in range(0, filterLen):
            if allPerms[x] == filterWords[y]:
                finalList.append(allPerms[x])

    outputList = noRepeats(finalList)
    return outputList

window = Tk()
window.configure(background='#EEE')
window.title("WordScrape")
window.geometry('325x350')
window.resizable(width=False, height=False)

n = 14
fonty = "Courier"
def submitbtn():
    wordys = WordScrape(txt.get())
    lbl1.configure(text=wordys, wraplength=280, justify=LEFT)

def clearbtn():
    txt.delete(0, END)
    txt.insert(0, "")
    lbl1.configure(text="")

def tagbtn():
    webbrowser.open("http://sahasramesh.com")

#center tkinter window
window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())

fr = Frame(window, bg='#EEE')
fr.grid(column=0, row=0, padx=(10, 0), pady=(10, 10), sticky=W)

#(0,0) letter prompt text
lbl = Label(fr, text="Enter Letters:", bg='#EEE', font=(fonty, n))
lbl.pack(side=LEFT)

#(1,0) source folder text box
txt = Entry(fr, width=20, bg='#EEE', font=(fonty, n))
txt.pack(side=LEFT)

#(1,1) output label
lbl1 = Label(window, text="", bg='#EEE', font=(fonty, n))
lbl1.grid(column=0, row=1, padx=(10,0), sticky=W)

fr1 = Frame(window, bg='#EEE')
fr1.grid(column=0, row=2, padx=(10, 0), pady=(10, 0), sticky=W)

#(0,2) submit button
btn = Button(fr1, text="Submit", fg="#FF4500", font=(fonty, n), command=submitbtn)
btn.pack(side=LEFT)

lbl2 = Label(fr1, text=" ", bg='#EEE', font=(fonty, n))
lbl2.pack(side=LEFT)

btn1 = Button(fr1, text="Clear", font=(fonty, n), command=clearbtn)
btn1.pack(side=LEFT)

fr2 = Frame(window, bg='#EEE')
fr2.grid(column=0, row=3, padx=(10, 0), pady=(10, 0), sticky=W)

tag = Label(fr2, text="An original project by", fg='#737373', bg='#EEE', font=(fonty, 10))
tag.pack(side=LEFT)

btn2 = Button(fr2, text="Sahas Ramesh", fg="#FF4500", bd=0, activebackground='#EEE', highlightbackground='#EEE', highlightcolor='#EEE', highlightthickness=0, font=(fonty, 10), command=tagbtn)
btn2.pack(side=LEFT)

window.mainloop()


'''
pyinstaller --onefile --windowed --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' word_finder.py
'''
