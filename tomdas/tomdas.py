# Tom's Data Analysis Scripts module.
# Create Date: 2023-01-18
# Author: Tom Ling
# Changelog: 
#
# 2023-01-26: Tom Ling: Updated read_csv() to ignore http files, 
#             updated unimport() docstring. Used *args and **kwargs
#             to make wrapper functions more effective.
# 2023-01-19: Tom Ling: Added string_to_list(), updated read_csv(), 
#             added categorize(), added unimport(). 
# 2023-01-18: Tom Ling: Initial module completed. 
"""
Provides a set of useful data analysis functions.

This module provides some useful data analysis functions to speed up
data analysis in Jupyter Notebook. 

Notes
-----
None yet.

Examples
--------
>>> import tomdas as td
>>> td.world()
'Hello world'
>>> from tomdas import world
>>> world()
'Hello world'

"""
# Packages required by the scripts in this module.
import sys
import pandas as pd
from IPython.display import display
from os import path


# Set tomdas_version. Call this with tomdas.tomdas_version
tomdas_version = "0.0.5"


def example_docstring(parameter1, parameter2=0):
    """
    Exists to illustrate how to write a pandas docstring.

    (The short summary line above says what the function does in a concise way.
    Python lines should not exceed 79 characters, which the previous line has.)
    The short summary should begin with a capital letter and end with a full 
    stop. It should begin with an infinitive verb and fit onto a single line. 
    
    This section below is the extended summary which explains why the function
    is useful and the use cases. Each paragraph here ends with a full stop. 
    
    Parameters
    ----------
    parameter1 : int
        Short definition.
    parameter2 : int, default 0, (if useful) meaning of default value 
        Short definition.

    Returns
    -------
    int
        Describe what the function returns when called.

    See Also
    --------
    subtract : Subtract one integer from another.

    (This section lets the user know about related pandas functionality.)
    
    Notes
    -----
    An optional section that provides notes about the implementation or 
    technical aspects of the function. 
    
    References
    ----------
    For more info on pandas docstrings, see: 
    https://pandas.pydata.org/docs/development/contributing_docstring.html
    
    Examples
    --------
    >>> example_docstring(2, 2)
    4
    >>> example_docstring(25, 0)
    25
    
    Comments describing an example have blank lines on either side.
    Code in examples is assumed to start with ``import numpy as np``
    and ``import pandas as pd``. 
    
    >>> example_docstring(10, -10)
    0
    """
    return parameter1 + parameter2


def tomdas():
    """
    Returns "Tom's Data Analysis Scripts" to confirm module import.
    
    Returns
    -------
    str
        The string "Tom's Data Analysis Scripts".
  
    Examples
    --------
    >>> tomdas()
    "Tom's Data Analysis Scripts"
    """
    return "Tom's Data Analysis Scripts."


def string_to_list(input_string=""): 
    """
    Converts a string to a list with the string as the only element of the list.
    
    Returns a list consisting of the input string as the only element. If the 
    input_string is not of datatype "str", returns the input string unchanged.
    
    Parameters
    ----------
    input_string : str, default ""
        The string input.

    Returns
    -------
    list of str
        A list with a single element consisting of the input string.

    Examples
    --------
    >>> string_to_list("hello")
    ['hello']
    >>> string_to_list(1)
    1
    """
    if isinstance(input_string, str):
        return [input_string]
    else: 
        return input_string

    
def read_csv(filepath_or_buffer = "", 
             index_col = None, 
             usecols = None, 
             parse_dates = None, 
             ascending = True, 
             inplace = False,
             show_info = True, 
              *args, 
              **kwargs):
    """
    Load a CSV file as a pandas DataFrame and call ``.info()``.

    This is a wrapper function for ``pd.read_csv()`` and ``pd.sort_index()``.
    It loads a CSV file with filename as specified in the ``filepath_or_buffer`` 
    parameter and displays both a preview of the file (as if calling 
    ``pd.read_csv()``) and an information summary of the file (as if calling 
    ``df.info()``). If an index_col argument was provided, sorts the 
    dataframe by the index. 
    
    Any parameters in pd.read_csv that raise errors when strings are passed
    in instead of lists, will have the string arguments converted to lists
    before ``pd.read_csv()`` is called. 
    
    All this saves a little time when loading CSV files for data analysis. 
    Parameters not directly specified here should be passed to ``pd.read_csv``
    in *args and **kwargs. For detailed work use ``pd.read_csv()`` directly.
    
    Parameters
    ----------
    filepath_or_buffer : str, path object or file-like object, default ""
        Filename of the CSV file to load. Passed to pd.read_csv(file). 
    usecols : list-like or callable, optional, default None
        Columns to retain. Passed to pd.read_csv(usecols). 
    dtype : Type name or dict of column -> type, optional, default None
        Data type for data or columns. Passed to pd.read_csv(dtype). 
    parse_dates : str or list of str, default None
        Columns to parse dates in. Passed to pd.read_csv(parse_dates). 
        If parse_dates is a string, converts it to a list with 1 element.
    ascending : bool or list-like of bools, default True
        Index sort order. Passed to pd.sort_index(file). 
    inplace : bool or list-like of bools, default True
        Index sort order. Passed to pd.sort_index(file). 
    show_info : bool, default True
        If True: show DataFrame.info().   
    
    Returns
    -------
    pandas DataFrame
        A pandas DataFrame of the CSV file data, sorted by index.
    
    Examples
    --------
    >>> bigmac = read_csv(file="bigmac.csv")
    >>> len(bigmac)
    652
    >>> read_csv()
    No file supplied.
    """
    # Check whether a filename argument was supplied. 
    if filepath_or_buffer == "": 
        # No argument supplied to `filepath_or_buffer` parameter. Notify user.
        print("Error: No file selected.")
    elif (not filepath_or_buffer.startswith("http")) and (not path.exists(filepath_or_buffer)):
        # No valid file. Notify user.
        print("Error: Invalid file name or path.")
    else: 
        # If parse_dates is a string, convert it to a list with 1 element. 
        parse_dates_list = string_to_list(parse_dates)
            
        # If usecols is a string, convert it to a list with 1 element. 
        usecols_list = string_to_list(usecols)
        
        # Call pandas.read_csv and display the file preview.
        df_loaded_csv = pd.read_csv(
            filepath_or_buffer,
            index_col = index_col,                       
            usecols = usecols_list, 
            parse_dates = parse_dates_list,
            *args,
            **kwargs
        )
        
        # Sort the index(es) if present. 
        if index_col != None and len(index_col) > 0: 
            df_loaded_csv = df_loaded_csv.sort_index(
                ascending = ascending, 
                inplace = inplace
            )
        
        # Display preview of the clean DataFrame.
        display(df_loaded_csv)

        # Call .info() method on the DataFrame. 
        if show_info: 
            df_loaded_csv.info()
        
        # Return a deep copy of the DataFrame. 
        return df_loaded_csv.copy()
    

