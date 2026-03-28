class FileUtilsError(Exception):
    """Base exception"""


class FileNotFoundError(FileUtilsError):
    pass


class InvalidModeError(FileUtilsError):
    pass


class FileAlreadyExistsError(FileUtilsError):
    pass