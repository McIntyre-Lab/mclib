""" A class for generating flags.

Tables of binary flags are commonly used for looking at frequencies and filter
rows. Here is a class to quickly generate these types of tables.

"""
# Imports
import numpy as np
import pandas as pd


class FlagsDataFrame(pd.DataFrame):

    def __init__(self, *args, **kw):
        super(FlagsDataFrame, self).__init__(*args, **kw)

    def addColumn(self, column, mask=[]):
        self[column] = 0

        if len(mask) > 0:
            self.updateMask(mask=mask, column=column)

    def updateMask(self, mask, column=''):
        """ Update the dataframe with 1's if the mask value is true.

        :Arguments:
            :param mask: List of mask values. Must follow same structure as instantiated flag dataframe
            :type mask: list

            :param column: Column name to update in the flag frame. Not required
            :type column: String

        :Returns:
            Updated instance of the flag dataframe. The dataframe can be accessed through '.df_flags'.

        """
        # Update the values to 1's if they are true in the mask
        if len(column) > 0:
            self.loc[mask.index, column] = mask.astype(int)
        else:
            self.loc[mask.index, self.columns] = mask.astype(int)

    @property
    def _constructor(self):
        return FlagsDataFrame

    @property
    def _constructor_sliced(self):
        return FlagsSeries


class FlagsSeries(pd.Series):

    @property
    def _constructor(self):
        return FlagsSeries

    @property
    def _constructor_expanddim(self):
        return FlagsDataFrame


