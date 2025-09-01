import sys

from PySide6.QtWidgets import (QApplication, QComboBox, QDialog,
                               QDialogButtonBox, QGridLayout, QGroupBox,
                               QFormLayout, QHBoxLayout, QLabel, QLineEdit,
                               QMenu, QMenuBar, QPushButton, QSpinBox,
                               QTextEdit, QVBoxLayout, QMainWindow, QWidget, QSizePolicy)

from PySide6.QtGui import     (QFont)

from PySide6.QtCore import    (Qt)

class Counter(QMainWindow):

    def __init__(self):
        super().__init__()

        self.create_menu()
        self.create_main_box()

        self.setWindowTitle("Counter v0.01")
        self.setMinimumSize(1280,720)
        self.setMaximumSize(1920,1080)

        main_layout = QVBoxLayout()

        self.setLayout(main_layout)

    def create_menu(self):

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")
        exit_action = file_menu.addAction("E&xit")
        exit_action.triggered.connect(self.close)

    def create_main_box(self):

        central_widget = QWidget()
        layout = QHBoxLayout(central_widget)

        textbox1 = QLineEdit("0")
        textbox1.setSizePolicy(
            textbox1.sizePolicy().horizontalPolicy(),
            QSizePolicy.Expanding
        )
        fo = QFont()
        fo.setPointSize(50)
        textbox1.setFont(fo)
        textbox1.setAlignment(Qt.AlignCenter)

        layout.addWidget(textbox1, 19)

        label = QPushButton("Count!")
        label.setSizePolicy(
            label.sizePolicy().horizontalPolicy(),
            QSizePolicy.Expanding)

        layout.addWidget(label, 20)

        self.setCentralWidget(central_widget)

    def create_right_counter(self):

        right_widget = QWidget()
        layout = QGridLayout




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Counter()
    window.show()
    sys.exit(app.exec())