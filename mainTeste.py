import sys
import json
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QAction, QPushButton
from teste import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.aliensJson = "alines.json"
        self.carregarAliens()
        self.alienAlvo = self.definirAlien()

        self.ui.pushButton.clicked.connect(self.testeBotao)

    def carregarAliens(self):
        try:
            with open(self.aliensJson, "r", encoding='UTF-8') as file:
                self.aliens = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.aliens = {}

    def definirAlien(self):
        return random.choice(self.aliens)

    def testeBotao(self):
        nomeInput = self.ui.lineEdit.text().strip().capitalize()
        print(self.alienAlvo)

        if nomeInput == self.alienAlvo['nome']:
            print("foi")
        else:
            print("num foi")
        for i in self.aliens:
            cont = 0
            nome = i['nome']
            genero = i['genero']
            poder = i['poder']
            cores = i['cores']
            altura = i['altura']
            origem = i['origem']
            primeiraAparicao = i['primeiraAparicao']

            # print(list(self.aliens))
            # print(f"Nome: {nome}\nGênero: {', '.join(genero)}\nPoder: {', '.join(poder)}\nCores: {', '.join(cores)}\nAltura: {altura}\nOrigem: {origem}\nPrimeira Aparição: {primeiraAparicao}")
            # for itens in i.items():
            #     self.ui.listWidget.addItem(f"{itens}")
        # for nome, telefone in self.aliens.items():
        #     self.ui.label.setText(f"{nome}: {telefone}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())