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

        # --- Initialisierung der GIF-Animation ---
        self.dragdrop_movie = qtg.QMovie("UI/Icons/gift-bag.gif")
        self.lb_dragdrop.setMovie(self.dragdrop_movie)

        # --- Events zuweisen ---
        self.lb_dragdrop.enterEvent = self.mouse_enter_dragdrop
        self.lb_dragdrop.leaveEvent = self.mouse_leave_dragdrop
        self.lb_dragdrop.dragEnterEvent = self.dragEnterEvent
        self.lb_dragdrop.dropEvent = self.dropEvent

        # --- Initial-Animation starten ---
        # NEU: Starte die Animation direkt beim Programmstart.
        self.dragdrop_movie.start()

        # NEU: Benutze einen QTimer, um die Animation nach 4 Sekunden zu stoppen.
        #      Wir rufen eine eigene Methode auf, um auch zum ersten Frame zurückzuspringen.
        qtc.QTimer.singleShot(4000, self.stop_initial_animation)

        # Dein restlicher Initialisierungs-Code
        self.le_input.setDisabled(True)
        self.lb_output_upper.setText("")
        self.lb_output_name.setText("")
        self.lb_output_success.setText("")

    # NEU: Eigene Methode zum Stoppen der Start-Animation
    def stop_initial_animation(self):
        """Stoppt die Animation und setzt sie auf den ersten Frame zurück."""
        self.dragdrop_movie.stop()
        self.dragdrop_movie.jumpToFrame(0)

    def mouse_enter_dragdrop(self, event: qtc.QEvent):
        """Startet die GIF-Animation."""
        self.dragdrop_movie.start()
        event.accept()

    def mouse_leave_dragdrop(self, event: qtc.QEvent):
        """Stoppt die GIF-Animation und setzt sie auf den Anfang zurück."""
        self.dragdrop_movie.stop()
        self.dragdrop_movie.jumpToFrame(0)
        event.accept()

    # --- Deine bestehenden Methoden bleiben unverändert ---

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
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event: qtg.QDropEvent):
        if event.mimeData().hasUrls():
            url = event.mimeData().urls()[0]
            file_path = url.toLocalFile()
            self.file_dropped(file_path)
            event.acceptProposedAction()


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())