"""
===========================
act.plotting (act.plotting)
===========================

.. currentmodule:: act.plotting

This module contains procedures for plotting ARM datasets.

.. autosummary::
    :toctree: generated/

    common.parse_ax
    common.parse_ax_fig
    common.get_date_format
"""

from .plot import TimeSeriesDisplay
from .plot import Display, WindRoseDisplay, SkewTDisplay
from .plot import XSectionDisplay
from . import common
