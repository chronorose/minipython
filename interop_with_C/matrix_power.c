#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdlib.h>

typedef struct {
    size_t size;
    double** mtrx;
} Matrix;

void initMatrix(Matrix* matrix, size_t size) {
    matrix->size = size;
    matrix->mtrx = malloc(sizeof(double*) * size);
    for (size_t i = 0; i < size; i++) {
        matrix->mtrx[i] = calloc(size, sizeof(double));
    }
}

Matrix* newMatrix(size_t size) {
    Matrix* matrix = malloc(sizeof(Matrix));
    matrix->size = size;
    matrix->mtrx = malloc(sizeof(double*) * size);
    for (size_t i = 0; i < size; i++) {
        matrix->mtrx[i] = calloc(size, sizeof(double));
    }
    return matrix;
}

Matrix* duplicateMatrix(Matrix* m_to_duplicate) {
    Matrix* new_matrix = newMatrix(m_to_duplicate->size);
    for (size_t i = 0; i < m_to_duplicate->size; i++) {
        for(size_t j = 0; j < m_to_duplicate->size; j++) {
            new_matrix->mtrx[i][j] = m_to_duplicate->mtrx[i][j];
        }
    }
    return new_matrix;
}

Matrix* raise_to_power(Matrix* m_to_raise, size_t power) {
    Matrix* startMatrix = duplicateMatrix(m_to_raise);
    Matrix* tmp_matrix = newMatrix(m_to_raise->size);
    for (size_t i = 0; i < power - 1; i++) {
        for (size_t j = 0; j < m_to_raise->size; j++) {
            for (size_t k = 0; k < m_to_raise->size; k++) {
                double sum = 0;
                for (size_t h = 0; h < m_to_raise->size; h++) {
                    sum += startMatrix->mtrx[j][h] * m_to_raise->mtrx[h][k];
                }
                tmp_matrix->mtrx[j][k] = sum;
            }
        }
        for (size_t j = 0; j < m_to_raise->size; j++) {
            for (size_t k = 0; k < m_to_raise->size; k++) {
                m_to_raise->mtrx[j][k] = tmp_matrix->mtrx[j][k];
            }
        }
    }
    return m_to_raise;
}

int python_to_c(PyObject* p_mtrx, void* address) {
    Matrix* matrix = address;
    size_t size = PyList_Size(p_mtrx);
    initMatrix(matrix, size);
    for (size_t i = 0; i < size; i++) {
        PyObject* list = PyList_GetItem(p_mtrx, i);
        for (size_t j = 0; j < size; j++) {
            PyObject* dbl = PyList_GetItem(list, j);
            matrix->mtrx[i][j] = PyFloat_AsDouble(dbl);
        }
    }
    return 1;
}

PyObject* c_to_python(Matrix* matrix) {
    size_t size = matrix->size;
    PyObject* p_mtrx = PyList_New(size);
    for (size_t i = 0; i < size; i++) {
        PyObject* array = PyList_New(size);
        for (size_t j = 0; j < size; j++) {
            PyObject* dbl = PyFloat_FromDouble(matrix->mtrx[i][j]);
            PyList_SetItem(array, j, dbl);
        }
        PyList_SetItem(p_mtrx, i, array);
    }
    return p_mtrx;
}

void freeMatrix(Matrix* matrix) {
    for (size_t i = 0; i < matrix->size; i++) {
        free(matrix->mtrx[i]);
    }
    free(matrix->mtrx);
}

static PyObject* foreign_matrix(PyObject* self, PyObject* args) { 
    Matrix matrix;
    unsigned int power = 0;
    if(!PyArg_ParseTuple(args, "O&I", python_to_c, &matrix, &power)) {
        return NULL;
    }
    Matrix* matrix_xd = raise_to_power(&matrix, power);
    PyObject* p_mtrx = c_to_python(&matrix);
    freeMatrix(&matrix);
    return p_mtrx;
}

static PyMethodDef ForeignMethods[] = {
    {
        "foreign_matrix", foreign_matrix, METH_VARARGS, "raises matrix to a power"
    },
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef matrix_module = {
    PyModuleDef_HEAD_INIT,
    "matrix",
    NULL,
    -1,
    ForeignMethods
};

PyMODINIT_FUNC PyInit_matrix(void) {
    return PyModule_Create(&matrix_module);
}
