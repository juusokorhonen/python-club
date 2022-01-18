from pathlib import Path
import sys

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from __feature__ import snake_case, true_property   # noqa: E501


def hello():
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    engine.load(Path(__file__).resolve().parent / "01_hello.qml")
    if not engine.root_objects():
        sys.exit(-1)
    sys.exit(app.exec())


if __name__ == "__main__":
    hello()
