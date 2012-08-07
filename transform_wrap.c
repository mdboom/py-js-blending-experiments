#include <Python.h>

#include "transform.c"

static PyObject *
py_transform(PyObject *self, PyObject *args)
{
  double val = transform();
  return Py_BuildValue("d", val);
}

static PyMethodDef methods[] = {
    {"transform", py_transform, METH_NOARGS,
     "Benchmark doing an affine transform"},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

PyMODINIT_FUNC
initctransform(void)
{
    PyObject* m;

    m = Py_InitModule("ctransform", methods);
}
