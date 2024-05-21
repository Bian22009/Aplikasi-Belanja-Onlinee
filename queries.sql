PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE items (item TEXT, price TEXT, stock TEXT);
INSERT INTO items VALUES('dwwa','1000','4');
INSERT INTO items VALUES('dwa','10000','12');
INSERT INTO items VALUES('dd','ddd','10');
INSERT INTO items VALUES('dd1','10000','10');
CREATE TABLE users (username TEXT, password TEXT, user_type TEXT);
INSERT INTO users VALUES('dd','dd','Admin');
INSERT INTO users VALUES('ww','ww','Pembeli');
CREATE TABLE categories (
                                          category_id INTEGER PRIMARY KEY,
                                          category_name TEXT NOT NULL
);
INSERT INTO categories VALUES(1,'Makanan');
INSERT INTO categories VALUES(2,'Minuman');
INSERT INTO categories VALUES(3,'Sayuran dan buah-buahan segar');
INSERT INTO categories VALUES(4,'Peralatan rumah tangga');
INSERT INTO categories VALUES(5,'Produk perawatan pribadi');
CREATE TABLE products (
                                        product_id INTEGER PRIMARY KEY,
                                        product_name TEXT NOT NULL,
                                        price INTEGER NOT NULL,
                                        stock INTEGER NOT NULL,
                                        category_id INTEGER,
                                        FOREIGN KEY (category_id) REFERENCES categories (category_id)
);
INSERT INTO products VALUES(1,'Mie Instan',3500,20,1);
INSERT INTO products VALUES(2,'Bubur Instan',5000,15,1);
INSERT INTO products VALUES(3,'Pasta',17000,10,1);
INSERT INTO products VALUES(4,'Samyang',18000,10,1);
INSERT INTO products VALUES(5,'Coca-Cola',7000,20,2);
INSERT INTO products VALUES(6,'Pepsi',7000,25,2);
INSERT INTO products VALUES(7,'Air mineral',4000,50,2);
INSERT INTO products VALUES(8,'Apel (1kg)',35000,10,3);
INSERT INTO products VALUES(9,'Pisang (1 sisir)',20000,12,3);
INSERT INTO products VALUES(10,'Wortel',8000,15,3);
INSERT INTO products VALUES(11,'Kentang',15000,15,3);
INSERT INTO products VALUES(12,'Tisu',10000,20,4);
INSERT INTO products VALUES(13,'Detergen',4000,50,4);
INSERT INTO products VALUES(14,'Sabun Cuci',5000,60,4);
INSERT INTO products VALUES(15,'Shampoo',15000,30,5);
INSERT INTO products VALUES(16,'Sabun',5000,40,5);
INSERT INTO products VALUES(17,'Pasta Gigi',9000,35,5);
COMMIT;
