from pathlib import Path
from timestamp import timestamp

class BackUp:

    BACK_UP_DIR = Path(__file__).parent.parent / "backup_directory"

    def __init__(self, raw_path):
        self._raw_path = raw_path

    @property
    def raw_path(self):
        return self.raw_path

    @raw_path.setter
    def raw_path(self, value):
        if isinstance(value, Path):
            self._raw_path = str(value)
        elif isinstance(value, str):
            self._raw_path = value
        else:
            raise TypeError("raw_path muss str oder Path Objekt sein!")

    @property
    def path(self):
        return Path(self._raw_path)

    @property
    def prefix_date_time(self):
        return f"[{timestamp(4)}]"

    def is_file(self) -> bool | None:
        if self.path.is_file():
            return True
        elif self.path.is_dir():
            return False
        else:
            return None

    @property
    def backup_name(self) -> str:
        return f"{self.prefix_date_time}__{self.path.name}"

    def show_suffix(self) -> str | None:
        if self.is_file():
            return self.path.suffix.replace(".", "")
        else:
            return None

    def show_info(self) ->str:
        return f"raw path:\t\t{self.raw_path}\nPath object:\t{self.path}\nbackup name:\t{self.backup_name}\nis a file:\t\t{self.is_file()}\ndata type:\t\t{self.show_suffix()}"


if __name__ == "__main__":
    b1 = BackUp(r"C:\Users\Ismail\Pictures\Screenshots")
    print(b1.show_info())
    print(BackUp.BACK_UP_DIR)
