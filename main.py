import sys
import json
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QAction, QPushButton, QCompleter, QMessageBox
from PyQt5.QtGui import QPixmap
from Ben10dle import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Ben10dle")
        self.aliensJson = "alines.json"
        self.carregarAliens()
        self.alienAlvo = self.definirAlien()
        self.nomeAliens = self.getNomes()

        self.completer = QCompleter(self.nomeAliens)
        self.completer.setCaseSensitivity(False)
        self.ui.lineEdit.setCompleter(self.completer)

        self.ui.pushButton_omnitrix.clicked.connect(self.testeBotao)

    def carregarAliens(self):
        try:
            with open(self.aliensJson, "r", encoding='UTF-8') as file:
                self.aliens = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.aliens = {}

    def definirAlien(self):
        return random.choice(self.aliens)
    
    def getNomes(self):
        listaNomes = []
        for i in self.aliens:
            nome = i['nome']
            listaNomes.append(nome)
        return listaNomes


    def testeBotao(self):
        nomeInput = self.ui.lineEdit.text().strip()
        print(self.alienAlvo)

        if nomeInput in self.nomeAliens:
            for i in self.aliens:
                if nomeInput == i['nome']:
                    genero = i['genero']
                    poder = i['poder']
                    cores = i['cores']
                    altura = i['altura']
                    origem = i['origem']
                    primeiraAparicao = i['primeiraAparicao']
            
            self.ui.label_Genero.setText(f"{', '.join(genero)}")
            self.ui.label_Poder.setText(f"{', '.join(poder)}")
            self.ui.label_Cores.setText(f"{', '.join(cores)}")

            self.ui.label_Altura.setText(f"{altura}")
            if altura > self.alienAlvo['altura']:

                print("acima")
                caminhoImagem = "testeB.png"
                pixmap = QPixmap(caminhoImagem)
                self.ui.label_Altura.setPixmap(pixmap)

            elif altura < self.alienAlvo['altura']:

                print("abaixo")
                caminhoImagem = "cima.png"
                pixmap = QPixmap(caminhoImagem)
                self.ui.label_Altura.setPixmap(pixmap)

            else:  
                print("acertou")

            
            self.ui.label_Origem.setText(f"{origem}")
            self.ui.label_PA.setText(f"{primeiraAparicao}")


            if nomeInput == self.alienAlvo['nome']:
                print("foi")
            else:
                print("num foi")
            
        else:
            QMessageBox.warning(self, "Erro", "Nome inválido")

                # self.ui.label_Altura.setStyleSheet("QLabel{\n"
                #                                     "    background-color: #FF2D2D\n"
                #                                     "    border: 4px solid #000000;\n"
                #                                     "}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())