import os
import shutil
import sys

from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, \
    QInputDialog, QDialog, QDialogButtonBox, QComboBox, QSpinBox, QHBoxLayout, QVBoxLayout, QWidget, QFileDialog
from PyQt5.QtCore import QTimer, QSize, Qt, QRect
import sqlite3

import db


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(777, 600)
        self.verticalLayoutWidget = QWidget(self)
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setSpacing(16)
        self.verticalLayoutWidget.setGeometry(130, 110, 491, 398)
        self.verticalLayout.setContentsMargins(130, 130, 130, 130)

        self.label_2 = QLabel(self)
        self.verticalLayout.addWidget(self.label_2)
        self.field_username = QLineEdit(self)
        self.field_username.setMinimumSize(QSize(0, 50))
        self.verticalLayout.addWidget(self.field_username)
        self.label_3 = QLabel(self)

        self.verticalLayout.addWidget(self.label_3)
        self.field_pw = QLineEdit(self)
        self.field_pw.setMinimumSize(QSize(0, 50))
        self.field_pw.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.field_pw)

        self.btn_to_register = QPushButton(self)
        self.btn_to_register.setFlat(True)

        self.verticalLayout.addWidget(self.btn_to_register)
        self.btn_login = QPushButton(self)
        self.btn_login.setMinimumSize(QSize(0, 50))
        self.btn_login.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        self.btn_login.setAutoDefault(False)
        self.btn_login.setDefault(False)
        self.btn_login.setFlat(False)

        self.verticalLayout.addWidget(self.btn_login)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.label = QLabel(self)
        self.label.setGeometry(QRect(-40, 30, 821, 91))
        font = QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignCenter)

        self.setWindowTitle("Login")
        self.label_2.setText("Username")
        self.label_3.setText("Password")
        self.btn_to_register.setText("Belum memiliki akun? Daftar disini")
        self.btn_login.setText("Login")
        self.label.setText("Aplikasi Belanja Online")

        self.btn_login.clicked.connect(self.login_clicked)
        self.btn_to_register.clicked.connect(self.to_register)

        self.db = sqlite3.connect('belanja_online.db')
        self.cursor = self.db.cursor()

    def login_clicked(self):
        username = self.field_username.text()
        password = self.field_pw.text()

        self.cursor = self.db.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT, user_type TEXT)")
        self.db.commit()

        # Fetch the user from the database
        self.cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?",
                            (username, password))
        user = self.cursor.fetchone()

        if user:
            if user[2] == "Admin":
                self.admin_window = AdminWindow(user[0])
                self.admin_window.show()
            else:
                self.interface_window = InterfaceWindow(user[0])
                self.interface_window.show()
            self.hide()
        else:
            QMessageBox.warning(self, "Login Error", "username atau password salah.")
            self.field_username.clear()
            self.field_pw.clear()

    def to_register(self):
        self.register_window = RegisterWindow(self)
        self.register_window.show()
        self.hide()


