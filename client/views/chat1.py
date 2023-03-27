from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTextEdit, QWidget)
import os

class ChatGPT(object):
    def setupUi(self, ChatGPT):
        if not ChatGPT.objectName():
            ChatGPT.setObjectName(u"ChatGPT")
        ChatGPT.resize(538, 580)
        #self.username1 = os.environ["USERNAME"]
        self.frame = QFrame(ChatGPT)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 538, 80))
        self.frame.setStyleSheet(u"background-color:#2F2D52")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 25, 241, 31))
        self.label.setStyleSheet(u"color:white;")
        self.Salir = QPushButton(self.frame)
        self.Salir.setObjectName(u"Salir")
        self.Salir.setGeometry(QRect(470, 0, 51, 51))
        self.Salir.setCursor(QCursor(Qt.PointingHandCursor))
        self.Salir.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"border-style: sold;\n"
"background-color:#bbdefb;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color:#0069c0;\n"
"}")
        icon = QIcon()
        icon.addFile(u"client/assets/salir.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Salir.setIcon(icon)
        self.Salir.setIconSize(QSize(60, 60))
        self.Salir.setFlat(True)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(470, 55, 49, 16))
        self.label_2.setStyleSheet(u"color:white;")
        self.ChatTextEdit = QTextEdit(ChatGPT)
        self.ChatTextEdit.setObjectName(u"ChatTextEdit")
        self.ChatTextEdit.setGeometry(QRect(0, 80, 538, 430))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.ChatTextEdit.setFont(font)
        #self.ChatTextEdit.setStyleSheet(u"background-color:#6C6A8B;\n"
#"color:white;")
        self.ChatTextEdit.setReadOnly(True)
        self.frame_2 = QFrame(ChatGPT)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 510, 538, 70))
        self.frame_2.setStyleSheet(u"background-color:white;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.messageLineEdit = QLineEdit(self.frame_2)
        self.messageLineEdit.setObjectName(u"messageLineEdit")
        self.messageLineEdit.setGeometry(QRect(20, 10, 400, 51))
        font1 = QFont()
        font1.setPointSize(10)
        self.messageLineEdit.setFont(font1)
        self.sendButton = QPushButton(self.frame_2)
        self.sendButton.setObjectName(u"sendButton")
        self.sendButton.setGeometry(QRect(440, 10, 71, 51))
        self.sendButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.sendButton.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"border-style: sold;\n"
"background-color:#bbdefb;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color:#0069c0;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"client/assets/send.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sendButton.setIcon(icon1)
        self.sendButton.setIconSize(QSize(60, 60))
        self.sendButton.setFlat(True)

        self.retranslateUi(ChatGPT)

        QMetaObject.connectSlotsByName(ChatGPT)
    # setupUi

    def retranslateUi(self, ChatGPT):
        ChatGPT.setWindowTitle(QCoreApplication.translate("ChatGPT", u"Form", None))
        self.label.setText(QCoreApplication.translate("ChatGPT", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">ChatGPT</span></p></body></html>", None))
        self.Salir.setText("")
        self.label_2.setText(QCoreApplication.translate("ChatGPT", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:700;\">Salir</span></p></body></html>", None))
        self.messageLineEdit.setPlaceholderText(QCoreApplication.translate("ChatGPT", u"Type sonthing to send...", None))
        self.sendButton.setText("")
#if QT_CONFIG(shortcut)
        self.sendButton.setShortcut(QCoreApplication.translate("ChatGPT", u"Return", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

