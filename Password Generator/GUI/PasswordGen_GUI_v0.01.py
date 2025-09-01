from __future__ import annotations

import string
import secrets

import sys

from PySide6.QtWidgets import (QApplication, QComboBox, QDialog,
                               QDialogButtonBox, QGridLayout, QGroupBox,
                               QFormLayout, QHBoxLayout, QLabel, QLineEdit,
                               QMenu, QMenuBar, QPushButton, QSpinBox,
                               QTextEdit, QVBoxLayout)

characterlist = ""

class Dialog(QDialog):
    num_grid_rows = 3
    num_buttons = 4


    def __init__(self):
        super().__init__()

        self.create_menu()
        self.create_horizontal_group_box()
        self.create_grid_group_box()


        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok
                                      | QDialogButtonBox.StandardButton.Cancel)

        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        main_layout = QVBoxLayout()
        main_layout.setMenuBar(self._menu_bar)
        main_layout.addWidget(self._horizontal_group_box)
        main_layout.addWidget(self._grid_group_box)
        self.setLayout(main_layout)

        self.setWindowTitle("PasswordGen V0.01")
        self.setFixedSize(720,950)
    def create_menu(self):
        self._menu_bar = QMenuBar()

        self._file_menu = QMenu("&File", self)
        self._exit_action = self._file_menu.addAction("E&xit")
        self._menu_bar.addMenu(self._file_menu)

        self._exit_action.triggered.connect(self.accept)

    def create_horizontal_group_box(self):
        self._horizontal_group_box = QGroupBox("Password options, click every button to add to generation")
        layout = QHBoxLayout()

        btn_special = QPushButton("Special Characters")
        layout.addWidget(btn_special)

        btn_letters = QPushButton("Letters")
        layout.addWidget(btn_letters)

        btn_digitz = QPushButton("Numbers")
        layout.addWidget(btn_digitz)

        def special_button_clicked():
            global characterlist
            characterlist += string.punctuation
            print("Succesful")
            print(f"characterlist: {characterlist}")


        def letters_button_clicked():
            global characterlist
            characterlist += string.ascii_letters
            print("Succesful")
            print(f"characterlist: {characterlist}")

        def numbers_button_clicked():
            global characterlist
            characterlist += string.digits
            print("Succesful")
            print(f"characterlist: {characterlist}")



        btn_digitz.clicked.connect(numbers_button_clicked)
        btn_special.clicked.connect(special_button_clicked)
        btn_letters.clicked.connect(letters_button_clicked)

        self._horizontal_group_box.setLayout(layout)


    def create_grid_group_box(self):
        self._grid_group_box = QGroupBox("Generation amount options")
        layout = QGridLayout()

        label1 = QLabel("Password Length: ")
        self.password_length_input = QLineEdit()

        label2 = QLabel("How many Passwords to generate: ")
        self.password_amount_input = QLineEdit()

        gen_pas = QPushButton("Generate")


        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.password_length_input, 0, 1)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(self.password_amount_input, 1, 1)
        layout.addWidget(gen_pas,0, 2)

        self._small_editor = QTextEdit()
        self._small_editor.setPlainText("Generated Passwords: ")

        layout.addWidget(self._small_editor, 2, 0, 1, 3)
        layout.setColumnStretch(1, 10)
        layout.setColumnStretch(2, 20)

        self._grid_group_box.setLayout(layout)

        def passwordgen():
            textpas = self.password_length_input.text()
            passwordam = self.password_amount_input.text()

            if not textpas.isdigit():
                print("Please Enter a number")
                return

            if not passwordam.isdigit():
                print("Please enter password amount")
                return

            length = int(textpas)
            passam = int(passwordam)

            print(f"password length is {length}")
            print(f"password amount is {passam}")

            if not characterlist:
                print("No characters set selected!")
                return

            passwords = []

            for i in range(passam):

                password = "".join(secrets.choice(characterlist)for i in range(length))
                passwords.append(password)

            self._small_editor.setPlainText("\n".join(passwords))

        gen_pas.clicked.connect(passwordgen)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dialog()
    sys.exit(dialog.exec())