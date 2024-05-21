import sqlite3

with sqlite3.connect("belanja_online.db") as db:
    cursor = db.cursor()


    def get_categories():
        cursor.execute("SELECT * FROM categories")
        categories = cursor.fetchall()
        return categories


    def get_all_products():
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()
        return products


    def get_products_by_category_id(id):
        cursor.execute(f"SELECT * FROM products WHERE category_id = {id}")
        products = cursor.fetchall()
        return products


    def get_product_by_name(name):
        cursor.execute(f"SELECT * FROM products WHERE product_name = '{name}'")
        product = cursor.fetchone()
        return product

    def get_product_by_id(id):
        cursor.execute(f"SELECT * FROM products WHERE product_id = '{id}'")
        product = cursor.fetchone()
        return product


    def product_reduce_stock(name, quantity):
        cursor.execute("SELECT stock FROM products WHERE product_name=?", (name,))
        current_stock = cursor.fetchone()[0]

        if current_stock >= quantity:
            new_stock = current_stock - quantity
            print(current_stock, "to", new_stock)
            cursor.execute("UPDATE products SET stock=? WHERE product_name=?", (new_stock, name))
            db.commit()

