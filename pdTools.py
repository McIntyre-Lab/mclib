""" Set of helper functions for the pandas library.

These functions are generic code for manipulating different parts of the pandas
library, for example data frames.

"""


def orderDf(df, varList):
    """ Re-order the columns of a dataframe.

    Arguments:
        :type df: pandas.DataFrame
        :param df: A pandas dataframe

        :param list varList: List of column names you want to be placed at the
            front of your data frame.

    """

    # Create a list of the other columns in df, not including the columns that
    # are being moved.
    otherCols = [x for x in df.columns if x not in varList]

    # Create new data frame with the columns name in varList at the front.
    dfOrder = df[varList + otherCols].copy()

    return dfOrder
