from ShowStaff import *
import os
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
import sqlite3

from CRUDSQL import *


class AddForm(object):
    def __init__(self):
        self.AddForm = Tk()
        self.AddForm.title = 'Edit'
        w = 1000
        h = 550
        ws = self.AddForm.winfo_screenwidth()
        hs = self.AddForm.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.AddForm.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.AddForm.configure(bg = '#dff9fb')
        self.AddForm.resizable(FALSE, FALSE)
        self.id = IntVar(self.AddForm)
        self.name = StringVar(self.AddForm)
        self.birthyear = IntVar(self.AddForm)
        self.gender = StringVar(self.AddForm)
        self.rank = StringVar(self.AddForm)
        self.salary = IntVar(self.AddForm)
        self.sift = StringVar(self.AddForm)
        self.bonus = IntVar(self.AddForm)
        self.count = IntVar(self.AddForm)
        self.crud = CRUD()
        self.form = ShowForm()
#========================Gui form===============================

    def guiForm(self):
        self.labelContent()
        self.labelID()
        self.labelNVname()
        self.labelnamSinh()
        self.labelSex()
        self.labelchucVu()
        self.labelluongCoBan()
        self.labelcaLamViec()
        self.labelThuong()
        self.labeldiemDanh()
        self.entryID()
        self.entryNVname()
        self.labelnamSinh()
        self.entrynamSinh()
        self.entrySex()
        self.entrychucVu()
        self.entryluongCoBan()
        self.entrycaLamViec()
        self.entryThuong()
        self.entrydiemDanh()
        #self.buttonEdit()
        #self.buttonRemove()
        self.buttonADD()
        #self.buttonShow()
        self.AddForm.mainloop()
#==================================================================================

#===============================Lable Form==============================================
    def labelContent(self):
        lb_Content = tk.Label(
            self.AddForm,
            text = 'Phi???u th??m nh??n vi??n',
            font = ('Times', 25, 'bold', 'italic'),
            fg = 'Black',
            bg = '#dff9fb'
            )
        lb_Content.place(x=300,y=20)
#=================================================================

#=============================label ID============================
    def labelID(self):
        lb_ID = tk.Label(
            self.AddForm,
            text = 'ID Nh??n Vi??n: ',
            font = 'Times 15 bold',
            bg = '#dff9fb')
        lb_ID.place(x=60,y=110)
#==============================================================

#===================================label NVname===============
    def labelNVname(self):
        lb_NVname = tk.Label(
            self.AddForm,
            text = 'T??n nh??n vi??n: ',
            font = 'Times 15 bold',
            bg = '#dff9fb')
        lb_NVname.place(x=60,y=180)
