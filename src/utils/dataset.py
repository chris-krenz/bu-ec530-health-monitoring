"""

"""

from datetime import datetime
from typing import Union

import numpy as np
import pandas as pd
import json


class Dataset:
    """

    """

    def __init__(self, dataset_type: str, dataset_id: str, fields: list[str], records_key_id: str,
                 records: Union[list[dict[Union[str, int, bool]]], pd.DataFrame]):
        self.type = dataset_type
        self.id = dataset_id
        self.fields = fields  # i.e. columns
        self.record_key_id = records_key_id  # record = row


