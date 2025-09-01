import sys

from PySide6.QtWidgets import (QApplication, QComboBox, QDialog,
                               QDialogButtonBox, QGridLayout, QGroupBox,
                               QFormLayout, QHBoxLayout, QLabel, QLineEdit,
                               QMenu, QMenuBar, QPushButton, QSpinBox,
                               QTextEdit, QVBoxLayout)

class Counter(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Counter v0.01")
        self.setFixedSize(720,950)

    # def create_main_box(self):
    #     layout = QGridLayout()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = QDialog()
    sys.exit(dialog.exec())