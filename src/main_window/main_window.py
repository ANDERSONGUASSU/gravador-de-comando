from PyQt5.QtWidgets import QMainWindow
from src.main_window.layout import setup_ui
from src.recording.recorder import Recorder


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.recorder = Recorder()
        setup_ui(self, self.recorder)
