#ifndef RFT_CS_RFTCS_CORE_TRAJECTORY_H_
#define PY_SSIZE_T_CLEAN
#define RFT_CS_RFTCS_CORE_TRAJECTORY_H_

#include <Python/Python.h>
#include "main_extend.h"

#if PY_MAJOR_VERSION >= 3

float double_angle_sine();
float flight_range(float, int);
float flight_time(int);

static PyObject *CEratosthenes_SieveOfEratosthenes(
	PyObject *self, PyObject *args);


#endif // PY_MAJOR_VERSION >= 3


#endif // RFT_CS_RFTCS_CORE_TRAJECTORY_H_
