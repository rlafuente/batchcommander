/*
 * Interface wrapper code.
 *
 * Generated by SIP 4.10.1 on Tue Jun  8 17:01:01 2010
 */

#include "sipAPIQtPoppler.h"

#line 150 "poppler-qt4.sip"
#define UNSTABLE_POPPLER_QT4 1
#include <qt4/poppler-qt4.h>
#line 13 "sipQtPopplerPopplerDocument.cpp"

#line 41 "/usr/share/sip/PyQt4/QtGui/qcolor.sip"
#include <qcolor.h>
#line 17 "sipQtPopplerPopplerDocument.cpp"
#line 216 "/usr/share/sip/PyQt4/QtXml/qdom.sip"
#include <qdom.h>
#line 20 "sipQtPopplerPopplerDocument.cpp"
#line 125 "/usr/share/sip/PyQt4/QtCore/qlist.sip"
#include <qlist.h>
#line 23 "sipQtPopplerPopplerDocument.cpp"
#line 78 "poppler-qt4.sip"
#define UNSTABLE_POPPLER_QT4 1
#include <qt4/poppler-qt4.h>
#line 27 "sipQtPopplerPopplerDocument.cpp"
#line 38 "/usr/share/sip/PyQt4/QtCore/qlist.sip"
#include <qlist.h>
#line 30 "sipQtPopplerPopplerDocument.cpp"
#line 45 "poppler-qt4.sip"
#define UNSTABLE_POPPLER_QT4 1
#include <qt4/poppler-qt4.h>
#line 34 "sipQtPopplerPopplerDocument.cpp"
#line 41 "/usr/share/sip/PyQt4/QtCore/qstringlist.sip"
#include <qstringlist.h>
#line 37 "sipQtPopplerPopplerDocument.cpp"
#line 41 "/usr/share/sip/PyQt4/QtCore/qstring.sip"
#include <qstring.h>
#line 40 "sipQtPopplerPopplerDocument.cpp"
#line 346 "/usr/share/sip/PyQt4/QtCore/qdatetime.sip"
#include <qdatetime.h>
#line 43 "sipQtPopplerPopplerDocument.cpp"
#line 43 "/usr/share/sip/PyQt4/QtCore/qbytearray.sip"
#include <qbytearray.h>
#line 46 "sipQtPopplerPopplerDocument.cpp"
#line 100 "poppler-qt4.sip"
#define UNSTABLE_POPPLER_QT4 1
#include <qt4/poppler-qt4.h>
#line 50 "sipQtPopplerPopplerDocument.cpp"


extern "C" {static PyObject *meth_Poppler_Document_load(PyObject *, PyObject *);}
static PyObject *meth_Poppler_Document_load(PyObject *, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const QString * a0;
        int a0State = 0;
        const QByteArray& a1def = QByteArray();
        const QByteArray * a1 = &a1def;
        int a1State = 0;
        const QByteArray& a2def = QByteArray();
        const QByteArray * a2 = &a2def;
        int a2State = 0;

        if (sipParseArgs(&sipParseErr, sipArgs, "J1|J1J1", sipType_QString,&a0, &a0State, sipType_QByteArray, &a1, &a1State, sipType_QByteArray, &a2, &a2State))
        {
            Poppler::Document *sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = Poppler::Document::load(*a0,*a1,*a2);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<QString *>(a0),sipType_QString,a0State);
            sipReleaseType(const_cast<QByteArray *>(a1),sipType_QByteArray,a1State);
            sipReleaseType(const_cast<QByteArray *>(a2),sipType_QByteArray,a2State);

            return sipConvertFromType(sipRes,sipType_Poppler_Document,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_Document, sipName_load, NULL);

    return NULL;
}


extern "C" {static PyObject *meth_Poppler_Document_page(PyObject *, PyObject *);}
static PyObject *meth_Poppler_Document_page(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        int a0;
        Poppler::Document *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "Bi", &sipSelf, sipType_Poppler_Document, &sipCpp, &a0))
        {
            Poppler::Page *sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->page(a0);
            Py_END_ALLOW_THREADS

            return sipConvertFromType(sipRes,sipType_Poppler_Page,NULL);
        }
    }

    {
        QString * a0;
        int a0State = 0;
        Poppler::Document *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "BJ1", &sipSelf, sipType_Poppler_Document, &sipCpp, sipType_QString,&a0, &a0State))
        {
            Poppler::Page *sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->page(*a0);
            Py_END_ALLOW_THREADS
            sipReleaseType(a0,sipType_QString,a0State);

            return sipConvertFromType(sipRes,sipType_Poppler_Page,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_Document, sipName_page, NULL);

    return NULL;
}


