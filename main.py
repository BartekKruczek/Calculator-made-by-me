import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fajny kalkulator")

        self.etykieta1 = QLabel("Wprowadź działanie: ", self)
        self.etykieta1.move(400, 150)
        self.etykieta1.resize(130, 30)

        self.button_dot = QPushButton()
        self.button_clear = QPushButton()
        self.button_wynik = QPushButton()
        self.button_dzie = QPushButton()
        self.button_mno = QPushButton()
        self.button_minus = QPushButton()
        self.button_plus = QPushButton()
        self.button0 = QPushButton()
        self.button9 = QPushButton()
        self.button8 = QPushButton()
        self.button7 = QPushButton()
        self.button6 = QPushButton()
        self.button5 = QPushButton()
        self.button4 = QPushButton()
        self.button3 = QPushButton()
        self.button2 = QPushButton()
        self.button1 = QPushButton()
        self.label = QLabel()

        self.widzety()

        self.showMaximized()

    def widzety(self):

        self.label = QLabel(self)
        self.label.move(550, 150)
        self.label.resize(500, 30)
        self.label.setWordWrap(True)
        self.label.setStyleSheet("QLabel"
                                 "{"
                                 "border : 1px solid black;"  # z neta
                                 "background : white;"
                                 "}")
        self.label.setAlignment(Qt.AlignRight)
        self.label.setFont(QFont('Arial', 15))

        self.button1 = QPushButton("1", self)
        self.button1.move(550, 200)
        self.button1.clicked.connect(self.one)

        self.button2 = QPushButton("2", self)
        self.button2.move(650, 200)
        self.button2.clicked.connect(self.two)

        self.button3 = QPushButton("3", self)
        self.button3.move(750, 200)
        self.button3.clicked.connect(self.three)

        self.button4 = QPushButton("4", self)
        self.button4.move(550, 250)
        self.button4.clicked.connect(self.four)

        self.button5 = QPushButton("5", self)
        self.button5.move(650, 250)
        self.button5.clicked.connect(self.five)

        self.button6 = QPushButton("6", self)
        self.button6.move(750, 250)
        self.button6.clicked.connect(self.six)

        self.button7 = QPushButton("7", self)
        self.button7.move(550, 300)
        self.button7.clicked.connect(self.seven)

        self.button8 = QPushButton("8", self)
        self.button8.move(650, 300)
        self.button8.clicked.connect(self.eight)

        self.button9 = QPushButton("9", self)
        self.button9.move(750, 300)
        self.button9.clicked.connect(self.nine)

        self.button0 = QPushButton("0", self)
        self.button0.move(550, 350)
        self.button0.clicked.connect(self.null)

        self.button_plus = QPushButton("+", self)
        self.button_plus.move(650, 350)
        self.button_plus.clicked.connect(self.dodawanie)

        self.button_minus = QPushButton("-", self)
        self.button_minus.move(750, 350)
        self.button_minus.clicked.connect(self.odejmowanie)

        self.button_mno = QPushButton("*", self)
        self.button_mno.move(550, 400)
        self.button_mno.clicked.connect(self.mnozenie)

        self.button_dzie = QPushButton("/", self)
        self.button_dzie.move(650, 400)
        self.button_dzie.clicked.connect(self.dzielenie)

        self.button_wynik = QPushButton("=", self)
        self.button_wynik.move(750, 400)
        self.button_wynik.clicked.connect(self.dzialanie)

        self.button_dot = QPushButton(".", self)
        self.button_dot.move(650, 450)
        self.button_dot.clicked.connect(self.dot)

        self.button_clear = QPushButton("Clear", self)
        self.button_clear.move(550, 450)
        self.button_clear.clicked.connect(self.clear)

    def dzialanie(self):
        x = self.label.text()
        try:
            ans = eval(x)
            self.label.setText(str(ans))
        except:
            self.label.setText("Błąd!")

    def dodawanie(self):
        x = self.label.text()
        self.label.setText(x + " + ")

    def odejmowanie(self):
        x = self.label.text()
        self.label.setText(x + " - ")

    def mnozenie(self):
        x = self.label.text()
        self.label.setText(x + " * ")

    def dzielenie(self):
        x = self.label.text()
        self.label.setText(x + " / ")

    def null(self):
        x = self.label.text()
        self.label.setText(x + "0")

    def one(self):
        x = self.label.text()
        self.label.setText(x + "1")

    def two(self):
        x = self.label.text()
        self.label.setText(x + "2")

    def three(self):
        x = self.label.text()
        self.label.setText(x + "3")

    def four(self):
        x = self.label.text()
        self.label.setText(x + "4")

    def five(self):
        x = self.label.text()
        self.label.setText(x + "5")

    def six(self):
        x = self.label.text()
        self.label.setText(x + "6")

    def seven(self):
        x = self.label.text()
        self.label.setText(x + "7")

    def eight(self):
        x = self.label.text()
        self.label.setText(x + "8")

    def nine(self):
        x = self.label.text()
        self.label.setText(x + "9")

    def dot(self):
        x = self.label.text()
        self.label.setText(x + ".")

    def clear(self):
        self.label.setText("")


app = QApplication(sys.argv)
ex = App()
app.exec_()
