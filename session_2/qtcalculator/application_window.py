from PySide6.QtGui import QGuiApplication
from __feature__ import snake_case, true_property   # noqa: E501

from .main_engine import MainEngine


class ApplicationWindow(QGuiApplication):
    def __init__(self):
        super().__init__()

        self.engine = MainEngine()
        self.engine.load("main.qml")

    def exec(self):
        if not self.engine.ready:
            return -1
        return super().exec()
