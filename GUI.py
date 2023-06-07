import sys
import Retriving_Data
from night_design import NightDesign
from day_design import DayDesign
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QHBoxLayout ,QMessageBox
from PyQt5.QtGui import QPixmap, QResizeEvent, QPalette ,QColor,QFont,QFontDatabase
from PyQt5.QtCore import Qt, pyqtProperty

LOCATION = ""

class MyDayApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("How's My Day")
        self.setGeometry(0, 0, 1600, 900)  # Set the initial window size

        # Set the background image
        self.bg_image = QLabel(self)
        self.bg_image.setScaledContents(True)  # Enable scaling of the background image
        self.updateBackgroundSize()  # Call the function to update the background size
        self.updateBackgroundImage()  # Call the function to update the background image

        #creating custom font
        # creating custom font
        font_id = QFontDatabase.addApplicationFont("final_font.ttf")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        font = QFont(font_family, 40)

        # Create the label
        welcome_label = QLabel("Welcome To", self)
        welcome_label.setObjectName("welcome_label")
        welcome_label.setStyleSheet("font-size: 60px; font-weight: bold; color: white;")
        welcome_label.setAlignment(Qt.AlignHCenter)  # Set the welcome label alignment to center horizontally

        # Create the label
        enter_label = QLabel("Please enter the Location", self)
        enter_label.setObjectName("enter_label")
        enter_label.setStyleSheet("font-size: 20px; font-weight: bold; color: white;")
        enter_label.setAlignment(Qt.AlignHCenter)  # Set the welcome label alignment to center horizontally

        # Create the label
        label = QLabel("How's My Day", self)
        label.setObjectName("label")
        label.setStyleSheet("font-size: 80px; font-weight: bold; color: white;")
        label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)  # Set the label alignment to center horizontally and top vertically

        # Create the input box
        self.input_box = QLineEdit(self)
        self.input_box.setFixedWidth(300)  # Set a fixed width for the input box
        self.input_box.setAlignment(Qt.AlignHCenter)  # Set the input box alignment to center horizontally

        # Create the enter button
        self.enter_button = QPushButton("Enter", self)
        self.enter_button.setStyleSheet("background-color: #87CEEB; color: white; border-radius: 10px;")
        self.enter_button.setFixedWidth(100)  # Set a fixed width for the button
        self.enter_button.clicked.connect(self.processData)  # Connect the button click to processData method

        # Set up the layout
        layout = QVBoxLayout()
        layout.addStretch(1)  # Add a stretchable space at the top
        layout.addWidget(welcome_label)  # Add the welcome label to the layout
        layout.addWidget(label)  # Add the label to the layout
        layout.addWidget(enter_label)  # Add the enter label to the layout
        layout.addSpacing(10)  # Add spacing between the labels and the input box

        input_button_layout = QHBoxLayout()  # Create a horizontal layout for the input box and button
        input_button_layout.addStretch(1)  # Add a stretchable space to the left
        input_button_layout.addWidget(self.input_box)  # Add the input box to the layout
        input_button_layout.addWidget(self.enter_button)  # Add the enter button to the layout
        input_button_layout.addStretch(1)  # Add a stretchable space to the right

        layout.addLayout(input_button_layout)  # Add the input box and button layout to the main layout
        layout.addStretch(1)  # Add a stretchable space at the bottom
        self.setLayout(layout)

        self.show()

    def resizeEvent(self, event: QResizeEvent):
        new_size = event.size()  # Get the new size of the window
        if new_size == self.size():  # Check if the new size is the same as the current size
            return  # Return from the function if the sizes are the same

        self.updateBackgroundSize()  # Call the function to update the background size
        self.updateBackgroundImage()  # Call the function to update the background image
        self.updateLabelSizes()  # Call the function to update the label sizes

    def updateBackgroundSize(self):
        window_size = self.size()  # Get the current window size
        self.bg_image.setGeometry(0, 0, window_size.width(), window_size.height())  # Set the background size

    def updateBackgroundImage(self):
        pixmap = QPixmap("Final Background.png")  # Load the background image
        self.bg_image.setPixmap(pixmap)  # Set the background image

    def updateLabelSizes(self):
        window_size = self.size()  # Get the current window size

        # Calculate the new font sizes based on the window height
        welcome_font_size = window_size.height() // 15
        enter_font_size = window_size.height() // 45
        label_font_size = window_size.height() // 11

        # Update the font sizes for the labels
        self.findChild(QLabel, "welcome_label").setStyleSheet(f"font-size: {welcome_font_size}px; font-weight: bold; color: white;")
        self.findChild(QLabel, "enter_label").setStyleSheet(f"font-size: {enter_font_size}px; font-weight: bold; color: white;")
        self.findChild(QLabel, "label").setStyleSheet(f"font-size: {label_font_size}px; font-weight: bold; color: white;")

    def hide(self):
        self.close()

    def processData(self):
        global LOCATION  # Declare the global variable
        LOCATION = self.input_box.text()  # Save the value of the input box into the global variable

        if not Retriving_Data.valid(LOCATION):  # Check if the location is valid using the valid() function
            # Show an error message box
            error_box = QMessageBox()
            error_box.setIcon(QMessageBox.Warning)
            error_box.setWindowTitle("Error")
            error_box.setText("Not a valid location.")
            error_box.setStandardButtons(QMessageBox.Ok)
            error_box.exec_()

            # Clear the input box and prompt the user for a new location
            self.input_box.clear()
            self.input_box.setFocus()
        else:
            # Disconnect the resizeEvent temporarily
            self.resizeEvent = lambda event: None

            # Perform further actions if the location is valid
            night_design = NightDesign()
            # Retrieve necessary data for NightDesign (e.g., temperature, weather condition)
            temp = "temp"
            temp_max = "temp_max"
            temp_min = "empty"
            name = "empty"
            date = "empty"
            wind = "empty"
            weth = "empty"
            night_window = night_design.invoke(temp, temp_max, temp_min, name, date, wind, weth)
            self.hide()
            night_window.show()

            # Reconnect the resizeEvent
            self.resizeEvent = self.originalResizeEvent

    @pyqtProperty(QColor)
    def color(self):
        return self.enter_button.palette().button().color()

    @color.setter
    def color(self, value):
        palette = self.enter_button.palette()
        palette.setColor(QPalette.Button, value)
        self.enter_button.setPalette(palette)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myday_app = MyDayApp()
    sys.exit(app.exec_())
