
# Value error (ValueError)
def invalid_entire(text: str) -> str:
	description = f"Вы ввели некоректные данные: {text}"
	return description


# Attribute error (AttributeError)
def invalid_attribute(text: str) -> str:
	description = f"Вы пытаетесь вызвать не существующий параметр: {text}"
	return description


# IO error (IOError)
def invalid_IO(text: str) -> str:
	description = f"Не найден файл или диск заполнен: {text}"
	return description


# Import error (ImportError)
def invalid_import(text: str) -> str:
	description = f"Не получилось вызвать импорт: {text}"
	return description


# Index error (IndexError)
def invalid_index(text: str) -> str:
	description = f"Не найден индекс: {text}"
	return description


# Keyboard interrupt error (KeyboardInterrupt)
def invalid_kbi() -> str:
	description = "Процесс остановлен в ручную!"
	return description


# Variable not found (NameError)
def invalid_var(text: str) -> str:
	description = f"Переменная не найдена: {text}"
	return description


# Type error (TypeError)
def invalid_type(text: str) -> str:
	description = f"Неправильный тип данных: {text}"
	return description


# Zero division (ZeroDivisionError)
def invalid_zero_division(text: str) -> str:
	description = f"Ошибка деления на 0: {text}"
	return description

# General error (Exceptions)
def invalid_general(text: str) -> str:
	description = f"Ошибка в {text}"
	return description


