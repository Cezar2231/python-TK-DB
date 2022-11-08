import sqlite3

conn = sqlite3.connect('Store.db')
curs = conn.cursor()

curs.execute("""CREATE TABLE IF NOT EXISTS ProductCategory(CategoryID integer PRIMARY KEY,
              CategoryName text NOT NULL);
              """)

#curs.execute("""INSERT INTO ProductCategory VALUES (1, 'Clothes'),
 #                                                   (2,'Shoes'),
    #                                                (3,'Accessories');
     #       """)

conn.commit()

curs.execute("""CREATE TABLE IF NOT EXISTS Product(ProductID integer PRIMARY KEY,
                ProductName text NOT NULL,
                ProductCategoryID integer REFERENCES ProductCategory(CategoryID) NOT NULL,
                ProductInStock integer NOT NULL,
                ProductPrice real NOT NULL);
                """)

#curs.execute("""INSERT INTO Product VALUES(1,'Nike Air 1',2,14,109.9),
 #                                          (2,'Adidas runners',2,8,99.99),
  #                                          (3,'Nike White T',1,25,30),
   #                                         (4,'Black Wallet',3,10,25.80);
    #                                        """)
conn.commit()
curs.execute("""CREATE TABLE IF NOT EXISTS Customer(CustomerID integer PRIMARY KEY,
                FirstName text NOT NULL,
                LastName text NOT NULL,
                CustomerTown text NOT NULL,
                CustomerAddress text NOT NULL,
                CustomerPhone text NOT NULL);
                """)
#curs.execute("""INSERT INTO Customer VALUES(001,'Martin','Stoyanov','Burgas','Center',0894321342),
 #                                           (002,'Georgi','Ivanov','Burgas','Meden Rudnik',0894311234),
  #                                          (003,'Ana','Stoeva','Varna','Slaveykov',0894314542);
   #                                         """)
conn.commit()
curs.execute("""CREATE TABLE IF NOT EXISTS Employee(EmployeeID integer PRIMARY KEY,
                EmFirstName text NOT NULL,
                EmLastName text NOT NULL,
                EmTown text NOT NULL,
                EmAddress text NOT NULL,
                EmPhone text NOT NULL);
                """)
#curs.execute("""INSERT INTO Employee VALUES(001,'Konstantin','Kostadinov','Burgas','Izgrev',0894777777),
 #                                           (002,'Petar','Andonov','Sofiq','Lylin',0894666666),
  #                                          (003,'Mariana','Popova','Burgas','Lazur',0894555555);
   #                                         """)
conn.commit()
curs.execute("""CREATE TABLE IF NOT EXISTS Sale(SSaleID integer PRIMARY KEY,
                SCustomerID integer REFERENCES Customer(CustomerID) NOT NULL,
                SEmployeeID integer REFERENCES Employee(EmployeeID) NOT NULL,
                SDate text NOT NULL);
                """)
#curs.execute("""INSERT INTO Sale VALUES(1,1,1,'12.05.2022'),
 #                                       (2,2,2,'12.05.2022'),
  #                                      (3,3,3,'12.05.2022'),
   #                                     (4,1,1,'12.05.2022');
    #                                    """)
conn.commit()
curs.execute("""CREATE TABLE IF NOT EXISTS SaleProduct(SaleID integer REFERENCES Sale(SSaleID) PRIMARY KEY NOT NULL,
                SProductID integer REFERENCES Product(ProductID) NOT NULL,
                Quantity integer NOT NULL);
                """)
#curs.execute("""INSERT INTO SaleProduct VALUES(1,1,2),
 #                                               (2,2,1),
  #                                              (3,3,4);
   #                                             """)

conn.commit()

