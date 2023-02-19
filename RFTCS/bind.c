#include "api.h"


static PyMethodDef core_funcs[] = {
	{
		"double_angle_sine",
		(PyCFunction)ext_double_angle_sine,
		METH_NOARGS,
		"double_angle_sine"
	},
	{
		"flight_range",
		(PyCFunction)ext_flight_range,
		METH_VARARGS,
		"flight_range"
	},
	{
		"flight_time",
		(PyCFunction)ext_flight_time,
		METH_VARARGS,
		"flight_time"
	},
	{NULL, NULL, 0, NULL},
};

static PyModuleDef core_mod = {
	PyModuleDef_HEAD_INIT,
	"core_api",
	"Core Api",
	-1,
	core_funcs
};

PyMODINIT_FUNC PyInit_core_api(void) {
	return PyModule_Create(&core_mod);
}