from pathlib import Path

from PySide6.QtQml import QQmlApplicationEngine
from __feature__ import snake_case, true_property   # noqa: E501


class MainEngine(QQmlApplicationEngine):
    VIEW_PATH = Path(__file__).resolve().parent / "views"

    def __init__(self):
        super().__init__()

        self.add_import_path(self.VIEW_PATH)

        self.ready = False
        self.objectCreated.connect(self.on_engine_created)

    def on_engine_created(self, obj, url):
        if obj is not None:
            self.ready = True

    def load(self, url):
        super().load(self.VIEW_PATH / url)