extern "C" {static PyObject *meth_Poppler_Document_numPages(PyObject *, PyObject *);}
static PyObject *meth_Poppler_Document_numPages(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        Poppler::Document *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_Poppler_Document, &sipCpp))
        {
            int sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->numPages();
            Py_END_ALLOW_THREADS

            return SIPLong_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_Document, sipName_numPages, NULL);

    return NULL;
}


extern "C" {static PyObject *meth_Poppler_Document_pageMode(PyObject *, PyObject *);}
static PyObject *meth_Poppler_Document_pageMode(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        Poppler::Document *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_Poppler_Document, &sipCpp))
        {
            Poppler::Document::PageMode sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->pageMode();
            Py_END_ALLOW_THREADS

            return sipConvertFromEnum(sipRes,sipType_Poppler_Document_PageMode);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_Document, sipName_pageMode, NULL);

    return NULL;
}


extern "C" {static PyObject *meth_Poppler_Document_pageLayout(PyObject *, PyObject *);}
static PyObject *meth_Poppler_Document_pageLayout(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        Poppler::Document *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_Poppler_Document, &sipCpp))
        {
            Poppler::Document::PageLayout sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->pageLayout();
            Py_END_ALLOW_THREADS

            return sipConvertFromEnum(sipRes,sipType_Poppler_Document_PageLayout);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_Document, sipName_pageLayout, NULL);

    return NULL;
}


extern "C" {static PyObject *meth_Poppler_Document_unlock(PyObject *, PyObject *);}
static PyObject *meth_Poppler_Document_unlock(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const QByteArray * a0;
        int a0State = 0;
        const QByteArray * a1;
        int a1State = 0;
        Poppler::Document *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "BJ1J1", &sipSelf, sipType_Poppler_Document, &sipCpp, sipType_QByteArray, &a0, &a0State, sipType_QByteArray, &a1, &a1State))
        {
            bool sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->unlock(*a0,*a1);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<QByteArray *>(a0),sipType_QByteArray,a0State);
            sipReleaseType(const_cast<QByteArray *>(a1),sipType_QByteArray,a1State);

            return PyBool_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_Document, sipName_unlock, NULL);

    return NULL;
}


extern "C" {static PyObject *meth_Poppler_Document_isLocked(PyObject *, PyObject *);}
static PyObject *meth_Poppler_Document_isLocked(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        Poppler::Document *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_Poppler_Document, &sipCpp))
        {
            bool sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->isLocked();
            Py_END_ALLOW_THREADS

            return PyBool_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_Document, sipName_isLocked, NULL);

    return NULL;
}


extern "C" {static PyObject *meth_Poppler_Document_date(PyObject *, PyObject *);}
static PyObject *meth_Poppler_Document_date(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const QString * a0;
        int a0State = 0;
        Poppler::Document *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "BJ1", &sipSelf, sipType_Poppler_Document, &sipCpp, sipType_QString,&a0, &a0State))
        {
            QDateTime *sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new QDateTime(sipCpp->date(*a0));
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<QString *>(a0),sipType_QString,a0State);

            return sipConvertFromNewType(sipRes,sipType_QDateTime,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_Document, sipName_date, NULL);

    return NULL;
}


extern "C" {static PyObject *meth_Poppler_Document_info(PyObject *, PyObject *);}
static PyObject *meth_Poppler_Document_info(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const QString * a0;
        int a0State = 0;
        Poppler::Document *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "BJ1", &sipSelf, sipType_Poppler_Document, &sipCpp, sipType_QString,&a0, &a0State))
        {
            QString *sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new QString(sipCpp->info(*a0));
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<QString *>(a0),sipType_QString,a0State);

            return sipConvertFromNewType(sipRes,sipType_QString,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_Document, sipName_info, NULL);

    return NULL;
}


