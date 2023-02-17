#ifndef RFT_CS_RFTCS_CORE_API_H_
#define RFT_CS_RFTCS_CORE_API_H_
#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>

#if PY_MAJOR_VERSION >= 3

// Core functions
#include "core/simulation.h"
#include "core/fuel.h"
#include "core/trajectory.h"

// Extentions
static PyObject * ext_double_angle_sine(PyObject *);
static PyObject * ext_flight_range(PyObject *, PyObject *);
static PyObject * ext_flight_time(PyObject *, PyObject *);

#endif

#endif // RFT_CS_RFTCS_CORE_API_H_