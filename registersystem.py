import sys
from PyQt5 import QtWidgets, uic
import sqlite3

def register_new_user(name, email, password, confirm_password):
    error = False

    if name:
        pass

    if "@" in email and ".com":
        pass

    if password == confirm_password and len(password) > 6:
        pass

    else:
        error = True
    
    try:
        bank = sqlite3.connect("data_user.db")
        cursor = bank.cursor()

        cursor.execute("CREATE TABLE IF NOT EXISTS data_user (name text, email text, password text)")
        cursor.execute(f"INSERT INTO data_user VALUES ('{name}', '{email}', '{password}')")

        bank.commit()
        bank.close()

    except sqlite3.Error as Error:
        print(Error)
        error = True
    
    return error

def sign_in():
    email = window.lineEdit.text()
    password = window.lineEdit_2.text()

    if email and password:
        try:
            bank = sqlite3.connect("data_user.db")
            cursor = bank.cursor()

            cursor.execute(f"SELECT password FROM data_user WHERE email='{email}'")

            captured_password = cursor.fetchall()

            try:
                if password == captured_password[0][0]:
                    print("Joined")
                else:
                    print("Failed")
            except:
                pass
    
        except sqlite3.Error as error:
            print(error)
    else:
        print("Email and Password are required")

    window.lineEdit.setText("")
    window.lineEdit_2.setText("")

def create_acc():
    name = window.lineEdit_4.text()
    email = window.lineEdit_3.text()
    password = window.lineEdit_5.text()
    confirm_password = window.lineEdit_6.text()

    error = register_new_user(name, email, password, confirm_password)
    if not error:
        print("Successfully Registered")
    else:
        print("Register went wrong")
        
    window.lineEdit_4.setText("")
    window.lineEdit_3.setText("")
    window.lineEdit_5.setText("")
    window.lineEdit_6.setText("")

app = QtWidgets.QApplication([])
window = uic.loadUi("Interface2.ui")

window.pushButton.clicked.connect(sign_in)
window.pushButton_3.clicked.connect(create_acc)
window.pushButton_2.clicked.connect(lambda: window.RegisterAcc.setCurrentWidget(window.Create_Account))
window.pushButton_4.clicked.connect(lambda: window.RegisterAcc.setCurrentWidget(window.Login))

window.show()
sys.exit(app.exec_())
