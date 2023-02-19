#include "api.h"


// Api of flight trajectory
static PyObject * ext_double_angle_sine(PyObject *self)
{
	return PyFloatObject(api_double_angle_sine());
};

static PyObject * ext_flight_range(PyObject *self, PyObject *args)
{
	PyFloatObject * sine = 0;
	PyLongObject * speed = 0;
	if (!PyArg_ParseTuple(args, "fi", &sine, &speed)) return NULL;

	return Py_BuildValue("f", api_flight_range(sine, speed));
};

static PyObject * ext_flight_time(PyObject *self, PyObject *args)
{
	PyLongObject * speed = 0;
	if (!PyArg_ParseTuple(args, "i", &speed)) return NULL;

	return PyFloatObject(api_flight_time(speed));
};

static PyObject * version(PyObject *self)
{
	return Py_BuildValue("s", "Version 1.0.0");
};
