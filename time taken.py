D = '''Enter password: ***********
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 42
Server version: 8.0.24 MySQL Community Server - GPL

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> drop database business;
Query OK, 4 rows affected (2.74 sec)

mysql> create database business;
Query OK, 1 row affected (0.58 sec)

mysql>
mysql> use business;
Database changed
mysql>
mysql> create table products
    -> (
    -> Product_Key integer primary key,
    -> Name char(20),
    -> GST_Slab integer,
    -> Min_Stock integer,
    -> Max_stock integer );
Query OK, 0 rows affected (0.98 sec)

mysql>
mysql> insert into products
    -> values(6094,'Amoxicillin(250mg)',5,120,420);
Query OK, 1 row affected (0.38 sec)

mysql> insert into products
    -> values(3125,'Warfarin(2.5mg)',5,125,425);
Query OK, 1 row affected (0.56 sec)

mysql> insert into products
    -> values(3212,'Temozolomide(100mg)',5,130,430);
Query OK, 1 row affected (0.38 sec)

mysql> insert into products
    -> values(2883,'Saquinavir(200mg)',10,135,435);
Query OK, 1 row affected (0.10 sec)

mysql> insert into products
    -> values(3722,'Azithromycin(600mg)',5,140,440);
Query OK, 1 row affected (0.12 sec)

mysql> insert into products
    -> values(9413,'Posaconazole(100mg)',5,145,445);
Query OK, 1 row affected (0.09 sec)

mysql> insert into products
    -> values(9428,'Rituximab(500ml)',5,120,420);
Query OK, 1 row affected (0.20 sec)

mysql> insert into products
    -> values(3627,'Promethazine(25mg)',5,125,425);
Query OK, 1 row affected (0.08 sec)

mysql> insert into products
    -> values(5216,'Nelfinavir(250mg)',5,130,430);
Query OK, 1 row affected (0.18 sec)

mysql> insert into products
    -> values(8609,'Irinotecan(100ml)',5,135,435);
Query OK, 1 row affected (0.08 sec)

mysql>
mysql> create table batch_master
    -> (
    -> product_key integer,
    -> batch_key integer NOT NULL primary key,
    -> stock integer,
    -> manufacture_date date,
    -> expiary_date date,
    -> cost integer check(cost>0),
    -> check ( manufacture_date < expiary_date),
    -> foreign key (product_key) references Products(product_key)
    -> on delete cascade on update cascade );
Query OK, 0 rows affected (1.21 sec)

mysql>
mysql> insert into batch_master values
    -> (6094,56546,122,'2021-02-01','2025-02-01',1000);
Query OK, 1 row affected (0.32 sec)

mysql> insert into batch_master values
    -> (3125,46869,285,'2021-05-01','2025-05-01',6520);
Query OK, 1 row affected (0.09 sec)

mysql> insert into batch_master values
    -> (3212,54498,273,'2021-06-01','2025-06-01',9800);
Query OK, 1 row affected (0.13 sec)

mysql> insert into batch_master values
    -> (2883,54654,246,'2021-04-01','2025-04-01',1500);
Query OK, 1 row affected (0.08 sec)

mysql> insert into batch_master values
    -> (3722,65292,425,'2021-11-01','2025-11-01',3000);
Query OK, 1 row affected (0.22 sec)

mysql> insert into batch_master values
    -> (9413,54988,439,'2021-12-01','2025-12-01',4500);
Query OK, 1 row affected (0.31 sec)

mysql> insert into batch_master values
    -> (9428,98149,341,'2021-03-01','2025-03-01',3100);
Query OK, 1 row affected (0.15 sec)

mysql> insert into batch_master values
    -> (3627,81498,319,'2021-02-01','2025-02-01',2990);
Query OK, 1 row affected (0.17 sec)

mysql> insert into batch_master values
    -> (5216,71981,294,'2021-07-01','2025-07-01',6520);
Query OK, 1 row affected (0.13 sec)

mysql> insert into batch_master values
    -> (8609,14785,428,'2021-01-01','2025-01-01',2000);
Query OK, 1 row affected (0.30 sec)

mysql>
mysql> create table suppliers
    -> (
    -> supp_key integer primary key,
    -> name char(25),
    -> phno char(10),
    -> amount_due integer );
Query OK, 0 rows affected (0.97 sec)

mysql>
mysql> insert into suppliers values
    -> (6555,'Healthly.pvt.ltd',6263972722,0);
Query OK, 1 row affected (0.07 sec)

mysql> insert into suppliers values
    -> (6546,'Synergy.pvt.ltd',5791687397,0);
Query OK, 1 row affected (0.23 sec)

mysql> insert into suppliers values
    -> (5465,'Greenity.pvt.ltd',6703732358,0);
Query OK, 1 row affected (0.14 sec)

mysql> insert into suppliers values
    -> (8989,'Stark.pvt.ltd',2707384116,0);
Query OK, 1 row affected (0.08 sec)

mysql> insert into suppliers values
    -> (8948,'Roger.pvt.ltd',2418201660,0);
Query OK, 1 row affected (0.27 sec)

mysql> insert into suppliers values
    -> (4487,'Purity.pvt.ltd',7132541383,0);
Query OK, 1 row affected (0.27 sec)

mysql>
mysql> create table customers(
    -> custom_key integer not null primary key,
    -> name char(25),
    -> phno char(10),
    -> credit integer );
Query OK, 0 rows affected (0.79 sec)

mysql>
mysql> insert into customers values
    -> (8116,'nimesh.pvt.ltd',8728023872,0);
Query OK, 1 row affected (0.28 sec)

mysql> insert into customers values
    -> (6486,'ganesh.pvt.ltd',2140914861,0);
Query OK, 1 row affected (0.10 sec)

mysql> insert into customers values
    -> (6293,'appolo meds.pvt.ltd',3072717900,0);
Query OK, 1 row affected (0.10 sec)

mysql> insert into customers values
    -> (4461,'green meds.pvt.ltd',5169549780,0);
Query OK, 1 row affected (0.26 sec)

mysql> insert into customers values
    -> (7131,'youcare meds.pvt.ltd',5892925113,0);
Query OK, 1 row affected (0.36 sec)'''

time = 0
lines = D.split('\n')
for i in lines:
    if 'Qu' in i:
        t = i[26:30]
        if t[0] == '(':
            t = t[1:5]
        t = float(t)
        time += t
print (time)
