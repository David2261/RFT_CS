# Расширение Python с помощью C
*Для оптимизации функций связанных с вычислением.*

## Общие сведения
_Для поддержки расширений Python API (программный интерфейс приложения) определяет набор функций, макросов и переменных, которые обеспечивают доступ к большинству аспектов Python системы времени выполнения. API Python включается в исходный файл C путем включения "Python.h" заголовка._

## Этапы создания API
1. В начале напишим функцию на языке Си для вычисления *Синуса двойного угла*, который принимает 1 параметр с типом float:
```c
float api_double_angle_sine(float speed)
{
	/* Синус двойного угла */
	float x = 2 * sin(speed) * cos(speed);
	x = (x < 0) ? -x : x;
	return x;
}
```

2. Создадим заголовочный файл формата .h:
```h
#ifndef RFT_CS_RFTCS_CORE_API_H_ // Путь к данному файлу
#define RFT_CS_RFTCS_CORE_API_H_ // Путь к данному файлу
#define PY_SSIZE_T_CLEAN
#include <Python.h> // Обязательно выше всех других импортов
#include <stdio.h>

#if PY_MAJOR_VERSION >= 3

// Место где находиться наша функция синуса двойного угла
#include "core/trajectory.h"

static PyObject * ext_double_angle_sine(PyObject *, PyObject *);

#endif

#endif // RFT_CS_RFTCS_CORE_API_H_ // Путь к данному файлу
```

3. Создадим функцию инициализации данной функции для API:
```c
static PyObject * ext_double_angle_sine(PyObject *self, PyObject *args)
{
	float das = 0;
	if (!PyArg_ParseTuple(args, "f", &das)) return NULL;
	return PyLong_FromLong(api_double_angle_sine(das));
};
```
- static PyObject - Данный тип содержит информацию, необходимую Python для обработки указателя на объект как объекта.
- PyArg_ParseTuple - Анализирует параметры функции, которая принимает только позиционные параметры в локальные переменные.
- PyLong_FromLong - Текущая реализация хранит массив целочисленных объектов для всех целых чисел между -5 и 256, когда вы создаете int в этом диапазоне, вы фактически просто получаете обратно ссылку на существующий объект.

4. Создадим структуру для описания метода типа расширения:
```c
static PyMethodDef methods[] = {
	{"ext_double_angle_sine", ext_double_angle_sine, METH_VARARGS, "ext_double_angle_sine"},
	{NULL, NULL, 0, NULL}
};
```
- PyMethodDef - Структура, используемая для описания метода типа расширения. У данной структуры есть четыре поля:

|   Поле   |     C тип    | Смысл |
| --------- | ------------ | ----- |
| ml_name  | const char * | имя метода |
| ml_meth  | PyCFunction  | указатель на C реализацию |
| ml_flags |      int     | биты флага, указывающие, как должен быть построен вызов |
| ml_doc   | const char * | указывает на содержимое докстринга |

- ml_meth — это указатель на функцию C
- Поле ml_flags — это битовое поле, которое может включать следующие флаги. Отдельные флаги указывают либо соглашение о вызовах, либо соглашение о привязке.

5. Нужно инициализовать модуль для API:
```c
static struct PyModuleDef module = {
	PyModuleDef_HEAD_INIT,
	"API_das",
	"API for double angle sine",
	-1,
	methods
};
```
- PyModuleDef - Структура определения модуля, которая содержит всю информацию, необходимую для создания объекта модуля. Обычно для каждого модуля существует только одна статически инициализированная переменная этого типа.
- PyModuleDef_Base m_base - Всегда инициализировать данный элемент как PyModuleDef_HEAD_INIT.
- const char *\*m_name* - Имя для нового модуля.
- const char *\*m_doc* - Строка документации для модуля; обычно используется переменная строки документации, созданная с помощью PyDoc_STRVAR.
- Py_ssize_t *m_size* - Состояние модуля может храниться в области памяти для каждого модуля, которую можно получить с помощью PyModule_GetState(), а не в статических глобальных объектах. Это делает модули безопасными для использования в нескольких субинтерпретаторах. Данная область памяти выделяется на основе m_size при создании модуля и освобождается при освобождении объекта модуля после вызова функции m_free, если таковая имеется. Установка m_size на -1 означает, что модуль не поддерживает субинтерпретаторы, поскольку у него есть глобальное состояние. Установка неотрицательного значения означает, что модуль можно повторно инициализировать, и указывает дополнительный объем памяти, необходимый для его состояния. Неотрицательный m_size требуется для многофазной инициализации.
- PyMethodDef *\*m_methods* - Указатель на таблицу функций уровня модуля, описанную значениями PyMethodDef. Может быть NULL, если нет функций.
- PyModuleDef_Slot *\*m_slots* - Массив определений слотов для многофазной инициализации, завершается записью {0, NULL}. При использовании однофазной инициализации m_slots должен быть NULL.


6. Создадим функцию инициализации функции модуля XD:
```c
PyMODINIT_FUNC
PyInit_ext_double_angle_sine(void) {
  return PyModule_Create(&module);
}

```
- PyMODINIT_FUNC PyInit_{name} - Инициализация функции модуля, вместо {name} - нужно написать имя функции
- PyTypeObject PyModule_Type - Экземпляр PyTypeObject представляет тип модуля Python. Он отображается в программах Python, как types.ModuleType.

7. Создадим файл setup.py, со следующим содержанием:
```py
from distutils.core import setup, Extension


setup(
	name="RFTCS_Core",
	version="1.0.1",
	description="Extend core on the C code",
	author="Bulat",
	ext_modules=[
		Extension("API_das", ["api.c"])
	]
)
```
- Extension - должна содержать имя модуля и путь к нему.

8. Добавим модуль в необходимый нам файл:
```py
import API_das as CA 
a = CA(360.0)
```

9. Запустим компиляцию для модуля написаного на Си:
```bash
python3.11 setup.py build_ext --inplace
```

## Конечный вид Си файла
```c
#include "api.h"


// Api of flight trajectory
static PyObject * ext_double_angle_sine(PyObject *self, PyObject *args)
{
	float das = 0;
	if (!PyArg_ParseTuple(args, "f", &das)) return NULL;
	return PyLong_FromLong(api_double_angle_sine(das));
};

static PyMethodDef methods[] = {
	{"ext_double_angle_sine", ext_double_angle_sine, METH_VARARGS, "ext_double_angle_sine"},
	{NULL, NULL, 0, NULL}
};

static struct PyModuleDef module = {
	PyModuleDef_HEAD_INIT,
	"API_das",
	"API for double angle sine",
	-1,
	methods
};

PyMODINIT_FUNC
PyInit_ext_double_angle_sine(void) {
  return PyModule_Create(&module);
}
```
