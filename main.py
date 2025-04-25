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
        # cores do certo e errado
        cor_certo ="""
        QLabel{
        background-color: #78E750;
        border: 4px solid #000000;
        }"""
        cor_parcial ="""
        QLabel{
	        background-color: #FFD633;
	        border: 4px solid #000000;
        }"""
        cor_errado ="""
        QLabel{
        background-color: #FF2D2D;
        border: 4px solid #000000;
        }"""

        self.certo_errado(nomeInput,cor_certo)
        
        """
            else:
                poderVerific = False
                coresVerific = False
                generoVerific = False

                if altura > self.alienAlvo['altura']:
                    caminhoImagem = "assets/setaBaixo.png"
                    pixmap = QPixmap(caminhoImagem)
                    self.ui.label_Altura.setPixmap(pixmap)
                    self.ui.label_Altura.setStyleSheet(cor_errado)

                elif altura < self.alienAlvo['altura']:
                    caminhoImagem = "assets/setaCima.png"
                    pixmap = QPixmap(caminhoImagem)
                    self.ui.label_Altura.setPixmap(pixmap)
                    self.ui.label_Altura.setStyleSheet(cor_errado)

                else:
                    self.ui.label_Altura.setStyleSheet(cor_certo)  
                    pixmap = QPixmap(None)
                    self.ui.label_Altura.setPixmap(pixmap)

                # Poder

                for poderAlien in poder:
                    if poderVerific == False:
                        if poderAlien in self.alienAlvo['poder']:
                            poderVerific = True
                    else:
                        break

                if len(self.alienAlvo['poder']) > 1:
                    if len(poder) > 1:
                        if poderVerific == False:
                            self.ui.label_Poder.setStyleSheet(cor_errado)
                        else:
                            self.ui.label_Poder.setStyleSheet(cor_parcial)
                    else:
                        if poderVerific == False:
                            self.ui.label_Poder.setStyleSheet(cor_errado)
                        else:
                            self.ui.label_Poder.setStyleSheet(cor_parcial)

                else:
                    if len(poder) > 1:
                        if poderVerific == False:
                            self.ui.label_Poder.setStyleSheet(cor_errado)
                        else:
                            self.ui.label_Poder.setStyleSheet(cor_parcial)
                    else:
                        if poderVerific == False:
                            self.ui.label_Poder.setStyleSheet(cor_errado)
                        else:
                            self.ui.label_Poder.setStyleSheet(cor_certo)

                poderVerific = False

                ## Cores

                for corAlien in cores:
                    if coresVerific == False:
                        if corAlien in self.alienAlvo['cores']:
                            coresVerific = True
                    else:
                        break

                if len(self.alienAlvo['cores']) > 1:
                    if len(cores) > 1:
                        if coresVerific == False:
                            self.ui.label_Cores.setStyleSheet(cor_errado)
                        else:
                            self.ui.label_Cores.setStyleSheet(cor_parcial)
                    else:
                        if coresVerific == False:
                            self.ui.label_Cores.setStyleSheet(cor_errado)
                        else:
                            self.ui.label_Cores.setStyleSheet(cor_parcial)
                else:
                    if len(cores) > 1:
                        if coresVerific == False:
                            self.ui.label_Cores.setStyleSheet(cor_errado)
                        else:
                            self.ui.label_Cores.setStyleSheet(cor_parcial)
                    else:
                        if coresVerific == False:
                            self.ui.label_Cores.setStyleSheet(cor_errado)
                        else:
                            self.ui.label_Cores.setStyleSheet(cor_certo)

                coresVerific = False

                # Genero

                for generoAlien in genero:
                    if generoVerific == False:
                        if generoAlien in self.alienAlvo['genero']:
                            generoVerific = True
                    else:
                        break

                if len(self.alienAlvo['genero']) > 1:
                    if len(genero) > 1:
                        if generoVerific == False:
                            self.ui.label_Genero.setStyleSheet(cor_errado)
                        else:
                            self.ui.label_Genero.setStyleSheet(cor_parcial)
                    else:
                        if generoVerific == False:
                            self.ui.label_Genero.setStyleSheet(cor_errado)
                        else:
                            self.ui.label_Genero.setStyleSheet(cor_parcial)
                else:
                    if len(genero) > 1:
                        if generoVerific == False:
                            self.ui.label_Genero.setStyleSheet(cor_errado)
                        else:
                            self.ui.label_Genero.setStyleSheet(cor_parcial)
                    else:
                        if generoVerific == False:
                            self.ui.label_Genero.setStyleSheet(cor_errado)
                        else:
                            self.ui.label_Genero.setStyleSheet(cor_certo)

                generoVerific = False

                if origem == self.alienAlvo['origem']:
                    self.ui.label_Origem.setStyleSheet(cor_certo)
                else:
                    self.ui.label_Origem.setStyleSheet(cor_errado)

                if primeiraAparicao == self.alienAlvo['primeiraAparicao']:
                    self.ui.label_PA.setStyleSheet(cor_certo)
                else:
                    self.ui.label_PA.setStyleSheet(cor_errado)

        else:
            QMessageBox.warning(self, "Erro", "Nome inválido")"""

    def certo_errado(self,nome,cor):
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
            
            pixmap = QPixmap(imagemAlien)
            self.ui.label_Alien.setPixmap(pixmap)
            self.ui.label_Genero_text.setText(f"{', '.join(genero)}")
            self.ui.label_Poder_text.setText(f"{', '.join(poder)}")
            self.ui.label_Cores_text.setText(f"{', '.join(cores)}")
            self.ui.label_Altura_text.setText(f"{altura}m")
            self.ui.label_Origem_text.setText(f"{origem}")
            self.ui.label_PA_text.setText(f"{primeiraAparicao}")

            if nome == self.alienAlvo['nome']:

                self.ui.label_Genero.setStyleSheet(cor)
                self.ui.label_Poder.setStyleSheet(cor)
                self.ui.label_Cores.setStyleSheet(cor)
                self.ui.label_Altura.setStyleSheet(cor)
                self.ui.label_Origem.setStyleSheet(cor)
                self.ui.label_PA.setStyleSheet(cor)
                pixmap = QPixmap(None)
                self.ui.label_Altura.setPixmap(pixmap)
            else:
                self.verificaraltura()

    def verificaaltura(self.)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())