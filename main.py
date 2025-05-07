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
        self.aliensJson = "aliens.json"
        self.carregarAliens()
        self.alienAlvo = self.definirAlien()
        self.nomeAliens = self.getNomes()

        self.completer = QCompleter(self.nomeAliens)
        self.completer.setCaseSensitivity(False)
        self.ui.lineEdit.setCompleter(self.completer)

        self.ui.pushButton_omnitrix.clicked.connect(self.advinhar)

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
        

    def advinhar(self):
        nomeInput = self.ui.lineEdit.text().strip()
        print(self.alienAlvo)

        # Cores
        self.cor_certo = """
        QLabel{
            background-color: #78E750;
            border: 4px solid #000000;
        }"""
        self.cor_parcial = """
        QLabel{
            background-color: #FFD633;
            border: 4px solid #000000;
        }"""
        self.cor_errado = """
        QLabel{
            background-color: #FF2D2D;
            border: 4px solid #000000;
        }"""

        self.certo_errado(nomeInput)

    def certo_errado(self, nome):
        if nome in self.nomeAliens:
            for i in self.aliens:
                if nome == i['nome']:
                    genero = i['genero']
                    poder = i['poder']
                    cores = i['cores']
                    altura = i['altura']
                    origem = i['origem']
                    primeiraAparicao = i['primeiraAparicao']
                    imagemAlien = i['imagem']
                    break  # Quando encontrar, já pode parar o for

            pixmap = QPixmap(imagemAlien)
            self.ui.label_Alien.setPixmap(pixmap)
            self.ui.label_Genero_text.setText(f"{', '.join(genero)}")
            self.ui.label_Poder_text.setText(f"{', '.join(poder)}")
            self.ui.label_Cores_text.setText(f"{', '.join(cores)}")
            self.ui.label_Altura_text.setText(f"{altura}m")
            self.ui.label_Origem_text.setText(f"{origem}")
            self.ui.label_PA_text.setText(f"{primeiraAparicao}")

            if nome == self.alienAlvo['nome']:
                self.ui.label_Genero.setStyleSheet(self.cor_certo)
                self.ui.label_Poder.setStyleSheet(self.cor_certo)
                self.ui.label_Cores.setStyleSheet(self.cor_certo)
                self.ui.label_Altura.setStyleSheet(self.cor_certo)
                self.ui.label_Origem.setStyleSheet(self.cor_certo)
                self.ui.label_PA.setStyleSheet(self.cor_certo)
                self.ui.label_Altura.clear()  # Limpa a imagem da altura
            else:
                self.verificar_altura(altura)
                self.verificar_poder(poder)
                self.verificar_cores(cores)
                self.verificar_generos(genero)
                self.verificar_origem_E_aparição(origem,primeiraAparicao)
        else:
            QMessageBox.warning(self, "Erro", "Nome inválido")

    def verificar_altura(self, altura):
        if altura > self.alienAlvo['altura']:
            caminhoImagem = "assets/setaBaixo.png"
            pixmap = QPixmap(caminhoImagem)
            self.ui.label_Altura.setPixmap(pixmap)
            self.ui.label_Altura.setStyleSheet(self.cor_errado)
        elif altura < self.alienAlvo['altura']:
            caminhoImagem = "assets/setaCima.png"
            pixmap = QPixmap(caminhoImagem)
            self.ui.label_Altura.setPixmap(pixmap)
            self.ui.label_Altura.setStyleSheet(self.cor_errado)
        else:
            self.ui.label_Altura.setStyleSheet(self.cor_certo)
            self.ui.label_Altura.clear()
                    
                    
    def verificar_poder(self, poder):
        poderVerific = False

        for poderAlien in poder:
            if poderAlien in self.alienAlvo['poder']:
                poderVerific = True
                break 

        if len(self.alienAlvo['poder']) > 1:
            if poderVerific:
                self.ui.label_Poder.setStyleSheet(self.cor_parcial)
            else:
                self.ui.label_Poder.setStyleSheet(self.cor_errado)
        else: 
            if len(poder) > 1:
                if poderVerific:
                    self.ui.label_Poder.setStyleSheet(self.cor_parcial)
                else:
                    self.ui.label_Poder.setStyleSheet(self.cor_errado)
            else:
                if poderVerific:
                    self.ui.label_Poder.setStyleSheet(self.cor_certo)
                else:
                    self.ui.label_Poder.setStyleSheet(self.cor_errado)
    
    def verificar_cores(self, cores):
        coresVerific = any(cor in self.alienAlvo['cores'] for cor in cores)

        if len(self.alienAlvo['cores']) > 1:
            if coresVerific:
                self.ui.label_Cores.setStyleSheet(self.cor_parcial)
            else:
                self.ui.label_Cores.setStyleSheet(self.cor_errado)
        else:
            if len(cores) > 1:
                if coresVerific:
                    self.ui.label_Cores.setStyleSheet(self.cor_parcial)
                else:
                    self.ui.label_Cores.setStyleSheet(self.cor_errado)
            else:
                if coresVerific:
                    self.ui.label_Cores.setStyleSheet(self.cor_certo)
                else:
                    self.ui.label_Cores.setStyleSheet(self.cor_errado)

    def verificar_generos(self, generos):
        generoVerific = any(g in self.alienAlvo['genero'] for g in generos)
        # subistir por um mais eficiente e mais rapido 
        # generoVerific = False
        # for generoAlien in genero:
        #     if generoVerific == False:
        #         if generoAlien in self.alienAlvo['genero']:
        #             generoVerific = True
        #         else:
        #             break

        if len(self.alienAlvo['genero']) > 1:
            if generoVerific:
                self.ui.label_Genero.setStyleSheet(self.cor_parcial)
            else:
                self.ui.label_Genero.setStyleSheet(self.cor_errado)
        else:
            if len(generos) > 1:
                if generoVerific:
                    self.ui.label_Genero.setStyleSheet(self.cor_parcial)
                else:
                    self.ui.label_Genero.setStyleSheet(self.cor_errado)
            else:
                if generoVerific:
                    self.ui.label_Genero.setStyleSheet(self.cor_certo)
                else:
                    self.ui.label_Genero.setStyleSheet(self.cor_errado)


    def verificar_origem_E_aparição(self,origem,primeiraAparicao):
            
        if origem == self.alienAlvo['origem']:
            self.ui.label_Origem.setStyleSheet(self.cor_certo)
        else:
            self.ui.label_Origem.setStyleSheet(self.cor_errado)

        if primeiraAparicao == self.alienAlvo['primeiraAparicao']:
            self.ui.label_PA.setStyleSheet(self.cor_certo)
        else:
            self.ui.label_PA.setStyleSheet(self.cor_errado)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())