extern "C" {static PyObject *meth_Poppler_Document_infoKeys(PyObject *, PyObject *);}
static PyObject *meth_Poppler_Document_infoKeys(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        Poppler::Document *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_Poppler_Document, &sipCpp))
        {
            QStringList *sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new QStringList(sipCpp->infoKeys());
            Py_END_ALLOW_THREADS

            return sipConvertFromNewType(sipRes,sipType_QStringList,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_Document, sipName_infoKeys, NULL);

    return NULL;
}


extern "C" {static PyObject *meth_Poppler_Document_isEncrypted(PyObject *, PyObject *);}
static PyObject *meth_Poppler_Document_isEncrypted(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        Poppler::Document *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_Poppler_Document, &sipCpp))
        {
            bool sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->isEncrypted();
            Py_END_ALLOW_THREADS

            return PyBool_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_Document, sipName_isEncrypted, NULL);

    return NULL;
}


extern "C" {static PyObject *meth_Poppler_Document_isLinearized(PyObject *, PyObject *);}
static PyObject *meth_Poppler_Document_isLinearized(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        Poppler::Document *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_Poppler_Document, &sipCpp))
        {
            bool sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->isLinearized();
            Py_END_ALLOW_THREADS

            return PyBool_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_Document, sipName_isLinearized, NULL);

    return NULL;
}


extern "C" {static PyObject *meth_Poppler_Document_okToPrint(PyObject *, PyObject *);}
static PyObject *meth_Poppler_Document_okToPrint(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        Poppler::Document *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_Poppler_Document, &sipCpp))
        {
            bool sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->okToPrint();
            Py_END_ALLOW_THREADS

            return PyBool_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_Document, sipName_okToPrint, NULL);

    return NULL;
}


extern "C" {static PyObject *meth_Poppler_Document_okToPrintHighRes(PyObject *, PyObject *);}
static PyObject *meth_Poppler_Document_okToPrintHighRes(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        Poppler::Document *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_Poppler_Document, &sipCpp))
        {
            bool sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->okToPrintHighRes();
            Py_END_ALLOW_THREADS

            return PyBool_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_Document, sipName_okToPrintHighRes, NULL);

    return NULL;
}


extern "C" {static PyObject *meth_Poppler_Document_okToChange(PyObject *, PyObject *);}
static PyObject *meth_Poppler_Document_okToChange(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        Poppler::Document *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_Poppler_Document, &sipCpp))
        {
            bool sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->okToChange();
            Py_END_ALLOW_THREADS

            return PyBool_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_Document, sipName_okToChange, NULL);

    return NULL;
}


extern "C" {static PyObject *meth_Poppler_Document_okToCopy(PyObject *, PyObject *);}
static PyObject *meth_Poppler_Document_okToCopy(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        Poppler::Document *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_Poppler_Document, &sipCpp))
        {
            bool sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->okToCopy();
            Py_END_ALLOW_THREADS

            return PyBool_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_Document, sipName_okToCopy, NULL);

    return NULL;
}


extern "C" {static PyObject *meth_Poppler_Document_okToAddNotes(PyObject *, PyObject *);}
static PyObject *meth_Poppler_Document_okToAddNotes(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        Poppler::Document *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_Poppler_Document, &sipCpp))
        {
            bool sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->okToAddNotes();
            Py_END_ALLOW_THREADS

            return PyBool_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_Document, sipName_okToAddNotes, NULL);

    return NULL;
}


extern "C" {static PyObject *meth_Poppler_Document_okToFillForm(PyObject *, PyObject *);}
static PyObject *meth_Poppler_Document_okToFillForm(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        Poppler::Document *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_Poppler_Document, &sipCpp))
        {
            bool sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->okToFillForm();
            Py_END_ALLOW_THREADS

            return PyBool_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_Document, sipName_okToFillForm, NULL);

    return NULL;
}


extern "C" {static PyObject *meth_Poppler_Document_okToCreateFormFields(PyObject *, PyObject *);}
static PyObject *meth_Poppler_Document_okToCreateFormFields(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        Poppler::Document *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_Poppler_Document, &sipCpp))
        {
            bool sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->okToCreateFormFields();
            Py_END_ALLOW_THREADS

            return PyBool_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_Document, sipName_okToCreateFormFields, NULL);

    return NULL;
}


extern "C" {static PyObject *meth_Poppler_Document_okToExtractForAccessibility(PyObject *, PyObject *);}
static PyObject *meth_Poppler_Document_okToExtractForAccessibility(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        Poppler::Document *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_Poppler_Document, &sipCpp))
        {
            bool sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->okToExtractForAccessibility();
            Py_END_ALLOW_THREADS

            return PyBool_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_Document, sipName_okToExtractForAccessibility, NULL);

    return NULL;
}


