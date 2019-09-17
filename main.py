from tkinter import *
from tkinter import messagebox as mb
from add2db import main
from add2db import delete
import csv
import announce




def addTrain():


    def addFunc():
        main(tno_entry.get(), tname_entry.get(), from_entry.get(), to_entry.get(), pno_entry.get())
        add.destroy()



    add = Toplevel()
    add.geometry('300x400')
    add.resizable(0,0)
    add.title("Add Train")


    Label(add, text= 'Add Train', width=200, height=1, bg= 'teal', fg='white', font=('Cambria', 11),relief = 'groove' ).pack()

    Label(add, text='').pack()

    Label(add, text='Train No. ', font=('Cambria', 11) ).pack()

    tno_entry = Entry(add, font=('Cambria', 11))
    tno_entry.pack()


    Label(add, text='').pack()

    Label(add, text='Train Name ', font=('Cambria', 11) ).pack()

    tname_entry = Entry(add, font=('Cambria', 11))
    tname_entry.pack()


    Label(add, text='').pack()

    Label(add, text='From ', font=('Cambria', 11) ).pack()

    from_entry = Entry(add, font=('Cambria', 11))
    from_entry.pack()


    Label(add, text='').pack()

    Label(add, text='To ', font=('Cambria', 11) ).pack()

    to_entry = Entry(add, font=('Cambria', 11))
    to_entry.pack()


    Label(add, text='').pack()

    Label(add, text='Platform No. ', font=('Cambria', 11) ).pack()

    pno_entry = Entry(add, font=('Cambria', 11), width=2)
    pno_entry.pack()


    Label(add, text='').pack()

    Button(add, text='Add Train', font=('Cambria', 13), command=addFunc).pack()


    add.mainloop()





def deleteTrain():

    res = mb.askyesno('Delete Train','Are You Sure ? Do You Want To Delete The Selected Train.\n\nWarning:-Train Details Will Also Be Deleted From The Database ')
    if res:
        sr = int(trains_listbox.get(ACTIVE).split('        ')[0])
        delete(str(sr))
        print('deleted')
    else:
        print('not deleted')



def editTrain():

    edit = Toplevel()
    edit.geometry('300x400')
    edit.resizable(0,0)
    edit.title("Edit Train")


    Label(edit, text= 'edit Train', width=200, height=1, bg= 'teal', fg='white', font=('Cambria', 11),relief = 'groove' ).pack()

    Label(edit, text='').pack()

    Label(edit, text='Train No. ', font=('Cambria', 11) ).pack()

    tno_entry = Entry(edit, font=('Cambria', 11), text='Hello')
    tno_entry.pack()


    Label(edit, text='').pack()

    Label(edit, text='Train Name ', font=('Cambria', 11) ).pack()

    tname_entry = Entry(edit, font=('Cambria', 11))
    tname_entry.pack()


    Label(edit, text='').pack()

    Label(edit, text='From ', font=('Cambria', 11) ).pack()

    from_entry = Entry(edit, font=('Cambria', 11))
    from_entry.pack()


    Label(edit, text='').pack()

    Label(edit, text='To ', font=('Cambria', 11) ).pack()

    to_entry = Entry(edit, font=('Cambria', 11))
    to_entry.pack()


    Label(edit, text='').pack()

    Label(edit, text='Platform No. ', font=('Cambria', 11) ).pack()

    pno_entry = Entry(edit, font=('Cambria', 11), width=2)
    pno_entry.pack()


    Label(edit, text='').pack()

    Button(edit, text='edit Train', font=('Cambria', 13)).pack()


    edit.mainloop()






def add2list():
    with open('db.csv','r') as readFile:
        reader = csv.reader(readFile)
        trainsList = list(reader)

    l = 'Sr No.' + '    ' + 'Train No.' + '      ' + 'Train Name' 
    trains_listbox.insert(END, l)

    for i in trainsList:
        print(i)
        l = '  '+i[0]+(' '*8) + i[1] + (' '*5) + i[2]
        trains_listbox.insert(END , l)



def refresh():
    trains_listbox.delete(0,END)
    add2list()


def announceTrain():
    sr = int(trains_listbox.get(ACTIVE).split('        ')[0])
    input_ = open('db.csv','r',newline='')
    for row in csv.reader(input_):
        if row[0] == str(sr):
            announce.main(row[1], row[2], row[3], row[4], row[5])





    

win = Tk()
win.geometry('700x380')
win.title('DeeRail - Announcing System')
win.resizable(0,0)

Label(win, text= 'DeeRail-Announcing System', width=700, height=1, bg= 'teal', fg='white', font=('Cambria', 12),relief = 'groove' ).pack()

Label(win, text='Select The Train In ListBox To Perform Any Action', font = ('Cambria', 10)).place(x=10, y=35)

trains_listbox = Listbox(win, height=10, width=62, font=('Cambria', 14))
trains_listbox.place(x=10, y=60)

Button(win, text=' + Add New Train', font=('Cambria', 13), command = addTrain).place(x=10, y=315)

delete_img = PhotoImage(file='resources/images/delete1.png')

Button(win,image=delete_img, command=deleteTrain ,text=' Delete Train',compound='left', font=('Cambria', 13)).place(x=160, y=315)


edit_img = PhotoImage(file='resources/images/edit.png')

Button(win,image=edit_img, command=editTrain ,text=' Edit Train',compound='left', font=('Cambria', 13)).place(x=300, y=315)


refresh_img = PhotoImage(file='resources/images/refresh.png')

Button(win,image=refresh_img,text=' Refresh',compound='left', font=('Cambria', 13), command = refresh).place(x=430, y=315)



announce_img = PhotoImage(file='resources/images/announce1.png')

Button(win,image=announce_img, command=announceTrain ,text=' Announce',compound='left', font=('Cambria', 13)).place(x=550, y=315)



add2list()

win.mainloop()