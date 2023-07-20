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
