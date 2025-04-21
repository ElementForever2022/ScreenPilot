import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

# Create a basic window class
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Set window properties
        self.setWindowTitle("Simple Qt Demo")
        self.setGeometry(100, 100, 300, 200)

        # Create a button
        button = QPushButton("Click Me!", self)
        button.setGeometry(100, 80, 100, 40)
        button.clicked.connect(self.show_message)

    def show_message(self):
        QMessageBox.information(self, "Message", "Hello from PyQt5!")

# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
