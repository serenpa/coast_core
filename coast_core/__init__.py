"""
    Title:

    Author:

    Description:
"""
from __future__ import print_function
from ._version import get_versions

from coast_core import citations
from coast_core import clarity_of_writing
from coast_core import code_detection
from coast_core import events
from coast_core import extraction
from coast_core import markers
from coast_core import named_entities
from coast_core import ngram_extraction
from coast_core import utils

__author__ = 'Ashley Williams'
__email__ = 'ashley.williams@pg.canterbury.ac.nz'
__version__ = get_versions()['version']
del get_versions
