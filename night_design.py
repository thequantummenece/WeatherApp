from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QFrame, QHBoxLayout, QGraphicsOpacityEffect
from PyQt5.QtGui import QPixmap, QFontDatabase, QFont, QPalette, QBrush
from PyQt5.QtCore import Qt

class NightDesign:
    def __init__(self):
        font_id = QFontDatabase.addApplicationFont("final_font.ttf")
        self.font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        self.label_temp = None

    def invoke(self, temp, temp_max, temp_min, name, date, wind, weth):
        window = QWidget()
        window.setWindowTitle("Night Design")
        window.resize(1600, 900)

        layout = QVBoxLayout()

        palette = window.palette()
        background_image = QPixmap("night_image.png")
        palette.setBrush(QPalette.Background, QBrush(background_image))
        window.setPalette(palette)

        label_frame = QFrame()
        label_layout = QVBoxLayout(label_frame)

        top_layout = QHBoxLayout()

        clipart = QLabel()
        pixmap = QPixmap("night_cloud.png")
        clipart.setPixmap(pixmap.scaled(300, 300, Qt.KeepAspectRatio))
        clipart.setAlignment(Qt.AlignTop)
        top_layout.addWidget(clipart)

        labels_layout = QVBoxLayout()

        glass_frame = QFrame()
        glass_frame.setStyleSheet("background-color: rgba(255, 255, 255, .15);")

        glass_layout = QVBoxLayout(glass_frame)

        name_label = QLabel(name)
        name_label.setAlignment(Qt.AlignLeft)
        name_label.setFont(QFont(self.font_family, 30))

        name_label_effect = QGraphicsOpacityEffect()
        name_label_effect.setOpacity(1)
        name_label.setGraphicsEffect(name_label_effect)
        name_label.setContentsMargins(0, 0, 0, 0)
        name_label.setStyleSheet("color: white; border: none; padding: 0px; margin: 0px;")

        glass_layout.addWidget(name_label)

        date_label = QLabel(date)
        date_label.setAlignment(Qt.AlignLeft)
        date_label.setFont(QFont(self.font_family, 16))

        date_label.setContentsMargins(0, 0, 0, 0)
        date_label.setStyleSheet("color: white; border: none; padding: 0px; margin: 0px;")

        glass_layout.addWidget(date_label)

        Temperature = "Temperature"
        self.label_temp = QLabel(
            f"<html><span style='font-size: 48px; font-family: {self.font_family};'>{Temperature}<br>{temp}<br></span><span style='font-size: 24px; font-family: {self.font_family};'>{temp_min}</span><br><span style='font-size: 24px; font-family: {self.font_family};'>{temp_max}</span></html>")
        self.label_temp.setAlignment(Qt.AlignLeft)

        temp_label_effect = QGraphicsOpacityEffect()
        temp_label_effect.setOpacity(1)
        self.label_temp.setGraphicsEffect(temp_label_effect)
        self.label_temp.setContentsMargins(0, 0, 0, 0)
        self.label_temp.setStyleSheet("color: white; border: none; padding: 0px; margin: 0px;")

        glass_layout.addWidget(self.label_temp)

        weth_label = QLabel(weth)
        weth_label.setAlignment(Qt.AlignLeft)
        weth_label.setFont(QFont(self.font_family, 16))

        weth_label_effect = QGraphicsOpacityEffect()
        weth_label_effect.setOpacity(1)
        weth_label.setGraphicsEffect(weth_label_effect)
        weth_label.setContentsMargins(0, 0, 0, 0)
        weth_label.setStyleSheet("color: white; border: none; padding: 0px; margin: 0px;")

        glass_layout.addWidget(weth_label)

        wind_label = QLabel(wind)
        wind_label.setAlignment(Qt.AlignLeft)
        wind_label.setFont(QFont(self.font_family, 16))

        wind_label_effect = QGraphicsOpacityEffect()
        wind_label_effect.setOpacity(1)
        wind_label.setGraphicsEffect(wind_label_effect)
        wind_label.setContentsMargins(0, 0, 0, 0)
        wind_label.setStyleSheet("color: white; border: none; padding: 0px; margin: 0px;")

        glass_layout.addWidget(wind_label)

        labels_layout.addWidget(glass_frame)

        top_layout.addLayout(labels_layout)
        label_layout.addLayout(top_layout)
        layout.addWidget(label_frame)
        window.setLayout(layout)

        def resizeEvent(event):
            bg_image = window.findChild(QLabel)
            bg_image.setPixmap(background_image.scaled(event.size(), Qt.KeepAspectRatio))

            font_size_temp = event.size().height() // 30
            font_temp = QFont(self.font_family, font_size_temp)
            self.label_temp.setFont(font_temp)

        window.resizeEvent = resizeEvent

        return window
