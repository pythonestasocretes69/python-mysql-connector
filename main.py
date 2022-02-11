#medicine stock managers       

import mysql.connector as sqlator
import random
def stop() :                                                                                           #temporary function
    print('work in progress')
def Cprint():                                                                                         #print from cursor
    print(cursor.fetchall())
def c_add():                                                                                         # input statement for customers (name = c_add)
    Name = input("enter name:  ")
    Phno = input(" enter phno:  ")
    Credit = 0
    Q = random.randrange(100000,1000000)
    Customerkey = Q
    tuples=(Customerkey, Name, Phno, Credit)
    return (tuples)

def s_add():                                                                                         # input statement for suppliers (name = s_add)
    Name = input("enter name(10 characters):  ")
    Phno = input(" enter phno:  ")
    Amount_due = 0
    Q = random.randrange(100000,1000000)
    Suppkey = Q
    tuples=(Suppkey, Name, Phno, Amount_due)
    return (tuples)
def check_product(key):                                                                      # check if there is a product
    cursor.execute('select * from products where product_key = {}'.format(key))
    lists = cursor.fetchall()
    ans = False
    for i  in lists:
        ans = True
        print (lists,'are following products') 
    mycon.commit()
    return(ans)

def check_batch(key):                                                                      # check if there is a batch
    cursor.execute('select * from batch_master where batch_key = {}'.format(key))
    lists = cursor.fetchall()
    ans = False
    for i  in lists:
        ans = True
        print (lists,'are following products') 
    mycon.commit()
    return(ans)

def sales():                                                                                              #Tasks to be done :::::: identify things in product......... then go to its master ............ change its no....give total amount
    key = int(input('enter the product key'))
    batch_key = int(input(' specify batch key'+'{should be the table of batches}: '))
    cus_key = int(input('enter the customer key'))
    if check_product(key) and check_batch(batch_key):
        comm = 'select stock,cost,GST_slab from products,batch_master where products.product_key = batch_master.Product_Key AND batch_key = {}'.format(batch_key)
        cursor.execute(comm)
        dat = cursor.fetchall()[0]
        stock = dat[0]
        cost = dat[1]
        tax = dat[2]
        Qty = int(input('how many are you selling'))
        stock -= Qty
        sales_price = cost + (tax*cost)/100
        bill = sales_price * Qty
        cursor.execute('select credit from customers where custom_key = {}'.format(cus_key))
        out = cursor.fetchall()
        credit = out[0][0]
        credit += bill
        cursor.execute('update batch_master set stock ={} where batch_key = {} '.format(stock,batch_key))
        mycon.commit()
        cursor.execute('update customers set credit = {} where custom_key = {}'.format(credit,cus_key))
        mycon.commit()
    else:
        print('product not available try creating an new first')

def purchase():                                                                                     # Tasks to be done ::::::: check if there is any new product.......... check for any new batch..... update...give total amount
    key = int(input('enter key'))
    b_key = int(input('enter batch key'))
    if check_batch(b_key):
        print('we have the batch')
    elif check_product(key):
        print('add a new batch the key already exists')
        batch_update(key,b_key)
    else:
        create_product(key)
        batch_update(key,b_key)
    mycon.commit()
    checkout(key,b_key)

def  create_product(a):
    name =str( input('enter the name of the product: '))                         #!! Create new entery in product table
    packing = int(input('enter the GST slab of the product: '))
    minima = int(input('enter the minimum stock: '))
    maxima  = minima+300
    b,c,d,e = name,packing,minima,maxima
    comm = "insert into products values ({},'{}',{},{},{})".format(a,b,c,d,e)
    out = cursor.execute(comm)
    mycon.commit()

def enter_date():
    year = input('enter year: ')
    month = input('enter month number: ')
    day = input('enter date: ')
    date = year + '-' + month + '-'  + day
    return(date)

def batch_update(k,bk):
    print('\creating batch')
    b_key = bk
    stock  = int(input('enter how much you currently have in stock: '))
    print('enter manufacture date')
    m_date = enter_date()
    print('enter expiary date')
    e_date = enter_date()
    cost = int(input('enter the cost'))
    comm = "insert into batch_master values ({},{},{},'{}','{}',{})".format(k , b_key , stock , m_date , e_date, cost)
    cursor.execute(comm)
    mycon.commit()

def checkout(pk,bk):
    cursor.execute('select stock,cost from batch_master where batch_key = {}'.format(bk))
    dat = (cursor.fetchall())
    stock = dat[0][0]
    print(stock)
    quantity = int(input('enter the no of stocks you are buying'))
    stock += quantity
    price = dat[0][1]
    bill = price * quantity
    print(bill , 'is the total amount for purchasing')
    try:
        cursor.execute('update batch_master set stock = {} where batch_key ={}'.format(stock,bk))
    except:
        print('too many stocks')
    #updating customers
    custom_key = int(input('enter supplier key'))
    cursor.execute('select amount_due from suppliers where supp_key = {}'.format(custom_key))
    credit = cursor.fetchall()[0][0]
    credit += bill
    cursor.execute('update suppliers set amount_due ={} where supp_key = {}'.format(credit,custom_key))
    mycon.commit()

mycon = sqlator.connect(host='localhost', user='root', passwd='Plank#6.626', database='business')
if mycon.is_connected():
    print('connected')                                                                         # basic connection   object = mycon


cursor = mycon.cursor()                                                                   #cursor setup           cursor = cursor


while True:                                                                                        #main
    comm = int(input('1-purchase master    \n2-sales master    \n3-supplier master  \n4-customer master    \n0 - exit    \nenter your command:' ))
    if comm == 1:
        purchase()
        mycon.commit()
        #stop()
    elif comm == 2:
        sales()
    elif comm == 3:
       val= s_add()
       a,b,c,d = val
       statement = "insert into suppliers values({},'{}','{}',{})".format (a,b,c,d)
       cursor.execute(statement)
       mycon.commit()
    elif comm == 4:
        val= c_add()
        a,b,c,d = val  
        statement = "insert into customers values({},'{}','{}',{})".format (a,b,c,d)
        cursor.execute(statement)
        mycon.commit()
    elif comm == 0:
        break
    else:
        print('try again wrong command')
