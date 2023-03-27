from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt, QThread, Signal
from Config import config
from views.chat1 import ChatGPT
import openai
import os


class ChatWindow(QWidget, ChatGPT):
    def __init__(self):
        super().__init__()
        self.username = os.environ["USERNAME"]
        self.setupUi(self)
        openai.api_key = config.api_key

        self.connect()

        self.sendButton.clicked.connect(self.send_messages)
        # agregamos hojas de estilo a la ventana del chat
        self.ChatTextEdit.setStyleSheet("""
        QTextEdit {
            background-color: #6C6A8B;
            color: white;
            font-size: 16px;
        }.username {
            #color: blue;}
        """)

    def connect(self):
        self.Salir.clicked.connect(self.logout)

    def logout(self):
        self.login_window = ChatGPT()
        self.close()

    def receive_messages(self):
        message1 = self.messageLineEdit.text()
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": message1 + '\n'}])
        message2 = f"bot: {response.choices[0].message.content}"
        self.ChatTextEdit.append(message2)
        self.ChatTextEdit.setAlignment(Qt.AlignLeft)

    def send_messages(self):
        message = self.messageLineEdit.text()
        message = f"<span class='username'>{self.username}:</span> <span style='font-size: 14px'>{message}</span>"
        #message = f"{self.username}: {message}"
        self.ChatTextEdit.append(message)
        self.ChatTextEdit.setAlignment(Qt.AlignRight)

        # guardamos el mensaje del usuario en una variable
        user_message = self.messageLineEdit.text()

        # borramos el texto del QLineEdit
        self.messageLineEdit.clear()

        # llamamos a receive_messages en segundo plano,
        # para evitar bloquear la interfaz de usuario
        self.thread = ReceiveMessagesThread(self, user_message)
        self.thread.message_received.connect(self.receive_message_on_ui_thread)
        self.thread.start()

    def receive_message_on_ui_thread(self, message):
        self.ChatTextEdit.append(message)
        self.ChatTextEdit.setAlignment(Qt.AlignLeft)

class ReceiveMessagesThread(QThread):
    message_received = Signal(str)

    def __init__(self, parent=None, user_message=None):
        super().__init__(parent)
        self.user_message = user_message

    def run(self):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": self.user_message + '\n'}])
        message = f"bot: {response.choices[0].message.content}"
        self.message_received.emit(message)



