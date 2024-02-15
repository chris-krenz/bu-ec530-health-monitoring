"""
Primarily contains Dataset class used across the system.
"""

from datetime import datetime
import json
import uuid

import pandas as pd


class Dataset:
    """
    A dataset stored on a device or the cloud. May include data specific to a single entity or aggregated data.
    e.g. An Organization may have a dataset for all Patients, or a Device may have a dataset of all device readings.
    """

    def __init__(self, dataset_id: uuid, dataset_type: str, data: dict[str, any]):
        # TODO: Accept  other data types?
        self.dataset_id = dataset_id
        self.dataset_type = dataset_type
        # TODO: Validate data
        self.dataset = pd.DataFrame(data)

    def rows_add(self):
        pass

    def rows_del(self):
        pass

    def rows_change(self):
        pass

    def rows_read(self):
        pass

    def col_add(self):
        pass

    def col_del(self):
        pass

    def col_rename(self):
        pass

    def cols_read(self):
        pass
