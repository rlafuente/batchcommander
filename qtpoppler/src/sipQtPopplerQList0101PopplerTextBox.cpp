/*
 * Interface wrapper code.
 *
 * Generated by SIP 4.10.1 on Tue Jun  8 17:01:01 2010
 */

#include "sipAPIQtPoppler.h"

#line 125 "/usr/share/sip/PyQt4/QtCore/qlist.sip"
#include <qlist.h>
#line 12 "sipQtPopplerQList0101PopplerTextBox.cpp"

#line 27 "poppler-qt4.sip"
#define UNSTABLE_POPPLER_QT4 1
#include <qt4/poppler-qt4.h>
#line 17 "sipQtPopplerQList0101PopplerTextBox.cpp"


extern "C" {static void assign_QList_0101Poppler_TextBox(void *, SIP_SSIZE_T, const void *);}
static void assign_QList_0101Poppler_TextBox(void *sipDst, SIP_SSIZE_T sipDstIdx, const void *sipSrc)
{
    reinterpret_cast<QList<Poppler::TextBox *> *>(sipDst)[sipDstIdx] = *reinterpret_cast<const QList<Poppler::TextBox *> *>(sipSrc);
}


extern "C" {static void *array_QList_0101Poppler_TextBox(SIP_SSIZE_T);}
static void *array_QList_0101Poppler_TextBox(SIP_SSIZE_T sipNrElem)
{
    return new QList<Poppler::TextBox *>[sipNrElem];
}


extern "C" {static void *copy_QList_0101Poppler_TextBox(const void *, SIP_SSIZE_T);}
static void *copy_QList_0101Poppler_TextBox(const void *sipSrc, SIP_SSIZE_T sipSrcIdx)
{
    return new QList<Poppler::TextBox *>(reinterpret_cast<const QList<Poppler::TextBox *> *>(sipSrc)[sipSrcIdx]);
}


/* Call the mapped type's destructor. */
extern "C" {static void release_QList_0101Poppler_TextBox(void *, int);}
static void release_QList_0101Poppler_TextBox(void *ptr, int)
{
    Py_BEGIN_ALLOW_THREADS
    delete reinterpret_cast<QList<Poppler::TextBox *> *>(ptr);
    Py_END_ALLOW_THREADS
}



extern "C" {static int convertTo_QList_0101Poppler_TextBox(PyObject *, void **, int *, PyObject *);}
static int convertTo_QList_0101Poppler_TextBox(PyObject *sipPy,void **sipCppPtrV,int *sipIsErr,PyObject *sipTransferObj)
{
    QList<Poppler::TextBox *> **sipCppPtr = reinterpret_cast<QList<Poppler::TextBox *> **>(sipCppPtrV);

#line 154 "/usr/share/sip/PyQt4/QtCore/qlist.sip"
    SIP_SSIZE_T len;

    // Check the type if that is all that is required.
    if (sipIsErr == NULL)
    {
        if (!PySequence_Check(sipPy) || (len = PySequence_Size(sipPy)) < 0)
            return 0;

        for (SIP_SSIZE_T i = 0; i < len; ++i)
        {
            PyObject *itm = PySequence_ITEM(sipPy, i);
            bool ok = (itm && sipCanConvertToType(itm, sipType_Poppler_TextBox, 0));

            Py_XDECREF(itm);

            if (!ok)
                return 0;
        }

        return 1;
    }

    QList<Poppler::TextBox *> *ql = new QList<Poppler::TextBox *>;
    len = PySequence_Size(sipPy);
 
    for (SIP_SSIZE_T i = 0; i < len; ++i)
    {
        PyObject *itm = PySequence_ITEM(sipPy, i);
        Poppler::TextBox *t = reinterpret_cast<Poppler::TextBox *>(sipConvertToType(itm, sipType_Poppler_TextBox, sipTransferObj, 0, 0, sipIsErr));

        Py_DECREF(itm);
 
        if (*sipIsErr)
        {
            delete ql;
            return 0;
        }

        ql->append(t);
    }
 
    *sipCppPtr = ql;
 
    return sipGetState(sipTransferObj);
#line 102 "sipQtPopplerQList0101PopplerTextBox.cpp"
}


extern "C" {static PyObject *convertFrom_QList_0101Poppler_TextBox(void *, PyObject *);}
static PyObject *convertFrom_QList_0101Poppler_TextBox(void *sipCppV,PyObject *sipTransferObj)
{
   QList<Poppler::TextBox *> *sipCpp = reinterpret_cast<QList<Poppler::TextBox *> *>(sipCppV);

#line 129 "/usr/share/sip/PyQt4/QtCore/qlist.sip"
    // Create the list.
    PyObject *l;

    if ((l = PyList_New(sipCpp->size())) == NULL)
        return NULL;

    // Set the list elements.
    for (int i = 0; i < sipCpp->size(); ++i)
    {
        Poppler::TextBox *t = sipCpp->at(i);
        PyObject *tobj;

        if ((tobj = sipConvertFromType(t, sipType_Poppler_TextBox, sipTransferObj)) == NULL)
        {
            Py_DECREF(l);
            return NULL;
        }

        PyList_SET_ITEM(l, i, tobj);
    }

    return l;
#line 134 "sipQtPopplerQList0101PopplerTextBox.cpp"
}


sipMappedTypeDef sipTypeDef_QtPoppler_QList_0101Poppler_TextBox = {
    {
        -1,
        0,
        0,
        SIP_TYPE_MAPPED,
        sipNameNr_317,
        {0}
    },
    {
        -1,
        {0, 0, 1},
        0, 0,
        0, 0,
        0, 0,
        {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
    },
    assign_QList_0101Poppler_TextBox,
    array_QList_0101Poppler_TextBox,
    copy_QList_0101Poppler_TextBox,
    release_QList_0101Poppler_TextBox,
    convertTo_QList_0101Poppler_TextBox,
    convertFrom_QList_0101Poppler_TextBox
};
