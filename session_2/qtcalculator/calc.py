import sys

from .application_window import ApplicationWindow


def calc():
    app = ApplicationWindow()
    sys.exit(app.exec())
