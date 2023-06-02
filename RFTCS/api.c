#include "api.h"


// Api of flight trajectory
static PyObject * ext_double_angle_sine(PyObject *self, PyObject *args)
{
	float das = 0;
	if (!PyArg_ParseTuple(args, "f", &das)) return NULL;
	return PyLong_FromLong(api_double_angle_sine(das));
};

// static PyObject * ext_flight_range(PyObject *self, PyObject *args)
// {
// 	PyFloatObject * sine = 0;
// 	PyLongObject * speed = 0;
// 	if (!PyArg_ParseTuple(args, "fi", &sine, &speed)) return NULL;

// 	return Py_BuildValue("f", api_flight_range(sine, speed));
// };

// static PyObject * ext_flight_time(PyObject *self, PyObject *args)
// {
// 	PyLongObject * speed = 0;
// 	if (!PyArg_ParseTuple(args, "i", &speed)) return NULL;

// 	return PyFloatObject(api_flight_time(speed));
// };

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