class RegisterWindow(QWidget):
    def __init__(self, login_window):
        super().__init__()
        self.setFixedSize(777, 600)
        self.verticalLayoutWidget = QWidget(self)
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setSpacing(16)
        self.verticalLayoutWidget.setGeometry(130, 110, 491, 398)
        self.verticalLayout.setContentsMargins(100, 100, 100, 100)

        self.login_window = login_window
        self.label_2 = QLabel(self)
        self.verticalLayout.addWidget(self.label_2)
        self.field_username = QLineEdit(self)
        self.field_username.setMinimumSize(QSize(0, 50))
        self.verticalLayout.addWidget(self.field_username)
        self.label_3 = QLabel(self)

        self.verticalLayout.addWidget(self.label_3)
        self.field_pw = QLineEdit(self)
        self.field_pw.setMinimumSize(QSize(0, 50))

        self.verticalLayout.addWidget(self.field_pw)
        self.label_4 = QLabel(self)

        self.verticalLayout.addWidget(self.label_4)
        self.cb_role = QComboBox(self)
        self.cb_role.setMinimumSize(QSize(0, 50))
        self.cb_role.addItem("Admin")
        self.cb_role.addItem("Pembeli")

        self.verticalLayout.addWidget(self.cb_role)
        self.btn_to_login = QPushButton(self)
        self.btn_to_login.setFlat(True)

        self.verticalLayout.addWidget(self.btn_to_login)
        self.btn_register = QPushButton(self)
        self.btn_register.setMinimumSize(QSize(0, 50))
        self.btn_register.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        self.btn_register.setAutoDefault(False)
        self.btn_register.setDefault(False)
        self.btn_register.setFlat(False)

        self.verticalLayout.addWidget(self.btn_register)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.label = QLabel(self)
        self.label.setGeometry(QRect(-40, 30, 821, 91))
        font = QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setObjectName("label")

        self.setWindowTitle("Register")
        self.label_2.setText("Username")
        self.label_3.setText("Password")
        self.label_4.setText("Role")
        self.btn_to_login.setText("Sudah memiliki akun? Login disini")
        self.btn_register.setText("Register")
        self.label.setText("Daftar Akun")

        self.btn_register.clicked.connect(self.register_clicked)
        self.btn_to_login.clicked.connect(self.to_login)

        self.db = sqlite3.connect('belanja_online.db')
        self.cursor = self.db.cursor()

    def register_clicked(self):
        # Validate registration data
        username = self.field_username.text()
        password = self.field_pw.text()
        user_type = self.cb_role.currentText()  # get this value from a user input

        if username == "" or password == "":
            QMessageBox.warning(self, "Registrasi Error", "Semua harus terisi.")
            return

        # Simulasi penyimpanan data pengguna ke database
        self.cursor = self.db.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT, user_type TEXT)")

        # Check if the username already exists
        self.cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = self.cursor.fetchone()
        if user:
            QMessageBox.warning(self, "Registrasi Error", "Username sudah ada.")
            return

        self.cursor.execute("INSERT INTO users (username, password, user_type) VALUES (?, ?, ?)",
                            (username, password, user_type))
        self.db.commit()

        # Clear the input fields
        self.field_username.clear()
        self.field_pw.clear()

        QMessageBox.information(self, "Register berhasil!", "Silahkan login dengan username dan password")

        # Show the login window and hide the register window
        self.to_login()

    def to_login(self):
        self.login_window.show()
        self.close()

    def show_password_clicked(self):
        self.field_pw.setEchoMode(QLineEdit.Normal)
        QTimer.singleShot(10, lambda: self.field_pw.setEchoMode(QLineEdit.Password))


class AdminWindow(QWidget):
    def __init__(self, username):
        super().__init__()

        self.setWindowTitle("Admin")
        self.resize(400, 250)

        # Widgets
        self.welcome_label = QLabel(f"Selamat datang, {username}!")
        self.manage_button = QPushButton("Kelola Toko")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.welcome_label)
        layout.addWidget(self.manage_button)
        self.setLayout(layout)

        # Connections
        self.manage_button.clicked.connect(self.manage_clicked)

        self.db = sqlite3.connect('belanja_online.db')
        self.cursor = self.db.cursor()

    def manage_clicked(self):
        self.manage_store_window = ManageStoreWindow()
        self.manage_store_window.show()
        self.hide()


class ManageStoreWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kelola Toko")
        self.resize(400, 250)

        # Widgets
        self.item_label = QLabel("Nama Barang:")
        self.item_input = QComboBox()
        self.price_label = QLabel("Harga:")
        self.price_input = QLineEdit()
        self.stock_label = QLabel("Stok:")
        self.stock_input = QLineEdit()
        self.add_button = QPushButton("Tambah Barang Baru")
        self.update_button = QPushButton("Perbarui Barang")
        self.delete_button = QPushButton("Hapus Barang")
        self.logout_button = QPushButton("Log Out")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.item_label)
        layout.addWidget(self.item_input)
        layout.addWidget(self.price_label)
        layout.addWidget(self.price_input)
        layout.addWidget(self.stock_label)
        layout.addWidget(self.stock_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.update_button)
        layout.addWidget(self.delete_button)
        layout.addWidget(self.logout_button)
        self.setLayout(layout)

        # Connections
        self.add_button.clicked.connect(self.add_clicked)
        self.update_button.clicked.connect(self.update_clicked)
        self.delete_button.clicked.connect(self.delete_clicked)
        self.item_input.currentTextChanged.connect(self.set_data_to_field)
        self.logout_button.clicked.connect(self.logout)

        # Adding products to combo box
        products = db.get_all_products()
        for product in products:
            self.item_input.addItem(product[1], product[0])

        self.db = sqlite3.connect('belanja_online.db')
        self.cursor = self.db.cursor()

    def set_data_to_field(self):
        self.selected_id = self.item_input.itemData(self.item_input.currentIndex())
        product = db.get_product_by_id(self.selected_id)
        print(product)
        self.price_input.setText(str(product[2]))
        self.stock_input.setText(str(product[3]))

    def logout(self):
        self.login_window = LoginWindow()
        self.login_window.show()
        self.hide()

    def add_clicked(self):
        # name, ok = QInputDialog.getText(self, "New Item", "Enter item name:")
        # categories = db.get_categories()
        # if ok:
        #     category, ok = QInputDialog.getItem(self, "Category", "Select category:", categories[], 0, False)
        #     if ok:
        #         print("New Item Name:", name)
        #         print("Category:", category)
        #
        # self.cursor = self.db.cursor()
        # self.cursor.execute("INSERT INTO products (item, price, stock, img) VALUES (?, 0, 0, ?)", (item))
        # self.db.commit()
        #
        # self.item_input.clear()
        # self.price_input.clear()
        # self.stock_input.clear()
        dialog = NewItemDialog()
        if dialog.exec_() == QDialog.Accepted:
            try:
                name, category_id, img = dialog.get_new_item_info()
                self.cursor = self.db.cursor()
                self.cursor.execute(
                    "INSERT INTO products (product_name, price, stock, category_id, img) VALUES (?, ?, ?, ?, ?)",
                    (name, 0, 0, category_id, img))
                self.db.commit()
                self.restart()
            except TypeError:
                pass

    def restart(self):
        self.close()
        self.new_window = ManageStoreWindow()
        self.new_window.show()

    def update_clicked(self):
        item = self.item_input.currentText()
        price = self.price_input.text()
        stock = self.stock_input.text()

        self.cursor = self.db.cursor()
        self.cursor.execute("UPDATE products SET price = ?, stock = ? WHERE product_id = ?",
                            (price, stock, self.selected_id))
        self.db.commit()

        # self.item_input.clear()
        self.price_input.clear()
        self.stock_input.clear()

        QMessageBox.information(self, "Barang telah diupdate", "Informasi barang telah diperbarui!")
        self.restart()

    def delete_clicked(self):
        item = self.item_input.currentText()

        self.cursor = self.db.cursor()
        self.cursor.execute("DELETE FROM products WHERE product_id = ?", (self.selected_id,))
        self.db.commit()

        #         self.item_input.clear()
        self.price_input.clear()
        self.stock_input.clear()

        QMessageBox.information(self, "Barang telah dihapus", "Informasi barang telah dihapus!")
        self.restart()


class NewItemDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.img_file_name = None
        self.setWindowTitle("Tambah Barang Baru")

        layout = QVBoxLayout(self)

        self.label_name_edit = QLabel("Nama Barang:")
        self.name_edit = QLineEdit()
        self.label_category = QLabel("Kategori Barang:")
        self.category_combo = QComboBox()
        categories = db.get_categories()
        for category in categories:
            self.category_combo.addItem(category[1], category[0])  # Add your categories here

        self.select_file_button = QPushButton("Pilih gambar", self)
        self.select_file_button.clicked.connect(self.select_file)

        layout.addWidget(self.label_name_edit)
        layout.addWidget(self.name_edit)
        layout.addWidget(self.label_category)
        layout.addWidget(self.category_combo)
        layout.addWidget(self.select_file_button)

        button_box = QPushButton("Tambah")
        button_box.clicked.connect(self.accept)
        layout.addWidget(button_box)

    def select_file(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Image File", "", "Image Files (*.png *.jpg *.jpeg "
                                                                                  "*.bmp *.gif *.tiff)",
                                                   options=options)

        if file_path:
            # Move files to project folder
            project_folder = "img/"  # Replace with your project folder path
            self.img_file_name = os.path.basename(file_path)
            destination = os.path.join(project_folder, self.img_file_name)
            shutil.copy(file_path, destination)

    def get_new_item_info(self):
        name = self.name_edit.text()
        category_id = self.category_combo.itemData(self.category_combo.currentIndex())
        if name and category_id and self.img_file_name:
            return name, category_id, self.img_file_name
        else:
            QMessageBox.warning(self, "Error", "Isi semua field dan pilih file gambar!")


class InterfaceWindow(QWidget):
    def __init__(self, username):
        super().__init__()

        self.setWindowTitle("Interface")
        self.resize(400, 250)

        # Widgets
        self.welcome_label = QLabel(
            f"Selamat datang di toko kami, {username}!silahkan pilih benda yang akan anda pesan di halaman rekomendasi")
        self.recommendation_button = QPushButton("Halaman rekomendasi")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.welcome_label)
        layout.addWidget(self.recommendation_button)
        self.setLayout(layout)

        # Connections
        self.recommendation_button.clicked.connect(self.recommendation_clicked)

    def recommendation_clicked(self):
        self.recommendation_window = RecommendationWindow()
        self.recommendation_window.show()
        self.hide()


class RecommendationWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Rekomendasi")
        self.resize(400, 250)

        # Widgets
        self.recommendation_label = QLabel("Berikut adalah beberapa rekomendasi untuk Anda!")
        self.order_button = QPushButton("Taruh pesanan")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.recommendation_label)
        layout.addWidget(self.order_button)
        self.setLayout(layout)

        # Connections
        self.order_button.clicked.connect(self.order_clicked)

    def order_clicked(self):
        self.order_window = OrderWindow()
        self.order_window.show()
        self.hide()


class OrderWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Taruh pesanan")
        self.resize(500, 250)

        self.db = sqlite3.connect('belanja_online.db')
        self.cursor = self.db.cursor()

        # Widgets
        self.category_label = QLabel("Pilih pesanan:")

        self.category_combo = QComboBox()
        categories = db.get_categories()
        for category in categories:
            self.category_combo.addItem(category[1], category[0])
        self.category_combo.setCurrentIndex(0)

        self.item_label = QLabel("Pilih barang:")
        self.item_combo = QComboBox()
        self.quantity_label = QLabel("Pilih jumlah barang:")
        self.quantity_spinbox = QSpinBox()
        self.add_to_cart_button = QPushButton("Simpan dalam keranjang")
        self.view_cart_button = QPushButton("Cek keranjang")
        self.reduce_item_button = QPushButton("Kurangi jumlah barang")
        self.purchase_button = QPushButton("Beli")
        self.purchase_button.clicked.connect(self.purchase_clicked)
        self.selected_product_label = QLabel(self)
        self.selected_product_label.setFixedSize(200, 200)
        self.selected_product_pixmap = QPixmap()

        # Layout
        self.hlayout = QHBoxLayout()
        layout = QVBoxLayout()
        layout.addWidget(self.category_label)
        layout.addWidget(self.category_combo)
        layout.addWidget(self.item_label)
        layout.addWidget(self.item_combo)
        layout.addWidget(self.quantity_label)
        layout.addWidget(self.quantity_spinbox)
        layout.addWidget(self.add_to_cart_button)
        layout.addWidget(self.view_cart_button)
        layout.addWidget(self.reduce_item_button)
        self.hlayout.addLayout(layout)
        self.hlayout.addWidget(self.selected_product_label)
        self.setLayout(self.hlayout)

        # Connections
        self.category_combo.currentIndexChanged.connect(self.update_items)
        self.add_to_cart_button.clicked.connect(self.add_to_cart_clicked)
        self.view_cart_button.clicked.connect(self.view_cart_clicked)
        self.reduce_item_button.clicked.connect(self.reduce_item_clicked)
        self.item_combo.currentTextChanged.connect(self.set_barang_img)

        self.update_items()
        self.cart = {}

    def set_barang_img(self):
        id = self.item_combo.itemData(self.item_combo.currentIndex())
        if id:
            print("id", id)
            img_path = db.get_product_by_id(id)[5]
            print(img_path)
            self.selected_product_pixmap.load(f"img/{img_path}")
            self.selected_product_label.setPixmap(self.selected_product_pixmap)
            self.selected_product_label.setScaledContents(True)

    def update_items(self):
        selected_category = self.category_combo.currentIndex()
        id = self.category_combo.itemData(selected_category)
        products = db.get_products_by_category_id(id)
        self.item_combo.clear()
        for item in products:
            # item_text = f"{item[1]} - Harga: Rp.{item[2]}, Stok: {item[3]}"
            item_text = f"{item[1]} - Harga: Rp.{item[2]}"
            self.item_combo.addItem(item_text, item[0])

    def add_to_cart_clicked(self):
        category = self.category_combo.currentText()
        item_text = self.item_combo.currentText()  # Full item string including price and stock
        item = item_text.split(' - ')[0]  # Extract the item name
        quantity = self.quantity_spinbox.value()

        # Fetching product details from the database
        self.cursor.execute("SELECT price, stock FROM main.products WHERE product_name = ?", (item,))
        result = self.cursor.fetchone()

        if result:
            price, stock = result

            if stock >= quantity:
                # self.cursor.execute("UPDATE main.products SET stock = stock - ? WHERE product_name = ?", (quantity, item))

                # Add the item to the cart
                item_data = {"pesanan": category, "jumlah barang": quantity, "harga": price}

                if item in self.cart:
                    self.cart[item]["jumlah barang"] += quantity
                else:
                    self.cart[item] = {"pesanan": category, "jumlah barang": quantity, "harga": price}

                QMessageBox.information(self, "Keranjang",
                                        f"Anda menambahkan: {quantity} {item} ke dalam keranjang\nSisa stok barang: {stock - quantity}")
            else:
                QMessageBox.warning(self, "Stok barang habis", f"Barang {item} telah kehabisan stok.")
        else:
            QMessageBox.warning(self, "Produk Tidak Ditemukan", "Produk tidak ditemukan dalam database.")


    def view_cart_clicked(self):
        if self.cart:
            cart_summary = "Keranjang Anda:\n"
            total_price = 0
            print(self.cart)

            for item, details in self.cart.items():
                cart_summary += f"{item}: {details['jumlah barang']} (Harga: Rp.{details['harga']} per item)\n"
                total_price += details['jumlah barang'] * details['harga']

            cart_summary += f"Total harga: Rp.{total_price}"

            # Display cart summary in a QMessageBox
            QMessageBox.information(self, "Keranjang", cart_summary)

            # Create a QMessageBox to display cart summary and purchase button
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Keranjang")
            msg_box.setText(cart_summary)

            # Add "Beli" button
            purchase_button = msg_box.addButton("Beli", QMessageBox.AcceptRole)
            msg_box.addButton(QMessageBox.Cancel)

            # Execute QMessageBox and handle button click response
            result = msg_box.exec_()
            if msg_box.clickedButton() == purchase_button:
                self.purchase_clicked()
        else:
            QMessageBox.warning(self, "Keranjang Kosong", "Isi keranjang anda")

    def purchase_clicked(self):
        # Buat struk pembayaran
        payment_receipt = "Struk Pembayaran:\n"
        total_price = 0
        for item, details in self.cart.items():
            payment_receipt += f"{item}: {details['jumlah barang']} (Price: Rp.{details['harga']} each)\n"
            total_price += details['jumlah barang'] * details['harga']
        payment_receipt += f"Total price: Rp.{total_price}"

        # Tampilkan dialog pembayaran
        self.payment_dialog = QDialog(self)
        self.payment_dialog.setWindowTitle("Pembayaran")
        self.payment_dialog.setGeometry(100, 100, 400, 250)

        # Tambahkan label untuk struk pembayaran
        payment_label = QLabel(payment_receipt)

        # Tambahkan tombol "Cancel" dan "Konfirmasi Pembayaran"
        cancel_button = QPushButton("Cancel")
        confirm_button = QPushButton("Konfirmasi Pembayaran")
        cancel_button.clicked.connect(self.payment_dialog.reject)
        confirm_button.clicked.connect(self.confirm_payment)

        # Layout untuk dialog pembayaran
        payment_layout = QVBoxLayout()
        payment_layout.addWidget(payment_label)
        payment_layout.addWidget(cancel_button)
        payment_layout.addWidget(confirm_button)
        self.payment_dialog.setLayout(payment_layout)

        # Perbarui stok barang di toko
        self.update_stock()
        self.payment_dialog.exec_()

    def confirm_payment(self):
        self.after_order_window = AfterOrderWindow()
        self.after_order_window.show()
        self.payment_dialog.close()
        self.close()

    def reduce_item_clicked(self):
        current_item_index = 0
        print(list(self.cart.keys()))
        item, ok_pressed = QInputDialog.getItem(self, 'Select Item', 'Choose an item:', list(self.cart.keys()),
                                                current_item_index)

        # Tampilkan dialog
        if ok_pressed:
            item_name = item

            quantity, ok = QInputDialog.getInt(self, "Kurangi jumlah barang", "Masukkan jumlah yang ingin dikurangi:",
                                               1, 1, self.cart[item_name]["jumlah barang"])
            if ok:
                self.cart[item_name]["jumlah barang"] -= quantity
                self.update_stock_toko(item_name, quantity)
                QMessageBox.information(self, "keranjang",
                                        f"Anda mengurangi: {quantity} {item_name} dari keranjang")
                self.update_items()

    def get_available_items(self):
        self.cursor.execute("SELECT product_name FROM products WHERE stock > 0")
        return [row[0] for row in self.cursor.fetchall()]

    def get_item_stock(self, product_name):
        self.cursor.execute("SELECT stock FROM products WHERE product_name = ?", (product_name,))
        return self.cursor.fetchone()[0]

    def update_stock_toko(self, item, quantity):
        self.cursor.execute("UPDATE products SET stock = stock + ? WHERE product_name = ?", (quantity, item))
        self.db.commit()

    def update_stock(self):
        for item, details in self.cart.items():
            print(item)
            product = db.get_product_by_name(item)
            category = details["pesanan"]
            quantity = details["jumlah barang"]

            self.cursor.execute("SELECT stock FROM products WHERE product_name=?", (product[1],))
            current_stock = self.cursor.fetchone()[0]

            if current_stock >= quantity:
                new_stock = current_stock - quantity
                print(current_stock, "to", new_stock)
                self.cursor.execute("UPDATE products SET stock=? WHERE product_name=?", (new_stock, product[1]))
                self.db.commit()

    def show_payment_receipt(self):
        dialog = QDialog()
        dialog.setWindowTitle("Struk Pembayaran")
        dialog.resize(300, 200)

        label = QLabel("Terima kasih atas pembelian Anda!")
        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(dialog.accept)
        button_box.rejected.connect(dialog.reject)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button_box)
        dialog.setLayout(layout)

        result = dialog.exec_()
        if result == QDialog.Accepted:
            QMessageBox.information(self, "Pembayaran Berhasil", "Pembayaran Anda telah berhasil!")
        else:
            QMessageBox.warning(self, "Pembayaran Dibatalkan", "Pembayaran Anda telah dibatalkan.")


class AfterOrderWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(300, 200)

        self.label_success = QLabel("Pembayaran anda berhasil!\nApakah anda ingin belanja lagi?")
        self.btn_restart = QPushButton("Belanja Lagi")
        self.btn_log_out = QPushButton("Log out")
        self.btn_exit = QPushButton("Tutup Aplikasi")

        hlayout = QHBoxLayout()
        layout = QVBoxLayout()
        layout.addWidget(self.label_success)
        hlayout.addWidget(self.btn_restart)
        hlayout.addWidget(self.btn_log_out)
        hlayout.addWidget(self.btn_exit)
        layout.addLayout(hlayout)
        self.setLayout(layout)

        # Connections
        self.btn_restart.clicked.connect(self.restart)
        self.btn_log_out.clicked.connect(self.logout)
        self.btn_exit.clicked.connect(self.exit)

    def restart(self):
        self.order_window = OrderWindow()
        self.order_window.show()
        self.hide()

    def logout(self):
        self.login_window = LoginWindow()
        self.login_window.show()
        self.hide()

    def exit(self):
        QApplication.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
