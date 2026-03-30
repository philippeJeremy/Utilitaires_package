from pathlib import Path
from typing import Union
import shutil
import logging
from .exceptions import FileAlreadyExistsError, InvalidModeError
from .types import PathLike


class FileManager:
    def __init__(self, overwrite: bool = False, auto_rename: bool = True, logger: logging.Logger | None = None,):
        self.overwrite = overwrite
        self.auto_rename = auto_rename
        self.logger = logger or logging.getLogger(__name__)

    def _resolve_destination(self, destination: Path) -> Path:
        if not destination.exists():
            return destination

        if self.overwrite:
            return destination
        
        if not self.auto_rename:
            raise FileAlreadyExistsError(f"Fichier existe déjà : {destination}") 
        
        counter = 1 
        stem = destination.stem
        suffix = destination.suffix

        while True:
            new_name = f"{stem}_{counter}{suffix}"
            new_path = destination.with_name(new_name)

            if not new_path.exists():
                return new_path

            counter += 1

    def rename(self, file_path: PathLike, new_name: str) -> Path:
        source = Path(file_path)

        if not source.is_file():
            raise FileNotFoundError(f"Fichier introuvable : {source}")

        source_ext = source.suffix

        new_path = Path(new_name)

        # Nettoyage intelligent
        name = new_path.name

        # Si l'extension d'origine est déjà dedans → on l'enlève
        if source_ext in name:
            name = name.replace(source_ext, "")

        # Nettoyage des points finaux
        name = name.rstrip(".")

        final_name = f"{name}{source_ext}"

        destination = self._resolve_destination(source.with_name(final_name))

        source.rename(destination)
        self.logger.info(f"Renamed: {source} -> {destination}")

        return destination
    
    def transfer(self, source_path: PathLike, destination_path: PathLike, mode: str = 'copy') -> Path:

        source = Path(source_path)
        destination = Path(destination_path)

        if not source.is_file():
            raise FileNotFoundError(f"Source introuvable : {source}")
        
        if destination.exists() and destination.is_dir():
            destination = destination / source.name

        destination = self._resolve_destination(destination)

        if mode == "move":
            shutil.move(str(source), str(destination))
            self.logger.info(f"Moved: {source} -> {destination}")
        elif mode == "copy":
            shutil.copy2(source, destination)
            self.logger.info(f"Copied: {source} -> {destination}")
        else:
            raise InvalidModeError(mode)
        
        return destination