def categorize(data,
               columns = None,
               dtype = "category",
               copy = True,
               errors = 'raise',
               show_info = True,
               *args,
               **kwargs
              ):
    """
    Call the ``.astype()`` method on the pandas data object (Series or DataFrame). 

    This is a wrapper function for the ``.astype()`` method on a pandas Series or
    DataFrame object. It takes the Series or DataFrame provided in the ``data`` 
    parameter and looks for columns specified in the ``columns`` parameter. If
    a column is found in the data object, that column's datatype is changed to 
    the datatype specified in the ``dtype`` parameter. By default the datatype
    is changed to "category". If the ``columns`` parameter is omitted, the other
    parameters are passed to ``.astype()`` which should mean dict-like arguments
    for ``dtype`` are handled as expected. 
    
    Any parameters in ``.astype()`` that raise errors when strings are passed
    in instead of lists, will have the string arguments converted to lists
    before ``.astype()`` is called. 
    
    Parameters
    ----------
    data : pandas Series or DataFrame
        Pandas object on which .astype() method is called.   
    columns : str or list of str, optional, default None
        Columns to modify datatype. Passed to .astype(). 
    dtype : Type name or dict of column -> type, optional, default None
        Data type for data or columns. Passed to .astype(). 
    copy : bool, default True
        Return a copy when copy=True (be very careful setting copy=False 
        as changes to values then may propagate to other pandas objects). 
        Passed to .astype().
    errors : {‘raise’, ‘ignore’}, default ‘raise’
        Control raising of exceptions on invalid data for provided dtype. 
        Passed to .astype(). 
            raise : allow exceptions to be raised
            ignore : suppress exceptions. On error return original object.
    show_info : bool, default True
        If True: show results of calling .info() on the data object.   
    
    Returns
    -------
    pandas Series or DataFrame
        A deep copy of the pandas Series or DataFrame supplied in ``data``, 
        after calling ``.astype()``.
    
    Examples
    --------
    >>> ser = pd.Series([1, 2], dtype='int32')
    >>> ser
    0    1
    1    2
    dtype: int32
    >>> ser = categorize(ser, dtype = 'int64', showinfo = False)
    >>> ser
    0    1
    1    2
    dtype: int64
    """
    if not isinstance(data, pd.Series) and not isinstance(data, pd.DataFrame):
        # The data object is not a pandas Series or DataFrame. 
        print("Error: Data is not a pandas Series or DataFrame.")
    else:
        # Create a deep copy of the data object. 
        data_categorized = data.copy()
    
    if columns == None: 
        # No columns selected - call .astype() with remaining parameters. 
        # This is intended to allow a dictionary in dtype to be processed as normal. 
        data_categorized = data.astype(
            dtype = dtype,
            copy = copy, 
            errors = errors,
            *args,
            **kwargs
        )
    else:
        # If columns is a string, convert it to a list with 1 element. 
        columns_list = string_to_list(columns)
                
        # Call pandas Series or DataFrame method data.astype().
        data_categorized = data.copy()
        for column in columns_list:
            if column in data: 
                data_categorized[column] = data[column].astype(
                    dtype = dtype, 
                    copy = copy,
                    errors = errors
                )
            else: 
                print("Warning: Column '" + column + "' not found in the data.") 

    # Call .info() method on the data object. 
    if show_info: 
        data_categorized.info()
                
    # Return (a deep copy of) the categorized data object. 
    return data_categorized.copy()

    
def unimport(module_name=""):
    """
    Unimports a module if previously imported. 

    Unimports the module specified in ``module_name`` if it was previously
    imported in the current Jupyter Notebook session. 
    
    Parameters
    ----------
    module_name : str
        Name of module to unimport. 
    
    Notes
    -----
    If this function does not work, use: 
    import importlib
    importlib.reload(my_module)
    
    Examples
    --------
    >>> import sys, tomdas as td
    >>> "tomdas" in sys.modules.keys()
    True
    >>> td.tomdas()
    "Tom's Data Analysis Scripts."
    >>> td.unimport("tomdas")
    >>> "tomdas" in sys.modules.keys()
    False
    
    """
    # Check if module_name is a string
    if not isinstance(module_name, str): 
        "Error: module name must be a string."
    else: 
        # Unimport module
        if module_name != "" and module_name in sys.modules.keys(): 
            sys.modules.pop(module_name)
            print(module_name + " has been unimported.")