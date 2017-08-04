# -*- coding: utf-8 -*-
#
# Copyright (c) 2017, the cclib development team
#
# This file is part of cclib (http://cclib.github.io) and is distributed under
# the terms of the BSD 3-Clause License.

"""A library for parsing and interpreting results from computational chemistry packages.

The goals of cclib are centered around the reuse of data obtained from various
computational chemistry programs and typically contained in output files. Specifically,
cclib extracts (parses) data from the output files generated by multiple programs
and provides a consistent interface to access them.

Currently supported programs:
    ADF, Firefly, GAMESS(US), GAMESS-UK, Gaussian,
    Jaguar, Molpro, MOPAC, NWChem, ORCA, Psi, Q-Chem

Another aim is to facilitate the implementation of algorithms that are not specific
to any particular computational chemistry package and to maximise interoperability
with other open source computational chemistry and cheminformatic software libraries.
To this end, cclib provides a number of bridges to help transfer data to other libraries
as well as example methods that take parsed data as input.
"""

__version__ = "1.5.1"

from . import parser
from . import progress
from . import method
from . import bridge
from . import io

# The test module can be imported if it was installed with cclib.
try:
    from . import test
except ImportError:
    pass

# The objects below constitute our public API. These names will not change
# over time. Names in the sub-modules will typically also be backwards
# compatible, but may sometimes change when code is moved around.
ccopen = io.ccopen
ccwrite = io.ccwrite
