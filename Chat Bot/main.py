import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QTextBrowser
from backend import ChatBot
from threading import Thread


class ChatBotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.chatbot = ChatBot()

        # set window title and size
        self.setWindowTitle('Chat Bot')
        self.setMinimumSize(520, 390)

        # create widgets
        self.text_box = QTextBrowser(self)
        self.text_box.setGeometry(20, 20, 400, 300)

        self.user_input = QLineEdit(self)
        self.user_input.setPlaceholderText('Enter A Question')
        self.user_input.returnPressed.connect(self.send_query)
        self.user_input.setGeometry(20, 340, 400, 25)

        button = QPushButton('Send', self)
        button.clicked.connect(self.send_query)
        button.setGeometry(430, 340, 60, 25)

        self.show()

    def send_query(self):
        # display the user query
        user_input = self.user_input.text()
        self.text_box.append(f'<p>Me: {user_input}</p>')

        # clear the edit text box
        self.user_input.clear()

        # release a thread, the GUI will not get stuck
        Thread(target=self.get_bot_response, args=(user_input,)).start()

    def get_bot_response(self, user_input):
        """ Ask the bot a question and display the answer """

        answer = self.chatbot.get_response(user_input)
        self.text_box.append(f"<p style='font-weight: bold'>Bot: {answer}</p>")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = ChatBotWindow()
    sys.exit(app.exec())
