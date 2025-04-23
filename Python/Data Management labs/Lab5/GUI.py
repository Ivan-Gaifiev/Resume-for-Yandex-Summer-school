import sys
from PyQt5.QtWidgets import (
    QWidget, QLineEdit, QGridLayout, QApplication, QPushButton, QLabel,
    QVBoxLayout, QHBoxLayout, QSizePolicy, QSpacerItem, QTextEdit, QDesktopWidget
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import DB_Server_func as f
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QComboBox

# TODO: В этом файле инициализация интерфейса и его внешнего вида, описание положения кнопок и прочих аттрибутов, а также
#  описание функций, которые вызываются при нажатии на какую-либо кнопку и обращаются к функциям взаимодействия с
#  сервером
#  Первый вход - всегда суперпользователь, если он создаст базу данных, то
#  создание автиматически приведёт к созданию гостя, у которого есть доступ к этой бд
#  Сначала я накидываю базовый интерфейс, исключительно для того, чтобы функции работали.
#  Когда всё готово, можно сделать покрасивее
# пригодится: QComboBox - выпадающий список, QTableWidget - таблицы
# нажимаем на create database и вылезает окно с полем, чтобы ввести название базы. и так для разных кнопок (окошко чтобы вылезало)
# нажимаем update record вылезает окно, в нём количество полей соответсвенно количеству полей в открытой таблице справа.
# вписываем в поля новые данные и они обновляются по ключевому полю
# внизу интерфейса поле для вывода ошибок и информации какой-то
# Лучше использовать QTableView + QSqlTableModel (автоматически подгружает данные из бд)
# https://ru.stackoverflow.com/questions/1413887/qtableview-qsqltablemodel-%D0%98%D0%B7%D0%BC%D0%B5%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D0%B9-%D0%B2-%D1%8F%D1%87%D0%B5%D0%B9%D0%BA%D0%B0%D1%85


class SecondWindow(QWidget):
    def __init__(self, title, num_fields, username=None, password=None):
        super().__init__()
        self.username = username
        self.password = password
        self.setWindowTitle("Fill the fields")
        self.resize(500, 200)
        self.center()
        layout = QVBoxLayout()
        label = QLabel(title)
        layout.addWidget(label)
        self.fields=[]
        for _ in range(num_fields):
            field = QLineEdit()
            self.fields.append(field)
            layout.addWidget(field)
        self.enter_button = QPushButton("Enter")
        # if title == 'Choose a name for your database':
        #     layout.addWidget(self.enter_button)
        #     self.enter_button.clicked.connect(lambda: f.create_database(self.fields[0].text(), self.username_edit.text(), self.password_edit.text()))
        if title == 'Choose a name for your table':
            layout.addWidget(self.enter_button)
            self.enter_button.clicked.connect(lambda: f.create_table(self.fields[0].text()))
        elif title == 'What is the name of the table you want to clear?':
            layout.addWidget(self.enter_button)
            self.enter_button.clicked.connect(lambda: f.clear_table(self.fields[0].text()))
        elif title == 'Which data you want to insert?':
            layout.addWidget(self.enter_button)
            self.enter_button.clicked.connect(lambda: f.add_data_games(self.fields[0].text(), self.fields[1].text(), self.fields[2].text()))
        self.setLayout(layout)


    def center(self):
        frame_geometry = self.frameGeometry()
        screen_center = QDesktopWidget().availableGeometry().center()
        frame_geometry.moveCenter(screen_center)
        self.move(frame_geometry.topLeft())
    def send_query(self):
        pass

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI for postgres")
        self.setWindowIcon(QIcon('icon-database.png'))
        self.resize(500, 300)
        self.center()
        self.initUI()

    def center(self):
        frame_geometry = self.frameGeometry()
        screen_center = QDesktopWidget().availableGeometry().center()
        frame_geometry.moveCenter(screen_center)
        self.move(frame_geometry.topLeft())

    def initUI(self):
        username_label = QLabel('Username:')
        self.username_edit = QLineEdit()

        password_label = QLabel('Password:')
        self.password_edit = QLineEdit()

        self.button = QPushButton("Enter")
        self.button.clicked.connect(self.on_login)

        # set net and place widgets
        self.form_layout = QGridLayout()
        self.form_layout.addWidget(username_label, 0, 0)
        self.form_layout.addWidget(self.username_edit, 0, 1)
        self.form_layout.addWidget(password_label, 1, 0)
        self.form_layout.addWidget(self.password_edit, 1, 1)

        # template for centering
        self.center_layout = QVBoxLayout()
        self.center_layout.addStretch(1)
        self.center_layout.addLayout(self.form_layout)
        self.center_layout.addWidget(self.button, alignment=Qt.AlignCenter)
        self.center_layout.addStretch(1)

        # set template
        self.setLayout(self.center_layout)

    def on_login(self):
        conn = f.connect_db(self.username_edit.text(), self.password_edit.text())
        if conn:
            self.show_new_interface()
        else:
            self.error_mes = QLabel('<span style="color: rgb(250, 55, 55);">Wrong inputed data</span>', self)
            self.center_layout.addWidget(self.error_mes)

    def something(self):
        print("i am here")


    def clear_layout(self, layout):
        # delete old widgets
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

    def show_new_interface(self):
        self.clear_layout(self.center_layout)
        self.clear_layout(self.form_layout)

        self.resize(1100, 500)
        self.center()

        self.main_layout = QGridLayout()
        self.center_layout.addLayout(self.main_layout)

        self.button_db = QPushButton("Create database")
        self.button_db.clicked.connect(lambda: self.open_new_window('Choose a name for your database', 1, self.username_edit.text(), self.password_edit.text()))
        self.main_layout.addWidget(self.button_db, 0, 0)

        self.button_table = QPushButton("Create table")
        self.button_table.clicked.connect(lambda: self.open_new_window('Choose a name for your table', 1))
        self.main_layout.addWidget(self.button_table, 1, 0)

        self.button_del_db = QPushButton("Delete database")
        self.button_del_db.clicked.connect(lambda: self.open_new_window('What is the name of the database you want to delete?', 1))
        self.main_layout.addWidget(self.button_del_db, 2, 0)

        self.button_cl_table = QPushButton("Clear table")
        self.button_cl_table.clicked.connect(
            lambda: self.open_new_window('What is the name of the table you want to clear?', 1))
        self.main_layout.addWidget(self.button_cl_table, 3, 0)

        self.button_add_data = QPushButton("Add new data")
        self.button_add_data.clicked.connect(lambda: self.open_new_window('Which data you want to insert?', 3))
        self.main_layout.addWidget(self.button_add_data, 4, 0)

        self.button_search = QPushButton("Search by field")
        self.button_search.clicked.connect(lambda: self.open_new_window(f"What do you want to find in '{self.choose_field()}'?", 1))
        self.main_layout.addWidget(self.button_search, 5, 0)

        self.button_record = QPushButton("Update record")
        self.button_record.clicked.connect(
            lambda: self.open_new_window('Which data you want to update?', f.which_num_columns(self.choose_table())))
        self.main_layout.addWidget(self.button_record, 6, 0)

        self.button_del_field = QPushButton("Delete by field")
        self.button_del_field.clicked.connect(
            lambda: self.open_new_window(f"What do you want to delete in '{self.choose_field()}'?", 1))
        self.main_layout.addWidget(self.button_del_field, 7, 0)

        self.button_show_table = QPushButton("Show table")
        self.button_show_table.clicked.connect(self.display_table_data)
        self.main_layout.addWidget(self.button_show_table, 8, 0)

        self.combo_table = QComboBox()
        self.combo_table.addItems(["games", "orders", "trading_platforms", "customers"])
        self.main_layout.addWidget(self.combo_table, 9, 0)

        # Комбобокс для выбора поля
        self.combo_field = QComboBox()
        self.combo_field.addItems(["name", "genre", "price"]) 
        self.main_layout.addWidget(self.combo_field, 10, 0)

        self.query_output = QTextEdit()
        self.main_layout.addWidget(self.query_output, 0, 1, 11, 1)

        self.query_error = QTextEdit()
        self.query_error.setReadOnly(True)
        self.main_layout.addWidget(self.query_error, 11, 0, 1, 2)
        self.query_error.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.query_error.setMaximumHeight(70)

    def open_new_window(self, title, num_fields, username=None, password=None):
        self.second_window = SecondWindow(title, num_fields, username, password)
        self.second_window.show()

    def display_table_data(self):
        table_name = self.choose_table()
        output = f.show_table(table_name)
        if output:
            res = ""
            for row in output:
                res += " | ".join(map(str, row)) + "\n"
            self.query_output.setPlainText(res)

    def choose_table(self):
        return self.combo_table.currentText()

    def choose_field(self):
        # здесь нужно брать значение выбранное в comboBox и возвращать его как название поля
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