#===========================End label NVname=========================

    #label n??m sinh
    def labelnamSinh(self):
        lb_namSinh = tk.Label(
            self.AddForm,
            text = 'N??m sinh: ',
            font = 'Times 15 bold',
            bg = '#dff9fb')
        lb_namSinh.place(x=60,y=250)
    #End label gi???i t??nh

    #label gi???i t??nh
    def labelSex(self):
        lb_Sex = tk.Label(
            self.AddForm,
            text = 'Gi???i t??nh: ',
            font = 'Times 15 bold',
            bg = '#dff9fb')
        lb_Sex.place(x=60,y=320)
    #End label gi???i t??nh

    #label ch???c v???
    def labelchucVu(self):
        lb_chucVu = tk.Label(
            self.AddForm,
            text = 'Ch???c v???: ',
            font = 'Times 15 bold',
            bg = '#dff9fb')
        lb_chucVu.place(x=60,y=390)
    #End label gi???i t??nh

    #label l????ng c?? b???n
    def labelluongCoBan(self):
        lb_luongCoBan = tk.Label(
            self.AddForm,
            text = 'L????ng c?? b???n: ',
            font = 'Times 15 bold',
            bg = '#dff9fb')
        lb_luongCoBan.place(x=550,y=125)
    #End label l????ng c?? b???n

    #label ca l??m vi???c
    def labelcaLamViec(self):
        lb_caLamViec = tk.Label(
            self.AddForm,
            text = 'Ca l??m vi???c: ',
            font = 'Times 15 bold',
            bg = '#dff9fb')
        lb_caLamViec.place(x=550,y=205)
    #End label ca l??m vi???c

    #label th?????ng
    def labelThuong(self):
        lb_Thuong = tk.Label(
            self.AddForm,
            text = 'Th?????ng: ',
            font = 'Times 15 bold',
            bg = '#dff9fb')
        lb_Thuong.place(x=550,y=285)
    #End label th?????ng

    #label ??i???m danh
    def labeldiemDanh(self):
        lb_diemDanh = tk.Label(
            self.AddForm,
            text = '??i???m danh: ',
            font = 'Times 15 bold',
            bg = '#dff9fb')
        lb_diemDanh.place(x=550,y=365)
    #End label ??i???m danh

    #tk.Entry ID
    def entryID(self):
        self.et_ID = tk.Entry(
            self.AddForm,
            font = 'Times 15',
            bg = '#aaa69d',
            textvariable = self.id)
        self.et_ID.place(x=220,y = 110)
    #End tk.Entry ID

    #tk.Entry NVname
    def entryNVname(self):
        self.et_NVname = tk.Entry(
            self.AddForm,
            font = 'Times 15',
            bg = '#aaa69d',
            textvariable = self.name)
        self.et_NVname.place(x=220,y = 180)
    #End tk.Entry NVname

    #tk.Entry n??m sinh
    def entrynamSinh(self):
        self.et_namSinh = tk.Entry(
            self.AddForm,
            font = 'Times 15',
            bg = '#aaa69d',
            textvariable = self.birthyear)
        self.et_namSinh.place(x=220,y = 250)
    #End tk.Entry n??m sinh

    #tk.Entry sex
    def entrySex(self):
        OPTIONS = [
                    "Ch???n gi???i t??nh",
                    "N???",
                    "Nam"
                    ]
        variable = StringVar(self.AddForm)
        variable.set("Ch???n gi???i t??nh")
        self.et_Sex = OptionMenu(self.AddForm, variable, *OPTIONS,command = self.SetGender)
        self.et_Sex.place(x=220,y = 320)
    #End tk.Entry sex

    #tk.Entry ch???c v???
    def entrychucVu(self):
        OPTIONS = [
                    "Ch???n ch???c v???",
                    "Qu???n L??",
                    "T??? tr?????ng",
                    "Pha ch???",
                    "Qu??t d???n",
                    "R???a Ly",
                    "B???o v???",
                    "Xu??t nh???p kho",
                    "Thu ng??n",
                    ]
        variable = StringVar(self.AddForm)
        variable.set("Choose Sort")
        self.et_chucVu = OptionMenu(self.AddForm, variable, *OPTIONS,command = self.SetRank)
        self.et_chucVu.place(x=220,y = 390)
    #End tk.Entry ch???c v???

    #tk.Entry l????ng c?? b???n
    def entryluongCoBan(self):
        self.et_luongCoBan = tk.Entry(
            self.AddForm,
            font = 'Times 15',
            bg = '#aaa69d',
            textvariable = self.salary)
        self.et_luongCoBan.place(x=710,y = 125)
    #End tk.Entry l????ng c?? b???n

    #tk.Entry ca l??m vi???c
    def entrycaLamViec(self):
        self.et_caLamViec = tk.Entry(
            self.AddForm,
            font = 'Times 15',
            bg = '#aaa69d',
            textvariable = self.sift)
        self.et_caLamViec.place(x=710,y = 205)
    #End tk.Entry ca l??m vi???c

    #Entry th?????ng
    def entryThuong(self):
        self.et_Thuong = tk.Entry(
            self.AddForm,
            font = 'Times 15',
            bg = '#aaa69d',
            textvariable = self.bonus)
        self.et_Thuong.place(x=710,y = 285)
    #End tk.Entry th?????ng

    #tk.Entry ??i???m danh
    def entrydiemDanh(self):
        self.et_diemDanh = tk.Entry(
            self.AddForm,
            font = 'Times 15',
            bg = '#aaa69d',
            textvariable = self.count)
        self.et_diemDanh.place(x=710,y = 365)
    #End tk.Entry ??i???m danh

    #Button ADD
    def buttonADD(self):
        btn_ADD = tk.Button(
            self.AddForm,
            text = 'Th??m',
            font = 'Heveltica 10 bold',
            width = 15,
            command = self.Add
            )
        btn_ADD.place(x=400, y = 465)
    #End tk.Button ADD

    #End Button Show
    #Command

    def Add(self):
        if (self.checkTT() == True):
            if(self.checkGioiTinh() == True):
                if(self.checkIDNhanVien() == True):
                    self.crud.AddStaff(self.id.get(),self.name.get(),self.birthyear.get(),self.gender.get(),self.rank.get(),self.salary.get(),self.sift.get(),self.bonus.get(),self.count.get())
                    messagebox.showinfo("Add Nh??n Vi??n", "Th??m nh??n vi??n th??nh c??ng")
                else:
                     messagebox.showerror("Add Nh??n Vi??n", "L???i: ID nh??n vi??n ???? t???n t???i")
            else:
                messagebox.showerror("Add Nh??n Vi??n", "L???i: Gi???i t??nh ch??? ch???p nh???n 'Nam' hoac 'N???' ")
        else:
            messagebox.showerror("Add Nh??n Vi??n", "Kh??ng ???????c ????? tr??ng c??c m???c")



    def Show(self):
        self.form.display()
        self.form.MainShow()
    #command
#=========================verif====================================
    def checkIDNhanVien(self):
        listID = self.crud.getIDNhanVien()
        if(self.id.get() in listID):
            return False
        else:
            return True

    def checkTT(self):
        print(self.id.get() == 0, self.name.get() == "" , self.birthyear.get() == 0 , self.rank.get() == "" , self.salary.get() == 0 , self.sift.get() == "")
        if(self.id.get() == 0 or self.name.get() == "" or self.birthyear.get() == 0 or self.rank.get() == "" or self.salary.get() == 0 or self.sift.get() == ""):
            return False
        else:
            return True

    def checkGioiTinh(self):
        if(self.gender.get() != "Nam" and self.gender.get() != "N???"):
            return False
        else:
            return True
#=======================function===========================================
    def SetGender(self,value):
        self.gender.set(value)
        print(self.gender.get())
    def SetRank(self,value):
        self.rank.set(value)
        print(self.rank.get())
   
#==================================================================