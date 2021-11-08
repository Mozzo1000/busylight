from PyQt5.QtWidgets import QMainWindow, QPushButton, QCheckBox, QFontDialog, QMessageBox, \
    QComboBox, QListWidget, QHBoxLayout, QWidget, QStackedWidget, QFormLayout, QLineEdit
from PyQt5.QtCore import QLine, QSize, QSettings

class SettingsWindow(QMainWindow):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle('Settings')

        self.settings = QSettings('busylight', 'app')

        self.main_widget = QWidget()
        self.layout = QHBoxLayout()

        self.stack_widget = QStackedWidget(self)

        self.general_widget = QWidget(self)
        self.general_ui()


        self.stack_widget.addWidget(self.general_widget)

        settings_list = QListWidget(self)
        settings_list.currentRowChanged.connect(self.switch_display)
        settings_list.insertItem(0, 'General')

        save_btn = QPushButton("Save", self)
        save_btn.setToolTip("Save settings")
        save_btn.clicked.connect(self.save_settings)

        self.layout.addWidget(settings_list)
        self.layout.addWidget(self.stack_widget)
        self.layout.addWidget(save_btn)
        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)

        self.load_settings()

    def general_ui(self):
        layout = QFormLayout()


        self.busy_color_input = QLineEdit(self)
        self.busy_color_picker = QPushButton("Busy color", self)

        layout.addRow(self.busy_color_input)
        layout.addRow(self.busy_color_picker)

        self.general_widget.setLayout(layout)

    def switch_display(self, i):
        self.stack_widget.setCurrentIndex(i)

    def load_settings(self):
        if self.settings.contains('busy_color'):
            self.show_preview_by_default.setCheckState(self.settings.value('default_preview'))
        else:
            self.settings.setValue('default_preview', 2)

    def save_settings(self):
        self.settings.setValue('default_preview', self.show_preview_by_default.checkState())

        QMessageBox.question(self, 'Info', 'Please restart the application for changes to take affect.', QMessageBox.Ok)