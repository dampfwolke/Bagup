import sys

from PySide6 import QtWidgets as qtw
from PySide6 import QtCore as qtc
from PySide6 import QtGui as qtg

from utils.backup import BackUp

from UI.frm_main_window import Ui_frm_main_window

class MainWindow(qtw.QMainWindow, Ui_frm_main_window):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.lb_dragdrop.dragEnterEvent = self.dragEnterEvent
        self.lb_dragdrop.dropEvent = self.dropEvent

        self.le_input.setDisabled(True)
        self.lb_output_upper.setText("")
        self.lb_output_name.setText("")
        self.lb_output_success.setText("")

    @qtc.Slot()
    def file_dropped(self, file_path):
        backup = BackUp(file_path)
        backup.create_file_backup()
        self.lb_output_upper.setText("Sicherung von")
        self.lb_output_name.setText(f"{backup.path.name}")
        self.lb_output_success.setText("wurde erfolgreich erstellt.")
        qtc.QTimer.singleShot(8000, lambda: self.lb_output_upper.clear())
        qtc.QTimer.singleShot(8000, lambda: self.lb_output_name.clear())
        qtc.QTimer.singleShot(8000, lambda: self.lb_output_success.clear())

    def dragEnterEvent(self, event: qtg.QDragEnterEvent):
        # Wir prüfen, ob die gezogenen Daten URLs enthalten (also z.B. Dateien).
        if event.mimeData().hasUrls():
            event.acceptProposedAction()  # Annehmen, der Mauszeiger ändert sich
        else:
            event.ignore()  # Ablehnen

    def dropEvent(self, event: qtg.QDropEvent):
        # Prüfen, ob URLs vorhanden sind
        if event.mimeData().hasUrls():
            # Die erste URL aus der Liste holen
            url = event.mimeData().urls()[0]
            # Die URL in einen lokalen Dateipfad umwandeln
            file_path = url.toLocalFile()
            # Den Pfad im anderen Label ausgeben
            # self.lb_output_name.setText(f"Datei: {file_path}")
            self.file_dropped(file_path)
            event.acceptProposedAction()


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())