from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QPushButton
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('design.ui', self)

        # чекбоксы:
        self.checkBox.setChecked(True)
        self.checkbox_two.setChecked(False)

        # анализ и данные кнопки
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.pushButton_2.clicked.connect(self.on_pushButton_2_clicked)

    def on_pushButton_clicked(self):    #кнопка анализ
        print("Нажата кнопка pushButton")

    def on_pushButton_2_clicked(self):    #кнопка данные
        print("Нажата кнопка pushButton_2")


if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec_()
