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
from .armfiles import check_arm_standards

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

    #Read data using pandas read_csv
    arm_ds = pd.read_csv(filename)#.to_xarray()
    
    #Set Coordinates
    if arm_ds.date_time.any():
        arm_ds = arm_ds.set_index('date_time')

    #Convert to xarray DataSet
    arm_ds = arm_ds.to_xarray()

    #Set additional variables
    #Since we cannot assume a standard naming convention setting
    #file_date and file_time to the first time in the file
    x_coord = arm_ds.coords.to_index().values[0]
    if isinstance(x_coord,str):
        x_coord_dt = pd.to_datetime(x_coord)
        arm_ds.act.file_date = x_coord_dt.strftime('%Y%m%d')
        arm_ds.act.file_time = x_coord_dt.strftime('%H%M%S')

    #Check for standard ARM datastream name, if none, assume the file is ARM
    #standard format.
    is_arm_file_flag = check_arm_standards(arm_ds)
    if is_arm_file_flag.NO_DATASTREAM is True:
        arm_ds.act.datastream = '.'.join(filename.split('/')[-1].split('.')[0:2])
    else:
        arm_ds.act.datastream = arm_ds.attrs["datastream"]

    #Add additional attributes, site, standards flag, etc...
    arm_ds.act.site = str(arm_ds.act.datastream)[0:3]

    arm_ds.act.arm_standards_flag = is_arm_file_flag

    return arm_ds