extern "C" {static PyObject *meth_Poppler_Document_okToAssemble(PyObject *, PyObject *);}
static PyObject *meth_Poppler_Document_okToAssemble(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        Poppler::Document *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_Poppler_Document, &sipCpp))
        {
            bool sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->okToAssemble();
            Py_END_ALLOW_THREADS

            return PyBool_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_Document, sipName_okToAssemble, NULL);

    return NULL;
}


extern "C" {static PyObject *meth_Poppler_Document_pdfVersion(PyObject *, PyObject *);}
static PyObject *meth_Poppler_Document_pdfVersion(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        Poppler::Document *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_Poppler_Document, &sipCpp))
        {
            double sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->pdfVersion();
            Py_END_ALLOW_THREADS

            return PyFloat_FromDouble(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_Document, sipName_pdfVersion, NULL);

    return NULL;
}


extern "C" {static PyObject *meth_Poppler_Document_fonts(PyObject *, PyObject *);}
static PyObject *meth_Poppler_Document_fonts(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        Poppler::Document *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_Poppler_Document, &sipCpp))
        {
            QList<Poppler::FontInfo> *sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new QList<Poppler::FontInfo>(sipCpp->fonts());
            Py_END_ALLOW_THREADS

            return sipConvertFromNewType(sipRes,sipType_QList_0100Poppler_FontInfo,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_Document, sipName_fonts, NULL);

    return NULL;
}


extern "C" {static PyObject *meth_Poppler_Document_scanForFonts(PyObject *, PyObject *);}
static PyObject *meth_Poppler_Document_scanForFonts(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        int a0;
        QList<Poppler::FontInfo> * a1;
        int a1State = 0;
        Poppler::Document *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "BiJ0", &sipSelf, sipType_Poppler_Document, &sipCpp, &a0, sipType_QList_0100Poppler_FontInfo,&a1, &a1State))
        {
            bool sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->scanForFonts(a0,a1);
            Py_END_ALLOW_THREADS
            sipReleaseType(a1,sipType_QList_0100Poppler_FontInfo,a1State);

            return PyBool_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_Document, sipName_scanForFonts, NULL);

    return NULL;
}


extern "C" {static PyObject *meth_Poppler_Document_embeddedFiles(PyObject *, PyObject *);}
static PyObject *meth_Poppler_Document_embeddedFiles(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        Poppler::Document *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_Poppler_Document, &sipCpp))
        {
            QList<Poppler::EmbeddedFile *> *sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new QList<Poppler::EmbeddedFile *>(sipCpp->embeddedFiles());
            Py_END_ALLOW_THREADS

            return sipConvertFromNewType(sipRes,sipType_QList_0101Poppler_EmbeddedFile,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_Document, sipName_embeddedFiles, NULL);

    return NULL;
}


extern "C" {static PyObject *meth_Poppler_Document_hasEmbeddedFiles(PyObject *, PyObject *);}
static PyObject *meth_Poppler_Document_hasEmbeddedFiles(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        Poppler::Document *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_Poppler_Document, &sipCpp))
        {
            bool sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->hasEmbeddedFiles();
            Py_END_ALLOW_THREADS

            return PyBool_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_Document, sipName_hasEmbeddedFiles, NULL);

    return NULL;
}


extern "C" {static PyObject *meth_Poppler_Document_toc(PyObject *, PyObject *);}
static PyObject *meth_Poppler_Document_toc(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        Poppler::Document *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_Poppler_Document, &sipCpp))
        {
            QDomDocument *sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->toc();
            Py_END_ALLOW_THREADS

            return sipConvertFromType(sipRes,sipType_QDomDocument,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_Document, sipName_toc, NULL);

    return NULL;
}


extern "C" {static PyObject *meth_Poppler_Document_setPaperColor(PyObject *, PyObject *);}
static PyObject *meth_Poppler_Document_setPaperColor(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const QColor * a0;
        int a0State = 0;
        Poppler::Document *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "BJ1", &sipSelf, sipType_Poppler_Document, &sipCpp, sipType_QColor, &a0, &a0State))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp->setPaperColor(*a0);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<QColor *>(a0),sipType_QColor,a0State);

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_Document, sipName_setPaperColor, NULL);

    return NULL;
}


