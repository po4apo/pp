import datetime
import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QLabel
from models import *

from design import main_design, dialog_window, form, out_full_information


def remove_all_rows(tableWidget):
    for i in range(tableWidget.rowCount()):
        tableWidget.removeRow(i)


class OutFullInfo(QtWidgets.QDialog, out_full_information.Ui_Dialog):
    def __init__(self, employee_id):
        super().__init__()
        self.setupUi(self)
        print(1)

        emp = get_current_employee(int(employee_id))
        print(2)
        self.labelName.setText(str(emp[0]))
        self.labelSex.setText(str(emp[1]))
        self.labelPosition.setText(str(emp[2]))
        self.labelDateOfBirth.setText(str(emp[3]))
        self.labelDateOfHiring.setText(str(emp[4]))
        self.labelDepatment.setText(str(emp[5]))


class FormWindow(QtWidgets.QDialog, form.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.saveBtn.clicked.connect(self.add_employee)
        self.add_items_in_comboBoxes()

    def add_items_in_comboBoxes(self):
        print(1)
        self.comboBoxSex.addItem('ж', 0)
        print(2)
        self.comboBoxSex.addItem('м', 1)
        print(3)
        for dep in get_all_department():
            self.comboBoxDepartment.addItem(dep[1], dep[0])

    def add_employee(self):
        fields = {}
        fields['name'] = self.inputName.text()
        print(f'added name:{fields["name"]}')
        fields['position'] = self.inputPosition.text()
        print(f'added position:{fields["position"]}')
        fields['date_of_hiring'] = self.dateOfHiring.date().toPyDate()
        print(f'added date_of_hiring:{fields["date_of_hiring"]}')
        fields['birthday'] = self.dateOfBirth.date().toPyDate()
        print(f'added birthday:{fields["birthday"]}')
        fields['sex'] = self.comboBoxSex.currentData()
        print(f'added sex:{fields["sex"]}')
        fields['department'] = self.comboBoxDepartment.currentData()
        print(f'added department:{fields["department"]}')
        add_employee(**fields)
        self.close()


class DialogWindow(QtWidgets.QDialog, dialog_window.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.removeBtn.clicked.connect(self.accept)
        self.cancelBtn.clicked.connect(self.close)


class WindowApp(QtWidgets.QMainWindow, main_design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(['Номер', 'Имя', 'Должность', 'Отдел'])
        self.tableWidget.setRowCount(4)
        self.set_rows()
        self.sel.clicked.connect(self.remove_current_employee)
        self.add.clicked.connect(self.show_form)
        self.search.clicked.connect(self.show_full_info)

    def set_rows(self):
        """Удаляет все строки, после чего загружает новые из быза дынных"""
        remove_all_rows(self.tableWidget)
        rows = get_all_employee()
        i = 0
        for row in rows:
            self.tableWidget.setRowCount(len(rows))
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(row[1]))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(row[2])))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(row[3]))
            i += 1
        self.tableWidget.resizeColumnsToContents()

    def show_full_info(self):
        Id = self.inputId.text()
        if Id and Id and int(Id) in get_all_employee_id():
            print('in show_full_info')
            info = OutFullInfo(self.inputId.text())
            info.exec_()

    def show_form(self):
        form_window = FormWindow()
        form_window.exec_()
        self.set_rows()

    # Удаление сотрудника
    def show_dialog(self):
        """Выводит диалоговое окно для подтверждения удаления"""
        if self.tableWidget.selectedItems():
            print('go in dialog window')
            name = self.tableWidget.selectedItems()[1].text()
            dialog = DialogWindow()
            dialog.label.setText(f'Вы хотите удалить сотрудника {name.capitalize()}?')
            return dialog.exec_()
        else:
            ask = QtWidgets.QDialog()
            l = QLabel('Выберете сотрудника', ask)
            l.move(20, 20)
            ask.exec_()

    def remove_current_employee(self):
        """Удаляет сотрудника по его id. Id выбирается в таблице, путём выбора нужной строки. """
        if self.show_dialog():
            input_id = self.tableWidget.selectedItems()[0].text()
            remove_current_employee(input_id)
            self.set_rows()


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = WindowApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()


if __name__ == '__main__':
    main()
