from tkinter import *
import tkinter as tk
from tkinter import messagebox
import mysql.connector as mysql
from PIL import Image, ImageTk

import os
wind = Tk()
logo = ImageTk.PhotoImage(file='img.jpg')
wind.title("welcome")
wind.geometry("700x500")
wind.resizable(False, False)
wind.iconphoto(False, logo)
wind.configure(bg='#1b142a')
im = ImageTk.PhotoImage(file='iconn.png')
dashboardImg = ImageTk.PhotoImage(file='dashboard.png')


def tab1():

    lblsecrow = Label(wind, image=im, width=500, bg="#1b142a")
    lblsecrow.place(x=100, y=20)
    Ll6 = Label(wind, text="Email", fg="white", bg="#1b142a", font=("Arial ", 20),
                height=2)
    Ll6.place(x=130, y=180)
    l5 = Label(wind, text="Password", fg="white", bg="#1b142a", font=("Arial ", 20),
               height=2)
    l5.place(x=130, y=230)

    e1_v = StringVar()
    emailInput = Entry(wind, font=("Arial ", 15),
                       width=20, highlightthickness=2, highlightcolor="#5a536d", highlightbackground="#5a536d", bg="#27203d", fg="white")
    emailInput.place(x=310, y=200)
    passwordInput = Entry(wind, show="*", font=("Arial ", 15),
                          width=20, textvariable=e1_v, highlightthickness=2, highlightcolor="#5a536d", highlightbackground="#5a536d", bg="#27203d", fg="white")
    passwordInput.place(x=310, y=250)
    c_v = IntVar(value=0)

    def show():
        if (c_v.get() == 1):
            passwordInput.config(show='')
        else:
            passwordInput.config(show='*')
    ch = Checkbutton(wind, text="show password", command=show,
                     variable=c_v, onvalue=1, offvalue=0, bg="#1b142a", fg="white", activebackground="#1b142a", activeforeground="white")
    ch.place(x=450, y=300)

    def login():
        email = emailInput.get()
        password = passwordInput.get()

        if (email == "" or password == ""):
            messagebox.showinfo("", "Blank Not Allowed")

        elif(email == "admin@gmail.com" and password == "admin"):
            passwordInput.destroy()
            emailInput.destroy()
            l5.destroy()
            Ll6.destroy()
            ch.destroy()
            btn7.destroy()
            lblsecrow.destroy()
            dashboard = Label(wind, image=dashboardImg,
                              width=500, bg="#1b142a")
            dashboard.place(x=100, y=30)

            def edit():
                # show all function
                def showPhones():
                    con = mysql.connect(host="localhost", user="root",
                                        password="", db="phoneshop")
                    cursor = con.cursor()
                    cursor.execute("select * from phones")
                    rows = cursor.fetchall()
                    for row in rows:
                        insertData = str(row[0]) + '             ' + row[1] + '           ' + row[2] + '           ' + \
                            row[3] + '           ' + row[4] + '           ' + \
                            row[5] + '           '+str(row[6])
                        list.insert(list.size()+1, insertData)
                    con.close()

                # insert function
                def insertPhone():
                    Name = nameInput.get()
                    Type = typeInput.get()
                    Storage = storageInput.get()
                    Memory = memoryInput.get()
                    Color = colorInput.get()
                    Price = priceInput.get()
                    if(Name == "" or Type == "" or Storage == "" or Memory == "" or Color == "" or Price == ""):
                        messagebox.showinfo(
                            'Insert Status', 'all fields are required')
                    else:
                        con = mysql.connect(host="localhost", user="root",
                                            password="", db="phoneshop")
                        cursor = con.cursor()
                        cursor.execute("insert into phones values(NULL,'" +
                                       Name + "','" + Type + "' , '"+Storage+"' , '"+Memory+"' , '"+Color+"' , '"+Price+"')")
                        cursor.execute("commit")
                        nameInput.delete(0, 'end')
                        typeInput.delete(0, 'end')
                        storageInput.delete(0, 'end')
                        memoryInput.delete(0, 'end')
                        colorInput.delete(0, 'end')
                        priceInput.delete(0, 'end')
                        messagebox.showinfo(
                            'Insert Status', 'inserted successfully')
                        con.close()
                        wind.after(100, edit)
                        LAll.destroy()
                        l11.destroy()
                        l22.destroy()
                        l33.destroy()
                        l44.destroy()
                        l55.destroy()
                        l66.destroy()
                        l77.destroy()
                        btn66.destroy()
                        btn22.destroy()
                        btn33.destroy()
                        btn44.destroy()
                        btn55.destroy()
                        idInput.destroy()
                        nameInput.destroy()
                        typeInput.destroy()
                        storageInput.destroy()
                        memoryInput.destroy()
                        colorInput.destroy()
                        priceInput.destroy()
                        list.destroy()

                # get one row function
                def getPhone():
                    if(idInput.get() == ""):
                        MessageBox.showinfo(
                            'get Status', 'all fields are required')
                    else:
                        con = mysql.connect(host="localhost", user="root",
                                            password="", db="phoneshop")
                        cursor = con.cursor()
                        cursor.execute(
                            "select * from phones where id='"+idInput.get()+"'")
                        rows = cursor.fetchall()

                        for row in rows:
                            nameInput.delete(0, 'end')
                            typeInput.delete(0, 'end')
                            storageInput.delete(0, 'end')
                            memoryInput.delete(0, 'end')
                            colorInput.delete(0, 'end')
                            priceInput.delete(0, 'end')
                            nameInput.insert(0, row[1])
                            typeInput.insert(0, row[2])
                            storageInput.insert(0, row[3])
                            memoryInput.insert(0, row[4])
                            colorInput.insert(0, row[5])
                            priceInput.insert(0, row[6])
                        idInput.delete(0, 'end')
                        messagebox.showinfo(
                            'get Status', 'get successfully')
                        con.close()
                    

                # delete function
                def deletePhone():
                    if(idInput.get() == ""):
                        messagebox.showinfo(
                            'Delete Status', 'all fields are required')
                    else:
                        con = mysql.connect(host="localhost", user="root",
                                            password="", db="phoneshop")
                        cursor = con.cursor()
                        cursor.execute(
                            "delete from phones where id='"+idInput.get()+"'")
                        cursor.execute("commit")
                        idInput.delete(0, 'end')
                        messagebox.showinfo(
                            'Delete Status', 'deleted successfully')
                        con.close()
                    wind.after(100, edit)
                    LAll.destroy()
                    l11.destroy()
                    l22.destroy()
                    l33.destroy()
                    l44.destroy()
                    l55.destroy()
                    l66.destroy()
                    l77.destroy()
                    btn66.destroy()
                    btn22.destroy()
                    btn33.destroy()
                    btn44.destroy()
                    btn55.destroy()
                    idInput.destroy()
                    nameInput.destroy()
                    typeInput.destroy()
                    storageInput.destroy()
                    memoryInput.destroy()
                    colorInput.destroy()
                    priceInput.destroy()
                    list.destroy()

                # update function
                def updatePhone():
                    Id = idInput.get()
                    Name = nameInput.get()
                    Type = typeInput.get()
                    Storage = storageInput.get()
                    Memory = memoryInput.get()
                    Color = colorInput.get()
                    Price = priceInput.get()
                    if(Id == "" or Name == "" or Type == "" or Storage == "" or Memory == "" or Color == "" or Price == ""):
                        messagebox.showinfo(
                            'update Status', 'all fields are required')
                    else:
                        con = mysql.connect(host="localhost", user="root",
                                            password="", db="phoneshop")
                        cursor = con.cursor()
                        cursor.execute("update phones set name='"+Name +
                                       "' , type='" + Type + "', storage='" + Storage + "', memory='" + Memory + "', color='" + Color + "', price='" + Price + "' where id='"+Id+"'")
                        cursor.execute("commit")
                        idInput.delete(0, 'end')
                        nameInput.delete(0, 'end')
                        typeInput.delete(0, 'end')
                        storageInput.delete(0, 'end')
                        memoryInput.delete(0, 'end')
                        colorInput.delete(0, 'end')
                        priceInput.delete(0, 'end')
                        messagebox.showinfo(
                            'update Status', 'updatef successfully')
                        con.close()
                        wind.after(100, edit)
                        LAll.destroy()
                        l11.destroy()
                        l22.destroy()
                        l33.destroy()
                        l44.destroy()
                        l55.destroy()
                        l66.destroy()
                        l77.destroy()
                        btn66.destroy()
                        btn22.destroy()
                        btn33.destroy()
                        btn44.destroy()
                        btn55.destroy()
                        idInput.destroy()
                        nameInput.destroy()
                        typeInput.destroy()
                        storageInput.destroy()
                        memoryInput.destroy()
                        colorInput.destroy()
                        priceInput.destroy()
                        list.destroy()

                btn9.destroy()
                btn10.destroy()
                btn11.destroy()
                dashboard.destroy()
                LAll = Label(wind, text="Id             Name             Type             Storage             Memory             Color             Price",
                             fg="white", bg="#1b142a", font=("arial", 12))
                LAll.place(x=0, y=0)
                list = Listbox(wind, fg="white", bg="#1b142a",
                               font=("arial", 12))
                list.place(x=0, y=30, width=700, height=40)
                showPhones()
                l11 = Label(wind, text="Id", fg="white", bg="#1b142a",
                            font=("arial", 15))
                l11.place(x=20, y=110)
                l22 = Label(wind, text="Name", fg="white", bg="#1b142a",
                            font=("arial", 15))
                l22.place(x=20, y=150)
                l33 = Label(wind, text="Type", fg="white", bg="#1b142a",
                            font=("arial", 15))
                l33.place(x=20, y=190)
                l44 = Label(wind, text="Storage",
                            fg="white", bg="#1b142a", font=("arial", 15))
                l44.place(x=20, y=230)
                l55 = Label(wind, text="Memory",
                            fg="white", bg="#1b142a", font=("arial", 15))
                l55.place(x=20, y=270)
                l66 = Label(wind, text="Color",
                            fg="white", bg="#1b142a", font=("arial", 15))
                l66.place(x=20, y=310)
                l77 = Label(wind, text="Price",
                            fg="white", bg="#1b142a", font=("arial", 15))
                l77.place(x=20, y=350)
                idInput = Entry(wind, font=("arial", 15),  width=5, highlightthickness=2,
                                highlightcolor="#5a536d", highlightbackground="#5a536d", bg="#27203d", fg="white")
                idInput.place(x=170, y=110)
                nameInput = Entry(wind, font=("arial", 15),  width=20, highlightthickness=2,
                                  highlightcolor="#5a536d", highlightbackground="#5a536d", bg="#27203d", fg="white")
                nameInput.place(x=170, y=150)
                typeInput = Entry(wind, font=("arial", 15), width=20, highlightthickness=2,
                                  highlightcolor="#5a536d", highlightbackground="#5a536d", bg="#27203d", fg="white")
                typeInput.place(x=170, y=190)
                storageInput = Entry(wind, font=("arial", 15),  width=20, highlightthickness=2,
                                     highlightcolor="#5a536d", highlightbackground="#5a536d", bg="#27203d", fg="white")
                storageInput.place(x=170, y=230)
                memoryInput = Entry(wind, font=("arial", 15), width=20, highlightthickness=2,
                                    highlightcolor="#5a536d", highlightbackground="#5a536d", bg="#27203d", fg="white")
                memoryInput.place(x=170, y=270)
                colorInput = Entry(wind, font=("arial", 15),  width=20, highlightthickness=2,
                                   highlightcolor="#5a536d", highlightbackground="#5a536d", bg="#27203d", fg="white")
                colorInput.place(x=170, y=310)
                priceInput = Entry(wind, font=("arial", 15),  width=20, highlightthickness=2,
                                   highlightcolor="#5a536d", highlightbackground="#5a536d", bg="#27203d", fg="white")
                priceInput.place(x=170, y=350)
                btn66 = Button(wind, text="Insert",
                               bg="#27203d", fg="white", width=10, font=("arial", 15), command=insertPhone)
                btn66.place(x=20, y=400)

                btn44 = Button(wind, text="Search",
                               bg="#27203d", fg="white", width=10, font=("arial", 15), command=getPhone)
                btn44.place(x=160, y=400)
                btn22 = Button(wind, text="Update",
                               bg="#27203d", fg="white", width=10, font=("arial", 15), command=updatePhone)
                btn22.place(x=300, y=400)
                btn33 = Button(wind, text="Delete",
                               bg="#27203d", fg="white", width=10, font=("arial", 15), command=deletePhone)
                btn33.place(x=440, y=400)

                def back99():
                    LAll.destroy()
                    l11.destroy()
                    l22.destroy()
                    l33.destroy()
                    l44.destroy()
                    l55.destroy()
                    l66.destroy()
                    l77.destroy()
                    btn66.destroy()
                    btn22.destroy()
                    btn33.destroy()
                    btn44.destroy()
                    btn55.destroy()
                    idInput.destroy()
                    nameInput.destroy()
                    typeInput.destroy()
                    storageInput.destroy()
                    memoryInput.destroy()
                    colorInput.destroy()
                    priceInput.destroy()
                    list.destroy()
                    tab1()
                btn55 = Button(wind, text="Back", bg="#27203d", fg="white", width=10, font=(
                    "arial", 15), command=back99)
                btn55.place(x=570, y=400)
            btn9 = Button(wind, text="Show phone data", font=(
                "arial", 15), bg="#27203d", fg="white", width=18, command=edit)
            btn9.place(x=10, y=320)

            def show():
                # customers hereeeeeeeeeee
                # show all function
                def showCustomers():
                    con = mysql.connect(host="localhost", user="root",
                                        password="", db="phoneshop")
                    cursor = con.cursor()
                    cursor.execute("select * from customers")
                    rows = cursor.fetchall()
                    for row in rows:
                        insertData = str(row[0]) + '             ' + row[1] + '           ' + \
                            row[2] + '           ' + \
                            str(row[3]) + '           ' + row[4]
                        customersList.insert(
                            customersList.size()+1, insertData)
                    con.close()

                # insert function
                def insertCustomer():
                    customerName = nameInputC.get()
                    customerEmail = emailInputC.get()
                    customerPhoneNumber = phoneNumberInputC.get()
                    customerPhoneBought = phoneBoughtInputC.get()
                    if(customerName == "" or customerEmail == "" or customerPhoneNumber == "" or customerPhoneBought == ""):
                        messagebox.showinfo(
                            'Insert Status', 'all fields are required')
                    else:
                        con = mysql.connect(host="localhost", user="root",
                                            password="", db="phoneshop")
                        cursor = con.cursor()
                        cursor.execute("insert into customers values(NULL,'" +
                                       customerName + "','" + customerEmail + "' , '"+customerPhoneNumber+"' , '"+customerPhoneBought+"' )")
                        cursor.execute("commit")
                        nameInputC.delete(0, 'end')
                        emailInputC.delete(0, 'end')
                        phoneNumberInputC.delete(0, 'end')
                        phoneBoughtInputC.delete(0, 'end')
                        messagebox.showinfo(
                            'Insert Status', 'inserted successfully')
                        con.close()
                        wind.after(100, show)
                        customersList.destroy()
                        LAll.destroy()
                        LId.destroy()
                        Ll88.destroy()
                        Ll99.destroy()
                        L200.destroy()
                        L201.destroy()
                        idInputC.destroy()
                        nameInputC.destroy()
                        emailInputC.destroy()
                        phoneNumberInputC.destroy()
                        phoneBoughtInputC.destroy()
                        insertButton.destroy()
                        deleteButton.destroy()
                        updateButton.destroy()
                        searchButton.destroy()
                        bt1.destroy()

                # get one row function

                def getCustomer():
                    if(idInputC.get() == ""):
                        messagebox.showinfo(
                            'get Status', 'all fields are required')
                    else:
                        con = mysql.connect(host="localhost", user="root",
                                            password="", db="phoneshop")
                        cursor = con.cursor()
                        cursor.execute(
                            "select * from customers where id='"+idInputC.get()+"'")
                        rows = cursor.fetchall()
                        for row in rows:
                            nameInputC.insert(0, row[1])
                            emailInputC.insert(0, row[2])
                            phoneNumberInputC.insert(0, row[3])
                            phoneBoughtInputC.insert(0, row[4])
                        idInputC.delete(0, 'end')
                        messagebox.showinfo(
                            'get Status', 'get successfully')
                        con.close()

                # delete function
                def deleteCustomer():
                    if(idInputC.get() == ""):
                        messagebox.showinfo(
                            'Delete Status', 'all fields are required')
                    else:
                        con = mysql.connect(host="localhost", user="root",
                                            password="", db="phoneshop")
                        cursor = con.cursor()
                        cursor.execute(
                            "delete from customers where id='"+idInputC.get()+"'")
                        cursor.execute("commit")
                        idInputC.delete(0, 'end')
                        messagebox.showinfo(
                            'Delete Status', 'deleted successfully')
                        con.close()
                    wind.after(100, show)
                    customersList.destroy()
                    LAll.destroy()
                    LId.destroy()
                    Ll88.destroy()
                    Ll99.destroy()
                    L200.destroy()
                    L201.destroy()
                    idInputC.destroy()
                    nameInputC.destroy()
                    emailInputC.destroy()
                    phoneNumberInputC.destroy()
                    phoneBoughtInputC.destroy()
                    insertButton.destroy()
                    deleteButton.destroy()
                    updateButton.destroy()
                    searchButton.destroy()
                    bt1.destroy()

                # update function
                def updateCustomer():
                    customerId = idInputC.get()
                    customerName = nameInputC.get()
                    customerEmail = emailInputC.get()
                    customerPhoneNumber = phoneNumberInputC.get()
                    customerPhoneBought = phoneBoughtInputC.get()
                    if(customerId == "" or customerName == "" or customerEmail == "" or customerPhoneNumber == "" or customerPhoneBought == ""):
                        messagebox.showinfo(
                            'update Status', 'all fields are required')
                    else:
                        con = mysql.connect(host="localhost", user="root",
                                            password="", db="phoneshop")
                        cursor = con.cursor()
                        cursor.execute("update customers set name='"+customerName +
                                       "' , email='" + customerEmail + "', phone_number='" + customerPhoneNumber + "', phone_bought='" + customerPhoneBought + "' where id='"+customerId+"'")
                        cursor.execute("commit")
                        idInputC.delete(0, 'end')
                        nameInputC.delete(0, 'end')
                        emailInputC.delete(0, 'end')
                        phoneNumberInputC.delete(0, 'end')
                        phoneBoughtInputC.delete(0, 'end')
                        messagebox.showinfo(
                            'update Status', 'updatef successfully')
                        con.close()
                    wind.after(100, show)
                    customersList.destroy()
                    LAll.destroy()
                    LId.destroy()
                    Ll88.destroy()
                    Ll99.destroy()
                    L200.destroy()
                    L201.destroy()
                    idInputC.destroy()
                    nameInputC.destroy()
                    emailInputC.destroy()
                    phoneNumberInputC.destroy()
                    phoneBoughtInputC.destroy()
                    insertButton.destroy()
                    deleteButton.destroy()
                    updateButton.destroy()
                    searchButton.destroy()
                    bt1.destroy()

                btn9.destroy()
                btn10.destroy()
                btn11.destroy()
                dashboard.destroy()
                customersList = Listbox(
                    wind, bg="#1b142a", fg="white", font=("arial", 12))
                customersList.place(x=0, y=30, width=700, height=40)
                showCustomers()
                LAll = Label(wind, text="Id             Customer Name             Email             Phone Number             Phone Bought",
                             fg="white", bg="#1b142a", font=("arial", 12))
                LAll.place(x=0, y=0)
                LId = Label(wind, text="Id",
                            fg="white", bg="#1b142a", font=("arial", 15))
                LId.place(x=80, y=110)
                Ll88 = Label(wind, text="Customer Name",
                             fg="white", bg="#1b142a", font=("arial", 15))
                Ll88.place(x=80, y=150)
                Ll99 = Label(wind, text="Email",
                             fg="white", bg="#1b142a", font=("arial", 15))
                Ll99.place(x=80, y=190)
                L200 = Label(wind, text="Phone Numer",
                             fg="white", bg="#1b142a", font=("arial", 15))
                L200.place(x=80, y=230)
                L201 = Label(wind, text="Phone Bought",
                             fg="white", bg="#1b142a", font=("arial", 15))
                L201.place(x=80, y=270)
                idInputC = Entry(
                    wind, font=("Arial ", 15),  width=5, highlightthickness=2, highlightcolor="#5a536d", highlightbackground="#5a536d", bg="#27203d", fg="white")
                nameInputC = Entry(
                    wind, font=("Arial ", 15), width=20, highlightthickness=2, highlightcolor="#5a536d", highlightbackground="#5a536d", bg="#27203d", fg="white")
                emailInputC = Entry(
                    wind,  font=("Arial ", 15),  width=20, highlightthickness=2, highlightcolor="#5a536d", highlightbackground="#5a536d", bg="#27203d", fg="white")
                phoneNumberInputC = Entry(
                    wind,  font=("Arial ", 15),  width=20, highlightthickness=2, highlightcolor="#5a536d", highlightbackground="#5a536d", bg="#27203d", fg="white")
                phoneBoughtInputC = Entry(
                    wind, font=("Arial ", 15),  width=20, highlightthickness=2, highlightcolor="#5a536d", highlightbackground="#5a536d", bg="#27203d", fg="white")
                idInputC.place(x=280, y=110)
                nameInputC.place(x=280, y=150)
                emailInputC.place(x=280, y=190)
                phoneNumberInputC.place(x=280, y=230)
                phoneBoughtInputC.place(x=280, y=270)

                insertButton = Button(wind, text="Insert", bg="#27203d", fg="white", width=10, font=(
                    "arial", 15), command=insertCustomer)
                insertButton.place(x=20, y=400)
                deleteButton = Button(wind, text="Delete", bg="#27203d", fg="white", width=10, font=(
                    "arial", 15), command=deleteCustomer)
                deleteButton.place(x=160, y=400)
                updateButton = Button(wind, text="Update", bg="#27203d", fg="white", width=10, font=(
                    "arial", 15), command=updateCustomer)
                updateButton.place(x=300, y=400)
                searchButton = Button(wind, text="Search", bg="#27203d", fg="white", width=10, font=(
                    "arial", 15), command=getCustomer)
                searchButton.place(x=440, y=400)

                def back88():
                    customersList.destroy()
                    LAll.destroy()
                    LId.destroy()
                    Ll88.destroy()
                    Ll99.destroy()
                    L200.destroy()
                    L201.destroy()
                    idInputC.destroy()
                    nameInputC.destroy()
                    emailInputC.destroy()
                    phoneNumberInputC.destroy()
                    phoneBoughtInputC.destroy()
                    insertButton.destroy()
                    deleteButton.destroy()
                    updateButton.destroy()
                    searchButton.destroy()
                    bt1.destroy()
                    tab1()

                bt1 = Button(wind, text="Back", bg="#27203d", fg="white", width=10, font=(
                    "arial", 15), command=back88)
                bt1.place(x=570, y=400)
            btn10 = Button(wind, text="Show customer data", font=(
                "arial", 15), bg="#27203d", width=18, fg="white", command=show)
            btn10.place(x=240, y=320)

            def back5():
                btn9.destroy()
                btn10.destroy()
                btn11.destroy()
                dashboard.destroy()
                tab1()
            btn11 = Button(wind, text="Back", font=(
                "arial", 15), bg="#27203d", width=18, fg="white", command=back5)
            btn11.place(x=480, y=320)

        else:
            messagebox.showinfo("", "incorrect email or incorrect password")
    btn7 = Button(wind, font=("Arial ", 15), bg="#27203d", fg="white", width=20,
                  text="Login", command=login)
    btn7.place(x=220, y=370)


def tab2():
    def tab3():
        e1.destroy()
        e2.destroy()
        l0.destroy()
        l2.destroy()
        l3.destroy()
        btn3.destroy()
        btn4.destroy()

        def back2():
            btn5.destroy()
            btn6.destroy()
            l4.destroy()
            e3.destroy()
            tab2()

    l1.destroy()
    f1.destroy()
    btn1.destroy()

    def back():
        e1.destroy()
        e2.destroy()
        l0.destroy()
        l2.destroy()
        l3.destroy()
        btn3.destroy()
        btn4.destroy()
        tab1()

    def sub():
        phone = e1.get()
        us_name = e2.get()
        if phone == "" and us_name == "":
            messagebox.showinfo("", "Blank Not Allowed")
        else:
            tab3()

    btn3 = Button(wind, text="Submit", background="brown", fg="black", font=("Arial ", 15),
                  activebackground="black", command=sub)
    btn3.place(x=200, y=300,)
    btn4 = Button(wind, text="Back", background="brown", fg="black", font=("Arial ", 15),
                  activebackground="black", command=back)
    btn4.place(x=390, y=340)


tab1()
wind.mainloop()
    