import logging
from .logger import *


_log_format = f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s((%lineno)d) - %(message)s"

logger = logging.getLogger(__name__)


def invalid_entire(function: str, text: str, path: str, line_no) -> None:
	description = f"Вы ввели некоректные данные: {text}"
	print(description)
	file_handler = logging.FileHandler("__logs__/error.log", encoding="utf-8")
	file_handler.baseFileName(path)
	file_handler.setLevel(logging.ERROR)
	file_handler.setFormatter(logging.Formatter(_log_format))
	return file_handler






