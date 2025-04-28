import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtCore import QTimer, Qt


class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Trollagem CMD")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.botao_criar_cmds = QPushButton("Iniciar CMD Fake", self)
        self.botao_criar_cmds.clicked.connect(self.criar_cmds)

        layout.addWidget(self.botao_criar_cmds)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def criar_cmds(self):
        self.janelas_cmd = []
        for i in range(10):  # Criar 10 janelas
            janela = JanelaCMD(i + 1)
            
            # Gera posição aleatória na tela
            pos_x = random.randint(0, 1000)
            pos_y = random.randint(0, 600)
            janela.move(pos_x, pos_y)

            janela.show()
            self.janelas_cmd.append(janela)
            # Fecha depois de 35 segundos
            QTimer.singleShot(35000, janela.close)


class JanelaCMD(QMainWindow):
    def __init__(self, numero):
        super().__init__()
        self.setWindowTitle(f"C:\\Windows\\System32\\cmd.exe")
        self.setFixedSize(500, 300)  # Tamanho fixo padrão de um cmd aberto

        # Estilo de terminal
        self.setStyleSheet("""
            background-color: black;
            color: lime;
            font-family: Consolas, monospace;
            font-size: 13px;
        """)

        layout = QVBoxLayout()

        # Texto fake
        texto = QLabel(f"""
Microsoft Windows [Versão 10.0.19045.3086]
(c) Microsoft Corporation. Todos os direitos reservados.

C:\\Users\\ADM> Clonando Sistema {numero}...
C:\\Users\\ADM> Transferindo dados confidenciais...
C:\\Users\\ADM> Processando...
        """)
        texto.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        layout.addWidget(texto)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela_principal = JanelaPrincipal()
    janela_principal.show()
    sys.exit(app.exec_())
