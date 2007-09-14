# -*- Makefile -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Michael A.G. Aivazis
#                        California Institute of Technology
#                        (C) 1998-2005 All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PROJECT = histogram
PACKAGE = applications/gui

PROJ_TIDY += *.log *.pyc
PROJ_CLEAN =

# directory structure

BUILD_DIRS = \
    wxmpl \

OTHER_DIRS = \
 
RECURSE_DIRS = $(BUILD_DIRS) $(OTHER_DIRS)

#--------------------------------------------------------------------------
#
all: export
	BLD_ACTION="all" $(MM) recurse
 
distclean::
	BLD_ACTION="distclean" $(MM) recurse

clean::
	BLD_ACTION="clean" $(MM) recurse

tidy::
	BLD_ACTION="tidy" $(MM) recurse
#--------------------------------------------------------------------------
#

EXPORT_PYTHON_MODULES = \
	__init__.py \
	testhistogram.py \
	ControlPanel.py \
	HistInfoPanel.py \
	HistPlotPanel.py \
	HistNotebook.py \
	LowerPanel.py \
	MainWinApp.py \
	MainFrame.py \
	MainPanel.py \
	UpperPanel.py \



EXPORT_BINS = \
	histogramGui.py \



export:: export-binaries release-binaries export-package-python-modules 



# version
# $Id: Make.mm 925 2006-05-22 06:45:13Z jiao $

# End of file