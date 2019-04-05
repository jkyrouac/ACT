"""
===============
act.io.csvfiles
===============

This module contains I/O operations for loading csv files

"""

# import standard modules
import glob
import pandas as pd

from .dataset import ACTAccessor

def read_csv(filename):

    """
    Returns an `xarray.Dataset` with stored data and metadata from user-defined
    query of CSV files

    Parameters
    ----------
    filenames : str or list
        Name of file(s) to read

    Returns
    -------
    act_obj : Object
        ACT dataset

    Examples
    --------
    This example will load the example sounding data used for unit testing.

    .. code-block:: python

        import act

        the_ds, the_flag = act.io.csvfiles.read(
            act.tests.sample_files.EXAMPLE_CSV_WILDCARD)
    """

    data = pd.read_csv(filename).to_xarray()


