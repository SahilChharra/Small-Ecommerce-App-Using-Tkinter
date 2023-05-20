from pymongo import MongoClient
from random import randint
from tkinter import *
import tkinter.messagebox as tkMessageBox
import tkinter.ttk as ttk
from tkinter import Button
import sys
import customtkinter

try:
	client = MongoClient(port=27017)
	db=client.EcomCatalog
	print("Connected to MongoDB")
except :
	print("Database connection Error ")
	print("No connection could be made because the target machine actively refused it ")
	tkMessageBox.showerror("Error", "Connection Error")
	sys.exit(1)
	
root=Tk()
root.geometry('400x400')
root.title("E-Commerce Catalog")

def add_Products(root,db): 
    def add_query():
        global root
        pname = E1.get()
        cat = E2.get()
        pr = int(E3.get())
        st = E4.get()
        sname = E5.get()
        Product_Name = [pname]
        Category = [cat]
        Price = [pr]
        Stock = [st]
        Seller_Name = [sname]
        Ecom_Catalog = {
        'Product Name' : Product_Name[randint(0, (len(Product_Name)-1))],
        'Category' : Category[randint(0, (len(Category)-1))],
        'Price' : Price[randint(0, (len(Price)-1))],
        'Stock' : Stock[randint(0, (len(Stock)-1))],
        'Seller Name' : Seller_Name[randint(0, (len(Seller_Name)-1))],
        }
        
        if(len(pname)==0 or len(cat)==0 or len(pr)==0 or len(sname)==0 or len(st)==0 or len(sname)==0):
            tkMessageBox.showwarning("WARNING", "All fields are compulsory")
            return
        if len(sname)!=0 and db.Products.count_documents({ 'Product Name': pname }, limit = 1)==0:
            result=db.Products.insert_one(Ecom_Catalog)
        else:
            tkMessageBox.showwarning("ERROR", "PRODUCT Already Exists")
            return
       	
        newwin.destroy()
        tkMessageBox.showinfo("Add Product", "Product Added")
    newwin = Toplevel(root)
    newwin.geometry('400x400')
    newwin.title("Add Products")
    L1 = Label(newwin, text="Product Name")
    L1.place(x=10,y=50)
    E1 = Entry(newwin, bd=7)
    E1.place(x=100,y=50)
    L2 = Label(newwin, text="Category")
    L2.place(x=10,y=100)
    E2 = Entry(newwin, bd=7)
    E2.place(x=100,y=100)
    L3 = Label(newwin, text="Price")
    L3.place(x=10,y=150)
    E3 = Entry(newwin, bd=7)
    E3.place(x=100,y=150)
    L4 = Label(newwin, text="Stock")
    L4.place(x=10,y=200)
    E4 = Entry(newwin, bd=7)
    E4.place(x=100,y=200)
    L5 = Label(newwin, text="Seller Name")
    L5.place(x=10,y=250)
    E5 = Entry(newwin, bd=7)
    E5.place(x=100,y=250)
    sub=Button(newwin,text="Submit",command=add_query)
    sub.place(x=120,y=350)

def del_data(root,db):
    def delete():
        global root
        pname = E1.get()
        if(len(pname)==0):
            tkMessageBox.showwarning("WARNING", "Enter a Existing Product Name")
            return
        if db.Products.count_documents({ 'Product Name': pname }, limit = 1)==0:
            tkMessageBox.showwarning("ERROR", "Product Does Not Exist")
            return
        else:
            db.Products.delete_one({'Product Name':pname})    
        newwin.destroy()
        tkMessageBox.showinfo("Delete Product", "Product Deleted")
    newwin=Toplevel(root)
    newwin.geometry('400x350')
    newwin.title("Delete Product")
    L1 = Label(newwin, text="Product Name")
    L1.place(x=10, y=50)
    E1 = Entry(newwin,bd=5)
    E1.place(x=100, y=50)
    sub = Button(newwin, text="Delete Entry", command=delete)
    sub.place(x=120, y=200)

