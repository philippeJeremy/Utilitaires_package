import logging


class ColoredFormatter(logging.Formatter):
    COLORS = {
        logging.DEBUG: "\033[90m",     # gris
        logging.INFO: "\033[92m",      # vert
        logging.WARNING: "\033[93m",   # jaune
        logging.ERROR: "\033[91m",     # rouge
        logging.CRITICAL: "\033[95m",  # magenta
    }
    RESET = "\033[0m"

    def format(self, record):
        message = super().format(record)
        color = self.COLORS.get(record.levelno, self.RESET)
        return f"{color}{message}{self.RESET}"