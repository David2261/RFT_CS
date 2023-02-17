#include "api.h"


// Api of flight trajectory
static PyObject * ext_double_angle_sine(PyObject *self)
{
	return PyNumber_Float(api_double_angle_sine());
};

static PyObject * ext_flight_range(PyObject *self, PyObject *args)
{
	float sine = 0;
	int speed = 0;
	if (!PyArg_ParseTuple(args, "fi", &sine, &speed)) return NULL;

	return PyNumber_Float(api_flight_range(sine, speed));
};

static PyObject * ext_flight_time(PyObject *self, PyObject *args)
{
	int speed = 0;
	if (!PyArg_ParseTuple(args, "i", &speed)) return NULL;

	return PyNumber_Float(api_flight_time(speed));
};

static PyObject * version(PyObject *self)
{
	return Py_BuildValue("s", "Version 1.0.0");
};