extern "C" {static PyObject *meth_Poppler_Document_paperColor(PyObject *, PyObject *);}
static PyObject *meth_Poppler_Document_paperColor(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        Poppler::Document *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_Poppler_Document, &sipCpp))
        {
            QColor *sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new QColor(sipCpp->paperColor());
            Py_END_ALLOW_THREADS

            return sipConvertFromNewType(sipRes,sipType_QColor,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_Document, sipName_paperColor, NULL);

    return NULL;
}


extern "C" {static PyObject *meth_Poppler_Document_setRenderHint(PyObject *, PyObject *);}
static PyObject *meth_Poppler_Document_setRenderHint(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        Poppler::Document::RenderHint a0;
        bool a1 = 1;
        Poppler::Document *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "BE|b", &sipSelf, sipType_Poppler_Document, &sipCpp, sipType_Poppler_Document_RenderHint, &a0, &a1))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp->setRenderHint(a0,a1);
            Py_END_ALLOW_THREADS

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_Document, sipName_setRenderHint, NULL);

    return NULL;
}


/* Cast a pointer to a type somewhere in its superclass hierarchy. */
extern "C" {static void *cast_Poppler_Document(void *, const sipTypeDef *);}
static void *cast_Poppler_Document(void *ptr, const sipTypeDef *targetType)
{
    if (targetType == sipType_Poppler_Document)
        return ptr;

    return NULL;
}


/* Call the instance's destructor. */
extern "C" {static void release_Poppler_Document(void *, int);}
static void release_Poppler_Document(void *sipCppV,int)
{
    Py_BEGIN_ALLOW_THREADS

    delete reinterpret_cast<Poppler::Document *>(sipCppV);

    Py_END_ALLOW_THREADS
}


extern "C" {static void dealloc_Poppler_Document(sipSimpleWrapper *);}
static void dealloc_Poppler_Document(sipSimpleWrapper *sipSelf)
{
    if (sipIsPyOwned(sipSelf))
    {
        release_Poppler_Document(sipSelf->u.cppPtr,0);
    }
}


static PyMethodDef methods_Poppler_Document[] = {
    {SIP_MLNAME_CAST(sipName_date), meth_Poppler_Document_date, METH_VARARGS, NULL},
    {SIP_MLNAME_CAST(sipName_embeddedFiles), meth_Poppler_Document_embeddedFiles, METH_VARARGS, NULL},
    {SIP_MLNAME_CAST(sipName_fonts), meth_Poppler_Document_fonts, METH_VARARGS, NULL},
    {SIP_MLNAME_CAST(sipName_hasEmbeddedFiles), meth_Poppler_Document_hasEmbeddedFiles, METH_VARARGS, NULL},
    {SIP_MLNAME_CAST(sipName_info), meth_Poppler_Document_info, METH_VARARGS, NULL},
    {SIP_MLNAME_CAST(sipName_infoKeys), meth_Poppler_Document_infoKeys, METH_VARARGS, NULL},
    {SIP_MLNAME_CAST(sipName_isEncrypted), meth_Poppler_Document_isEncrypted, METH_VARARGS, NULL},
    {SIP_MLNAME_CAST(sipName_isLinearized), meth_Poppler_Document_isLinearized, METH_VARARGS, NULL},
    {SIP_MLNAME_CAST(sipName_isLocked), meth_Poppler_Document_isLocked, METH_VARARGS, NULL},
    {SIP_MLNAME_CAST(sipName_load), meth_Poppler_Document_load, METH_VARARGS, NULL},
    {SIP_MLNAME_CAST(sipName_numPages), meth_Poppler_Document_numPages, METH_VARARGS, NULL},
    {SIP_MLNAME_CAST(sipName_okToAddNotes), meth_Poppler_Document_okToAddNotes, METH_VARARGS, NULL},
    {SIP_MLNAME_CAST(sipName_okToAssemble), meth_Poppler_Document_okToAssemble, METH_VARARGS, NULL},
    {SIP_MLNAME_CAST(sipName_okToChange), meth_Poppler_Document_okToChange, METH_VARARGS, NULL},
    {SIP_MLNAME_CAST(sipName_okToCopy), meth_Poppler_Document_okToCopy, METH_VARARGS, NULL},
    {SIP_MLNAME_CAST(sipName_okToCreateFormFields), meth_Poppler_Document_okToCreateFormFields, METH_VARARGS, NULL},
    {SIP_MLNAME_CAST(sipName_okToExtractForAccessibility), meth_Poppler_Document_okToExtractForAccessibility, METH_VARARGS, NULL},
    {SIP_MLNAME_CAST(sipName_okToFillForm), meth_Poppler_Document_okToFillForm, METH_VARARGS, NULL},
    {SIP_MLNAME_CAST(sipName_okToPrint), meth_Poppler_Document_okToPrint, METH_VARARGS, NULL},
    {SIP_MLNAME_CAST(sipName_okToPrintHighRes), meth_Poppler_Document_okToPrintHighRes, METH_VARARGS, NULL},
    {SIP_MLNAME_CAST(sipName_page), meth_Poppler_Document_page, METH_VARARGS, NULL},
    {SIP_MLNAME_CAST(sipName_pageLayout), meth_Poppler_Document_pageLayout, METH_VARARGS, NULL},
    {SIP_MLNAME_CAST(sipName_pageMode), meth_Poppler_Document_pageMode, METH_VARARGS, NULL},
    {SIP_MLNAME_CAST(sipName_paperColor), meth_Poppler_Document_paperColor, METH_VARARGS, NULL},
    {SIP_MLNAME_CAST(sipName_pdfVersion), meth_Poppler_Document_pdfVersion, METH_VARARGS, NULL},
    {SIP_MLNAME_CAST(sipName_scanForFonts), meth_Poppler_Document_scanForFonts, METH_VARARGS, NULL},
    {SIP_MLNAME_CAST(sipName_setPaperColor), meth_Poppler_Document_setPaperColor, METH_VARARGS, NULL},
    {SIP_MLNAME_CAST(sipName_setRenderHint), meth_Poppler_Document_setRenderHint, METH_VARARGS, NULL},
    {SIP_MLNAME_CAST(sipName_toc), meth_Poppler_Document_toc, METH_VARARGS, NULL},
    {SIP_MLNAME_CAST(sipName_unlock), meth_Poppler_Document_unlock, METH_VARARGS, NULL}
};

