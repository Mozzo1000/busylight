import sys
import os
from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QApplication, QPushButton, QWidget, QColorDialog, QAction, qApp, QLabel, QVBoxLayout, QComboBox
from gui.settings import SettingsWindow
from com.connection import Connection
from com.commands import LightCommands
from com.devices import Devices

class Gui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Busylight Interface')

        layout = QVBoxLayout()
        layout_header = QHBoxLayout()
        main_widget = QWidget()
        layout.setContentsMargins(0, 0, 0, 0)

        device_label = QLabel(self)
        device_label.setText("Connected to: ")
        layout_header.addWidget(device_label)

        self.device_selection = QComboBox(self)
        for i in Devices().list:
            self.device_selection.addItem(i)
        self.device_selection.activated[str].connect(self.device_selected)
        self.selected_device = self.device_selection.currentText()

        layout_header.addWidget(self.device_selection)

        button_busy = QPushButton("Busy", self)
        button_busy.clicked.connect(self.click_busy)

        button_away = QPushButton("Away", self)
        button_away.clicked.connect(self.click_away)

        button_available = QPushButton("Free", self)
        button_available.clicked.connect(self.click_available)

        layout.addLayout(layout_header)
        layout.addWidget(button_busy)
        layout.addWidget(button_away)
        layout.addWidget(button_available)

        color_button = QPushButton("Custom color", self)
        color_button.clicked.connect(self.on_click_color)
        layout.addWidget(color_button)
        
        self.setCentralWidget(main_widget)
        main_widget.setLayout(layout)

        settings_action = QAction('&Settings', self)
        settings_action.setShortcut('Ctrl+P')
        settings_action.setStatusTip('Open settings')
        settings_action.triggered.connect(self.open_settings)

        exit_action = QAction('&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(qApp.quit)

        menubar = self.menuBar()

        file_menu = menubar.addMenu('&File')
        file_menu.addAction(settings_action)
        file_menu.addAction(exit_action)

        self.show()

    def device_selected(self, i):
        self.selected_device = i

    def click_away(self):
        conn = Connection(self.selected_device, 115200)
        conn.send_command(LightCommands().set_color(b'0xfffa00'))

    def click_busy(self):
        conn = Connection(self.selected_device, 115200)
        conn.send_command(LightCommands().set_color(b'0xff0200'))
    
    def click_available(self):
        conn = Connection(self.selected_device, 115200)
        conn.send_command(LightCommands().set_color(b'0x0bff07'))

    def open_settings(self):
        settings = SettingsWindow(self)
        settings.show()

    def on_click_color(self):
        color = QColorDialog.getColor()

        if color.isValid():
            print(str.encode(color.name().replace("#", "0x")))
            conn = Connection(self.selected_device, 115200)
            conn.send_command(LightCommands().set_color(str.encode(color.name().replace("#", "0x"))))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = Gui()
    sys.exit(app.exec_())