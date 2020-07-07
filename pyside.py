import sys
import random
from PySide2 import QtCore, QtWidgets, QtGui
TIMES = [
    {
        'text': '5 minutos',
        'time': 5
    },
    {
        'text': '15 minutos',
        'time': 15
    },
    {
        'text': '30 minutos',
        'time': 30
    },
    {
        'text': '1 hora',
        'time': 60
    },
]


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.word = 'Naturaleza'
        self.time_text = '5 minutos'
        self.hello = ['Hola Mundo', 'Hello World']
        self.button = QtWidgets.QPushButton('GUARDAR')
        self.text1 = QtWidgets.QLabel('Imagenes Sobre:')
        self.textbox1 = QtWidgets.QLineEdit(self)
        self.textbox1.setPlaceholderText(self.word)
        self.text2 = QtWidgets.QLabel('Cambiar cada:')
        self.combobox1 = QtWidgets.QComboBox(self)

        for time in TIMES:
            self.combobox1.addItem(time['text'])

        self.combobox1.currentIndexChanged.connect(
            self.selectionCombobox1Change
        )

        self.layout = QtWidgets.QBoxLayout(
            QtWidgets.QBoxLayout.Direction.TopToBottom
        )
        self.layout.addWidget(self.text1)
        self.layout.addWidget(self.textbox1)
        self.layout.addWidget(self.text2)
        self.layout.addWidget(self.combobox1)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        self.button.clicked.connect(self.save)

    def selectionCombobox1Change(self, i):
        print('hello')

    def save(self):
        if len(self.textbox1.text()) > 0:
            self.word = self.textbox1.text()
        self.time_text = self.combobox1.currentText()
        self._execute_cron()

    def _execute_cron(self):
        # executing cron
        print('hello')


def main():
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    widget.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
