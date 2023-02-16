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
		METH_NOARGS,
		"flight_range"
	},
	{
		"flight_time",
		(PyCFunction)ext_flight_time,
		METH_NOARGS,
		"flight_time"
	},
};

static PyModuleDef core_mod = {
	PyModuleDef_HEAD_INIT,
	"core_api",
	"Core Api",
	-1,
	core_funcs,
	NULL,
	NULL,
	NULL,
	NULL,
};

PyMODINIT_FUNC PyInit_core(void) {
	return PyModule_Create(&core_mod);
}