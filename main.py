# Rafael Miranda Jimenez

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
import ping3

class PingApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Configuración de la ventana
        self.setWindowTitle("Ping App")
        self.setGeometry(100, 100, 300, 200)

        # Crear el layout
        layout = QVBoxLayout()

        # Etiqueta para el resultado
        self.result_label = QLabel("Ingrese una IP y presione Ping")
        layout.addWidget(self.result_label, alignment=Qt.AlignCenter)

        # Campo de texto para ingresar la IP
        self.ip_input = QLineEdit()
        self.ip_input.setPlaceholderText("Ingrese la dirección IP")
        layout.addWidget(self.ip_input)

        # Botón para ejecutar el ping
        self.ping_button = QPushButton("Ping")
        self.ping_button.clicked.connect(self.ping_ip)
        layout.addWidget(self.ping_button, alignment=Qt.AlignCenter)

        # Botón para alternar el estado del ping
        self.toggle_button = QPushButton("Denegar Ping")
        self.toggle_button.clicked.connect(self.toggle_ping)
        layout.addWidget(self.toggle_button, alignment=Qt.AlignCenter)

        # Configurar layout principal
        self.setLayout(layout)

        # Variable de control para el estado del ping
        self.ping_allowed = True  # Estado inicial: Ping permitido

    def ping_ip(self):
        # Verificar si el ping está permitido antes de intentar
        if self.ping_allowed:
            ip_address = self.ip_input.text()
            if ip_address:
                response_time = ping3.ping(ip_address)
                if response_time is not None:
                    self.result_label.setText(f"Ping exitoso! Tiempo de respuesta: {response_time:.4f} segundos")
                else:
                    self.result_label.setText("No se pudo hacer ping. El host no responde.")
            else:
                self.result_label.setText("Por favor, ingrese una dirección IP válida.")
        else:
            self.result_label.setText("El ping está actualmente denegado.")

    def toggle_ping(self):
        # Cambiar el estado del ping
        self.ping_allowed = not self.ping_allowed
        if self.ping_allowed:
            self.toggle_button.setText("Denegar Ping")
            self.result_label.setText("Ping permitido. Ingrese una IP y presione Ping.")
        else:
            self.toggle_button.setText("Permitir Ping")
            self.result_label.setText("Ping denegado.")

# Ejecutar la aplicación
app = QApplication(sys.argv)
window = PingApp()
window.show()
sys.exit(app.exec_())
