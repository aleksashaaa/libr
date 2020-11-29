import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QPushButton
from PyQt5.QtGui import QPixmap
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Book(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(345, 445)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 20, 160, 180))
        self.label.setText("")
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(30, 220, 280, 210))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_6 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_9 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Информация о книге"))
        self.label_2.setText(_translate("Form", "Название"))
        self.label_3.setText(_translate("Form", "TextLabel"))
        self.label_6.setText(_translate("Form", "Автор"))
        self.label_7.setText(_translate("Form", "TextLabel"))
        self.label_5.setText(_translate("Form", "Год выпуска"))
        self.label_4.setText(_translate("Form", "TextLabel"))
        self.label_9.setText(_translate("Form", "Жанр"))
        self.label_8.setText(_translate("Form", "TextLabel"))


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(470, 420)
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(20, 120, 440, 280))
        self.listWidget.setObjectName("listWidget")
        self.Title = QtWidgets.QLineEdit(Form)
        self.Title.setGeometry(QtCore.QRect(30, 80, 150, 20))
        self.Title.setObjectName("Title")
        self.searchButton = QtWidgets.QPushButton(Form)
        self.searchButton.setGeometry(QtCore.QRect(230, 20, 130, 80))
        self.searchButton.setObjectName("searchButton")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(30, 30, 105, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Каталог библиотеки"))
        self.searchButton.setText(_translate("Form", "Искать"))
        self.comboBox.setItemText(0, _translate("Form", "Автор"))
        self.comboBox.setItemText(1, _translate("Form", "Название"))


class MainWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect("library.db")
        self.params = {"Автор": "author", "Название": "title"}
        self.searchButton.clicked.connect(self.search)

    def search(self):
        self.listWidget.clear()
        el = self.comboBox.currentText()
        if self.params.get(el) == "title":
            req = "SELECT id,title FROM books WHERE title LIKE '%{}%'".format(self.Title.text())
        else:
            req = "SELECT id,title FROM books WHERE author LIKE '%{}%'".format(self.Title.text())
        cur = self.con.cursor()
        data = cur.execute(req).fetchall()
        elems = [[QPushButton(i[1], self), i[0]] for i in data]
        for btn, loc_id in elems:
            btn.clicked.connect(self.show_info(loc_id))
        items = [QListWidgetItem() for _ in elems]
        for i in range(len(items)):
            self.listWidget.addItem(items[i])
            items[i].setSizeHint(elems[i][0].sizeHint())
            self.listWidget.setItemWidget(items[i], elems[i][0])

    def show_info(self, loc_id):
        def call_info():
            cur = self.con.cursor()
            title, year, author, image, genre = cur.execute(
                "SELECT title,year,author,image,genre From books Where id = {}".format(loc_id)).fetchone()
            if image:
                info_book = BookWidget(self, title, author, str(year), genre, image)
            else:
                info_book = BookWidget(self, title, author, str(year), genre)
            info_book.show()
        return call_info


class BookWidget(QMainWindow, Ui_Book):
    def __init__(self, parent=None, title=None, author=None, year=None, genre=None, image='noname.png'):
        super().__init__(parent)
        self.setupUi(self)
        self.label_3.setText(title)
        self.label_7.setText(author)
        self.label_4.setText(year)
        self.label_8.setText(genre)

        self.pixmap = QPixmap(image)
        self.label.setPixmap(self.pixmap)


app = QApplication(sys.argv)
ex = MainWidget()
ex.show()
sys.exit(app.exec_())