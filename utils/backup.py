from pathlib import Path
import shutil

from utils.timestamp import timestamp

class BackUp:

    BACK_UP_DIR = Path(__file__).parent.parent / "backup_directory"

    def __init__(self, source_path: str | Path):
        self._path: Path = Path(source_path)

    @property
    def path(self) -> Path:
        return self._path

    @property
    def raw_path(self) -> str:
        return str(self._path)

    @property
    def prefix_date_time(self) -> str:
        return f"[{timestamp(4)}]"

    @property
    def file_status(self) -> str | None:
        if self.path.is_file():
            return "file"
        elif self.path.is_dir():
            return "dir"
        elif not self.path.exists():
            return "not found"
        return None

    @property
    def backup_name(self) -> str:
        return f"{self.prefix_date_time}__{self.path.name}"

    def show_suffix(self) -> str | None:
        if self.file_status == "file":
            return self.path.suffix.lstrip(".")
        else:
            return None

    def classify_backup_file(self):
        pass

    def create_file_backup(self) -> None:
        source = self.path
        destination_dir = Path(self.BACK_UP_DIR) / self.show_suffix().upper()
        destination_dir.mkdir(exist_ok=True)
        destination = destination_dir / self.backup_name
        shutil.copy(source, destination)
        print(f"Backup von Datei '{self.path.name}' erfolgreich gespeichert! {timestamp(1)}")

    def __str__(self) ->str:
        return f"raw path:\t\t{self.raw_path}\nPath object:\t{self.path}\nbackup name:\t{self.backup_name}\nis a file:\t\t{self.file_status}\ndata type:\t\t{self.show_suffix()}"


if __name__ == "__main__":
    b1 = BackUp(r"C:\Users\Ismail\Pictures\Screenshots\Screenshot 2025-04-09 152956.png")
    print(b1)
    b1.create_file_backup()