def update_data(root,db):
	def UPDD():
		global root
		pname = E7.get()
		cat = E8.get()
		Price = E9.get()
		Stock = E10.get()
		sname = E11.get()
		if(len(pname)==0):
			tkMessageBox.showwarning("WARNING", "Enter a Valid Product")
			return

		if db.Products.count_documents({ 'Product Name': pname }, limit = 1)==0:
			tkMessageBox.showwarning("ERROR", "PRODUCT Does Not Exist")
			return
		if(len(cat)!=0):
			db.Products.update_one({"pname":pname},{"$set": {'Category' : cat}})
		if(len(Price)!=0):
			db.Products.update_one({"pname":pname},{"$set": {'Price' : Price}})
		if(len(Stock)!=0):
			db.Products.update_one({"pname":pname},{"$set": {'Stock' : Stock}})
		if(len(sname)!=0):
			db.Products.update_one({"pname":pname},{"$set": {'Seller Name' : sname}})
            
		newwin.destroy()
		tkMessageBox.showinfo("Update Product", "Product Updated")

	newwin = Toplevel(root)
	newwin.geometry('400x400')
	newwin.title("Update Products")
	
	L7 = Label(newwin, text="Product Name")
	L7.place(x=10,y=50)
	E7 = Entry(newwin, bd=7)
	E7.place(x=100,y=50)
	L8 = Label(newwin, text="Category")
	L8.place(x=10,y=100)
	E8 = Entry(newwin, bd=7)
	E8.place(x=100,y=100)
	L9 = Label(newwin, text="Price")
	L9.place(x=10,y=150)
	E9 = Entry(newwin, bd=7)
	E9.place(x=100,y=150)
	L10 = Label(newwin, text="Stock")
	L10.place(x=10,y=200)
	E10 = Entry(newwin, bd=7)
	E10.place(x=100,y=200)
	L11 = Label(newwin, text="Seller Name")
	L11.place(x=10,y=250)
	E11 = Entry(newwin, bd=7)
	E11.place(x=100,y=250)
	sub=Button(newwin,text="Submit",command=UPDD)
	sub.place(x=120,y=350)


def display(root,db):
	newwin=Toplevel(root)
	newwin.geometry('400x500')
	newwin.title("Product Details")
	L1=Label(newwin,text="Product Name")
	L1.grid(row=0,column=0)
	L2 = Label(newwin, text="Category")
	L2.grid(row=0, column=2)
	L3=Label(newwin,text="Price")
	L3.grid(row=0,column=4)
	L4=Label(newwin,text="Stock")
	L4.grid(row=0,column=6)
	L5=Label(newwin,text="Seller Name")
	L5.grid(row=0,column=8)
	i=1
	for x in db.Products.find():
		y=len(x)
		L1 = Label(newwin, text=x['Product Name'])
		L1.grid(row=i, column=0)
		L2 = Label(newwin, text=x['Category'])
		L2.grid(row=i, column=2)
		L3 = Label(newwin, text=x['Price'])
		L3.grid(row=i, column=4)
		L4 = Label(newwin, text=x['Stock'])
		L4.grid(row=i, column=6)
		L5 = Label(newwin, text=x['Seller Name'])
		L5.grid(row=i, column=8)
		i+=1

def newDisplay(root,db):
    newwin2=Toplevel(root)
    newwin2.geometry('400x500')
    newwin2.title('Product Details')
    L12=customtkinter.CTkLabel(newwin2,text='Search for Product')
    L12.grid(row=0,column=0)
    global L13
    L13=customtkinter.CTkComboBox(newwin2,values=['Product Name','Category','Price','Stock','Seller Name'])
    L13.grid(row=0,column=1)
    L1=Label(newwin2,text="Product Name")
    L1.grid(row=2,column=0)
    L2 = Label(newwin2, text="Category")
    L2.grid(row=2, column=2)
    L3=Label(newwin2,text="Price")
    L3.grid(row=2,column=4)
    L4=Label(newwin2,text="Stock")
    L4.grid(row=2,column=6)
    L5=Label(newwin2,text="Seller Name")
    L5.grid(row=2,column=8)
    B21=Button(newwin2,text='Search',command=lambda:Sort(newwin2,db))
    B21.grid(row=0,column=2)
    
def Sort(newwin2,db):
    par=L13.get()
    Mydoc=db.Products.find().sort(par)
    i=3
    for x in Mydoc:
        y=len(x)
        L1 = Label(newwin2, text=x['Product Name'])
        L1.grid(row=i, column=0)
        L2 = Label(newwin2, text=x['Category'])
        L2.grid(row=i, column=2)
        L3 = Label(newwin2, text=x['Price'])
        L3.grid(row=i, column=4)
        L4 = Label(newwin2, text=x['Stock'])
        L4.grid(row=i, column=6)
        L5 = Label(newwin2, text=x['Seller Name'])
        L5.grid(row=i, column=8)
        i+=1 
        
def search_item():
    sitem=s1.get()
    
        
def Search(newwin2,db):
    swin=Toplevel(root)
    swin.geometry('400x400')
    swin.title('Search')
    global s1
    s1=Entry(swin)
    s1.grid(row=0,column=0)
    sbtn=Button(swin,text="Search",command=search_item)
    sbtn.grid(row=0,column=1)
            

add= Button(root,text='Add New Product',command=lambda:add_Products(root,db))
delete= Button(root,text='Delete Product Entry',command=lambda:del_data(root,db))
update= Button(root,text='Update Product Info',command=lambda:update_data(root,db))
show= Button(root,text='Show Product Details',command=lambda:display(root,db))
searchBut = Button(root,text='Sort for Product',command=lambda:newDisplay(root,db))
add.place(x=100,y=100)
delete.place(x=100,y=150)
update.place(x=100,y=200)
show.place(x=100,y=250)
searchBut.place(x=100,y=300)
root.mainloop()