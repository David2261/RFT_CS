

def invalid_entire(text: str) -> str:
	""" Value error (ValueError) """
	description = f"Вы ввели некоректные данные: {text}"
	return description


def invalid_attribute(text: str) -> str:
	""" Attribute error (AttributeError) """
	description = f"Вы пытаетесь вызвать не существующий параметр: {text}"
	return description


def invalid_IO(text: OSError) -> str:
	""" IO error (IOError) """
	description = f"Не найден файл или диск заполнен: {text}"
	return description


def invalid_import(text: ImportError) -> str:
	""" Import error (ImportError) """
	description = f"Не получилось вызвать импорт: {text}"
	return description


def invalid_file(text: FileNotFoundError) -> str:
	""" Import error (FileNotFoundError) """
	description = f"Не получилось найти файл: {text}"
	return description


def invalid_index(text: IndexError) -> str:
	""" Index error (IndexError) """
	description = f"Не найден индекс: {text}"
	return description


def invalid_kbi() -> str:
	""" Keyboard interrupt error (KeyboardInterrupt) """
	description = "Процесс остановлен в ручную!"
	return description


def invalid_var(text: str) -> str:
	""" Variable not found (NameError) """
	description = f"Переменная не найдена: {text}"
	return description


def invalid_type(text: TypeError) -> str:
	""" Type error (TypeError) """
	description = f"Неправильный тип данных: {text}"
	return description


def invalid_zero_division(text: ZeroDivisionError) -> str:
	""" Zero division (ZeroDivisionError) """
	description = f"Ошибка деления на 0: {text}"
	return description


def invalid_general(text: Exception) -> str:
	""" General error (Exceptions) """
	description = f"Ошибка в {text}"
	return description
