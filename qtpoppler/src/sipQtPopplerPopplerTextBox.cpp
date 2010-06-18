/*
 * Interface wrapper code.
 *
 * Generated by SIP 4.10.1 on Tue Jun  8 17:01:01 2010
 */

#include "sipAPIQtPoppler.h"

#line 27 "poppler-qt4.sip"
#define UNSTABLE_POPPLER_QT4 1
#include <qt4/poppler-qt4.h>
#line 13 "sipQtPopplerPopplerTextBox.cpp"

#line 41 "/usr/share/sip/PyQt4/QtCore/qstring.sip"
#include <qstring.h>
#line 17 "sipQtPopplerPopplerTextBox.cpp"
#line 160 "/usr/share/sip/PyQt4/QtCore/qrect.sip"
#include <qrect.h>
#line 20 "sipQtPopplerPopplerTextBox.cpp"


extern "C" {static PyObject *meth_Poppler_TextBox_text(PyObject *, PyObject *);}
static PyObject *meth_Poppler_TextBox_text(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        Poppler::TextBox *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_Poppler_TextBox, &sipCpp))
        {
            QString *sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new QString(sipCpp->text());
            Py_END_ALLOW_THREADS

            return sipConvertFromNewType(sipRes,sipType_QString,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_TextBox, sipName_text, NULL);

    return NULL;
}


extern "C" {static PyObject *meth_Poppler_TextBox_boundingBox(PyObject *, PyObject *);}
static PyObject *meth_Poppler_TextBox_boundingBox(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        Poppler::TextBox *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_Poppler_TextBox, &sipCpp))
        {
            QRectF *sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new QRectF(sipCpp->boundingBox());
            Py_END_ALLOW_THREADS

            return sipConvertFromNewType(sipRes,sipType_QRectF,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_TextBox, sipName_boundingBox, NULL);

    return NULL;
}


extern "C" {static PyObject *meth_Poppler_TextBox_nextWord(PyObject *, PyObject *);}
static PyObject *meth_Poppler_TextBox_nextWord(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        Poppler::TextBox *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_Poppler_TextBox, &sipCpp))
        {
            Poppler::TextBox *sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->nextWord();
            Py_END_ALLOW_THREADS

            return sipConvertFromType(sipRes,sipType_Poppler_TextBox,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_TextBox, sipName_nextWord, NULL);

    return NULL;
}


extern "C" {static PyObject *meth_Poppler_TextBox_hasSpaceAfter(PyObject *, PyObject *);}
static PyObject *meth_Poppler_TextBox_hasSpaceAfter(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        Poppler::TextBox *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_Poppler_TextBox, &sipCpp))
        {
            bool sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->hasSpaceAfter();
            Py_END_ALLOW_THREADS

            return PyBool_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_TextBox, sipName_hasSpaceAfter, NULL);

    return NULL;
}


/* Cast a pointer to a type somewhere in its superclass hierarchy. */
extern "C" {static void *cast_Poppler_TextBox(void *, const sipTypeDef *);}
static void *cast_Poppler_TextBox(void *ptr, const sipTypeDef *targetType)
{
    if (targetType == sipType_Poppler_TextBox)
        return ptr;

    return NULL;
}


/* Call the instance's destructor. */
extern "C" {static void release_Poppler_TextBox(void *, int);}
static void release_Poppler_TextBox(void *sipCppV,int)
{
    Py_BEGIN_ALLOW_THREADS

    delete reinterpret_cast<Poppler::TextBox *>(sipCppV);

    Py_END_ALLOW_THREADS
}


extern "C" {static void dealloc_Poppler_TextBox(sipSimpleWrapper *);}
static void dealloc_Poppler_TextBox(sipSimpleWrapper *sipSelf)
{
    if (sipIsPyOwned(sipSelf))
    {
        release_Poppler_TextBox(sipSelf->u.cppPtr,0);
    }
}


extern "C" {static void *init_Poppler_TextBox(sipSimpleWrapper *, PyObject *, PyObject *, PyObject **, PyObject **, PyObject **);}
static void *init_Poppler_TextBox(sipSimpleWrapper *, PyObject *sipArgs, PyObject *sipKwds, PyObject **sipUnused, PyObject **, PyObject **sipParseErr)
{
    Poppler::TextBox *sipCpp = 0;

    {
        const QString * a0;
        int a0State = 0;
        const QRectF * a1;

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, NULL, sipUnused, "J1J9", sipType_QString,&a0, &a0State, sipType_QRectF, &a1))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new Poppler::TextBox(*a0,*a1);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<QString *>(a0),sipType_QString,a0State);

            return sipCpp;
        }
    }

    return NULL;
}


static PyMethodDef methods_Poppler_TextBox[] = {
    {SIP_MLNAME_CAST(sipName_boundingBox), meth_Poppler_TextBox_boundingBox, METH_VARARGS, NULL},
    {SIP_MLNAME_CAST(sipName_hasSpaceAfter), meth_Poppler_TextBox_hasSpaceAfter, METH_VARARGS, NULL},
    {SIP_MLNAME_CAST(sipName_nextWord), meth_Poppler_TextBox_nextWord, METH_VARARGS, NULL},
    {SIP_MLNAME_CAST(sipName_text), meth_Poppler_TextBox_text, METH_VARARGS, NULL}
};


pyqt4ClassTypeDef sipTypeDef_QtPoppler_Poppler_TextBox = {
{
    {
        -1,
        0,
        0,
        SIP_TYPE_CLASS,
        sipNameNr_Poppler__TextBox,
        {0}
    },
    {
        sipNameNr_TextBox,
        {0, 255, 0},
        4, methods_Poppler_TextBox,
        0, 0,
        0, 0,
        {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    },
    0,
    sipNameNr_PyQt4_QtCore_pyqtWrapperType,
    -1,
    0,
    0,
    init_Poppler_TextBox,
    0,
    0,
#if PY_MAJOR_VERSION >= 3
    0,
    0,
#else
    0,
    0,
    0,
    0,
#endif
    dealloc_Poppler_TextBox,
    0,
    0,
    0,
    release_Poppler_TextBox,
    cast_Poppler_TextBox,
    0,
    0,
    0
},
    0,
    0,
    0
};