static sipEnumMemberDef enummembers_Poppler_Document[] = {
    {sipName_Antialiasing, Poppler::Document::Antialiasing, 5},
    {sipName_ArthurBackend, Poppler::Document::ArthurBackend, 4},
    {sipName_FullScreen, Poppler::Document::FullScreen, 3},
    {sipName_NoLayout, Poppler::Document::NoLayout, 2},
    {sipName_OneColumn, Poppler::Document::OneColumn, 2},
    {sipName_SinglePage, Poppler::Document::SinglePage, 2},
    {sipName_SplashBackend, Poppler::Document::SplashBackend, 4},
    {sipName_TextAntialiasing, Poppler::Document::TextAntialiasing, 5},
    {sipName_TwoColumnLeft, Poppler::Document::TwoColumnLeft, 2},
    {sipName_TwoColumnRight, Poppler::Document::TwoColumnRight, 2},
    {sipName_TwoPageLeft, Poppler::Document::TwoPageLeft, 2},
    {sipName_TwoPageRight, Poppler::Document::TwoPageRight, 2},
    {sipName_UseAttach, Poppler::Document::UseAttach, 3},
    {sipName_UseNone, Poppler::Document::UseNone, 3},
    {sipName_UseOC, Poppler::Document::UseOC, 3},
    {sipName_UseOutlines, Poppler::Document::UseOutlines, 3},
    {sipName_UseThumbs, Poppler::Document::UseThumbs, 3},
};


pyqt4ClassTypeDef sipTypeDef_QtPoppler_Poppler_Document = {
{
    {
        -1,
        0,
        0,
        SIP_TYPE_CLASS,
        sipNameNr_Poppler__Document,
        {0}
    },
    {
        sipNameNr_Document,
        {0, 255, 0},
        30, methods_Poppler_Document,
        17, enummembers_Poppler_Document,
        0, 0,
        {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    },
    0,
    sipNameNr_PyQt4_QtCore_pyqtWrapperType,
    -1,
    0,
    0,
    0,
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
    dealloc_Poppler_Document,
    0,
    0,
    0,
    release_Poppler_Document,
    cast_Poppler_Document,
    0,
    0,
    0
},
    0,
    0,
    0
};
