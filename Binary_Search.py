from tkinter import *
import tkinter as tk


# create a window
window = Tk()

# set size of window
window.geometry("700x350")

# create Title
window.title("MyFirstProject")

# create heading
head = Label(window, text="Binary Search", font=('Calibri 15'))
#shove heading to window
head.pack(pady=20)
Label(window, text="Enter a Sorted List", font=('Calibri')).pack()

# Main Function

n = tk.IntVar()
e = tk.StringVar()

def binary_search():
    l = e.get().split(" ")

    for i in range(0, len(l)):
        l[i] = int(l[i])

    num = (n.get())
    first = 0
    last = len(l) - 1
    found = False

    while (first <= last and not found):
        mid = (first + last) // 2
        if (l[mid] == num):
            found = True
        else:
            if num < l[mid]:
                last = mid - 1
            else:
                first = mid + 1

    if found == True:
        Label(window, text="Number found in the list", font=('Calibri')).place(x=280,y=200)
    else:
        Label(window, text="Number NOT found in the list", font=('Calibri')).place(x=270,y=250)


Entry(window,textvariable=e).pack()

Label(window,text='Enter number you want to search').pack()

Entry(window,textvariable=n).pack()

Button(window, text="Search", command=binary_search).pack()



window.mainloop()


