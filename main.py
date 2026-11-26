
import sys

from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from qfluentwidgets import (
    FluentWindow,
    LineEdit,
    PrimaryPushButton,
    SubtitleLabel,
    BodyLabel,
    setTheme,
    Theme,
    FluentIcon
)


class HomeInterface(QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName("homeInterface")

        # Main layout
        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(15)

        # Heading
        title = SubtitleLabel("Welcome")
        layout.addWidget(title)

        description = BodyLabel("Test Window for CI/CD")
        layout.addWidget(description)

        # Fluent input field
        self.input_field = LineEdit()
        self.input_field.setPlaceholderText("Enter something...")
        self.input_field.setFixedWidth(300)
        layout.addWidget(self.input_field)

        # Fluent button
        button = PrimaryPushButton("Submit")
        button.setFixedWidth(120)
        layout.addWidget(button)

        # Output label
        self.output_label = BodyLabel("")
        layout.addWidget(self.output_label)

        # Connect button click
        button.clicked.connect(self.submit_text)

        layout.addStretch()

    def submit_text(self):
        text = self.input_field.text().strip()

        if text:
            self.output_label.setText(text)
            self.input_field.clear()


class MainWindow(FluentWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Desktop Application")
        self.resize(900, 600)

        self.home_interface = HomeInterface()

        # Add interface to navigation
        self.addSubInterface(
            self.home_interface,
            FluentIcon.HOME,
            "Home"
        )

        # Hide left sidebar
        self.navigationInterface.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    setTheme(Theme.AUTO)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())