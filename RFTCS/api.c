#include "api.h"


// API of flight trajectory
static PyObject * ext_double_angle_sine(PyObject *self, PyObject *args)
{
	float das = 0;
	if (!PyArg_ParseTuple(args, "f", &das)) return NULL;
	return PyLong_FromLong(api_double_angle_sine(das));
};


static PyObject * ext_flight_range(PyObject *self, PyObject *args)
{
	float sine = 0, speed = 0;
	if (!PyArg_ParseTuple(args, "ff", &sine, &speed)) return NULL;
	return PyLong_FromLong(api_flight_range(sine, speed));
};


// static struct PyModuleDef module = {
// 	PyModuleDef_HEAD_INIT,
// 	"API_FR",
// 	"API for flight range",
// 	-1,
// 	methods
// };


static PyMethodDef methods[] = {
	{"ext_double_angle_sine", ext_double_angle_sine, METH_VARARGS, "ext_double_angle_sine"},
	{"ext_flight_range", ext_flight_range, METH_VARARGS, "ext_flight_range"},
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

PyMODINIT_FUNC
PyInit_ext_flight_range(void) {
  return PyModule_Create(&module);
}
