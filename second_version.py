import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog
from PyQt5.uic import loadUi
import csv


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('design.ui', self)

        # чекбоксы:
        self.checkBox.setChecked(False)
        self.checkbox_two.setChecked(False)

        # анализ и данные кнопки
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.pushButton_2.clicked.connect(self.on_pushButton_2_clicked)

        self.checkBox.stateChanged.connect(self.on_checkBox_stateChanged)
        self.checkbox_two.stateChanged.connect(self.on_checkbox_two_stateChanged)

    def on_pushButton_clicked(self):  # кнопка анализ
        data_entry_window = DataEntryWindow()
        data_entry_window.exec_()

    def on_pushButton_2_clicked(self):  # сохраниение суммы чисел
        check_data_window = ConvergenceCalculator()  
        check_data_window.exec_()

    def on_checkBox_stateChanged(self, state):
        if state == 2:  # state == 2, если чекбокс отмечен
            about_app_dialog = AboutApp(self)
            about_app_dialog.exec_()

    def on_checkbox_two_stateChanged(self, state):
        if state == 2:  # state == 2, если чекбокс отмечен
            about_instruction_dialog = AboutInstruction(self)
            about_instruction_dialog.exec_()


class ConvergenceCalculator(QDialog):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Convergence Calculator')

        self.input_label = QLabel('Введите числа через запятую:')
        self.input_edit = QLineEdit()
        self.result_label = QLabel('Результат:')

        self.calculate_button = QPushButton('Вычислить')
        self.calculate_button.clicked.connect(self.calculate_convergence)

        self.save_button = QPushButton('Сохранить')
        self.save_button.clicked.connect(self.save_to_csv)

        layout = QVBoxLayout()
        layout.addWidget(self.input_label)
        layout.addWidget(self.input_edit)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.result_label)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def calculate_convergence(self):
        input_text = self.input_edit.text()
        try:
            numbers = [float(num) for num in input_text.split(',')]
            result = sum(numbers)
            self.result_label.setText(f'Результат: {result}')
        except ValueError:
            self.result_label.setText('Ошибка ввода. Пожалуйста, введите числа, разделенные запятой.')

    def save_to_csv(self):
        try:
            file_path, _ = QFileDialog.getSaveFileName(self, 'Сохранить результат', '', 'CSV Files (*.csv);;All Files (*)')
            if not file_path:
                return  

            is_new_file = not os.path.exists(file_path)
            with open(file_path, 'a', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)

                if is_new_file:
                    csv_writer.writerow(['Результат'])

                result_text = self.result_label.text().replace('Результат: ', '')
                csv_writer.writerow([result_text])

        except Exception as e:
            self.result_label.setText(f'Ошибка при сохранении в CSV: {e}')


#ОКНО АНАЛИЗА
class DataEntryWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Расчет для предпринимателя")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.label_income = QLabel("Введите данные о прибыле:")
        self.text_income = QLineEdit(self)

        self.label_expense = QLabel("Введите данные о расходах:")
        self.text_expense = QLineEdit(self)

        self.label_loan_amount = QLabel("Сумма кредита:")
        self.text_loan_amount = QLineEdit(self)

        self.label_loan_duration = QLabel("Количество месяцев обязательства:")
        self.text_loan_duration = QLineEdit(self)

        self.label_interest_rate = QLabel("Процентная ставка в месяц:")
        self.text_interest_rate = QLineEdit(self)

        self.label_net_income = QLabel("Чистая прибыль:")
        self.text_net_income = QLabel(self)

        self.label_total_payment = QLabel("Итоговая сумма по кредиту:")
        self.text_total_payment = QLabel(self)


        self.button_calculate = QPushButton("Рассчитать", self)
        self.button_calculate.clicked.connect(self.calculate_net_income_and_loan)

        self.button_clear = QPushButton("Очистить", self)
        self.button_clear.clicked.connect(self.clear_fields)

        layout.addWidget(self.label_income)
        layout.addWidget(self.text_income)
        layout.addWidget(self.label_expense)
        layout.addWidget(self.text_expense)
        layout.addWidget(self.label_loan_amount)
        layout.addWidget(self.text_loan_amount)
        layout.addWidget(self.label_loan_duration)
        layout.addWidget(self.text_loan_duration)
        layout.addWidget(self.label_interest_rate)
        layout.addWidget(self.text_interest_rate)
        layout.addWidget(self.button_calculate)
        layout.addWidget(self.label_net_income)
        layout.addWidget(self.text_net_income)
        layout.addWidget(self.label_total_payment)
        layout.addWidget(self.text_total_payment)
        layout.addWidget(self.button_clear)

        self.setLayout(layout)

    def calculate_net_income_and_loan(self):
        income = float(self.text_income.text()) if self.text_income.text() else 0.0
        expense = float(self.text_expense.text()) if self.text_expense.text() else 0.0
        net_income = income - expense
        self.text_net_income.setText(str(net_income))

        loan_amount = float(self.text_loan_amount.text()) if self.text_loan_amount.text() else 0.0
        loan_duration = int(self.text_loan_duration.text()) if self.text_loan_duration.text() else 0
        interest_rate = float(self.text_interest_rate.text()) if self.text_interest_rate.text() else 0.0

        total_payment = loan_amount * (1 + interest_rate / 100) ** loan_duration
        self.text_total_payment.setText(str(total_payment))

        total_payment = loan_amount * (1 + interest_rate / 100) ** loan_duration
        self.text_total_payment.setText(str(total_payment))

        result_str = f"Income: {income}\nExpense: {expense}\nNet Income: {net_income}\nLoan Amount: {loan_amount}\nLoan Duration: {loan_duration}\nInterest Rate: {interest_rate}\nTotal Payment: {total_payment}\n"
        self.save_to_file(result_str)

    def save_to_file(self, result_str):
        try:
            file_path = "text_results.txt"

            if not os.path.exists(file_path):
                with open(file_path, "w"):
                    pass

            with open(file_path, "a") as file:
                file.write(result_str)

        except Exception as e:
            print(f"Error saving to file: {e}")

    def clear_fields(self):
        self.text_income.clear()
        self.text_expense.clear()
        self.text_loan_amount.clear()
        self.text_loan_duration.clear()
        self.text_interest_rate.clear()
        self.text_net_income.clear()
        self.text_total_payment.clear()


#Сумма чисел
class AboutApp(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Справка')
        self.setFixedSize(520, 400)

        
        label = QLabel('Здесь вы можете получить всю необходимую информацию о приложении.<br>'
        'Узнайте текущую версию приложения, дату последнего обновления и ключевые<br> '
        'технические особенности. Мы постоянно работаем над улучшением функционала, <br>'
        'и здесь вы сможете найти подробности о последних изменениях.<br>'

        'Также в этом разделе вы найдете информацию о команде разработчиков,<br> '
        'ответственных за создание приложения. Узнайте больше о нашем опыте,<br> '
        'миссии и целях, чтобы быть в курсе всех тонкостей технологического<br> '
        'творчества.', self)
        layout = QVBoxLayout(self)
        layout.addWidget(label)


class AboutInstruction(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Инструкция')
        self.setFixedSize(500, 400)

        label = QLabel('анализ - калькулятор ипотечной ставки и кальуклятор прибыли', self)

        layout = QVBoxLayout(self)
        layout.addWidget(label)


if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec_()
