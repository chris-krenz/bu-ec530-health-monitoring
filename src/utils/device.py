"""

"""

from datetime import datetime
from typing import Union

import numpy as np
import pandas as pd
import json

from dataset import Dataset
from patient import Patient
from provider import Provider
from admin import Admin


class Device:
    """

    """

    def __init__(self, device_type: str, device_id: str, owner: Union[Patient, Provider, Admin],
                 users: list[Union[Patient, Provider, Admin]], dataset: Dataset,  # Disaggregate users?
                 settings: list[dict[Union[str, int, bool]]]):
        self.id = device_id
        self.type = device_type
        self.owner = owner
        self.users = users
        self.dataset = dataset
        self.settings = settings
        # self.log

    # User and Owner Methods
    def add_user_to_device(self, user: Union[Patient, Provider, Admin]):
        """

        :param user:
        """

    def remove_user_from_device(self, user: Union[Patient, Provider, Admin]):
        """

        :param user:
        """

    def change_owner_of_device(self, owner: Union[Patient, Provider, Admin]):
        """

        :param owner:
        """

    # Data Methods
    def add_records_to_device(self, records: list[dict[str, Union[str, int, bool]]], source: str):
        """

        :return:
        """

    def replace_a_record_on_device(self, old_record, new_record: list[dict[str, Union[str, int, bool]]], source: str):
        """

        :return:
        """

    def read_data_from_device(self, data_types: list[str], record_filters: dict[str, Union[str, int, bool]],
                              destination: str):
        """

        :return:
        """

    def delete_data_on_device(self, data_types: list[str], data_filters: dict[str, Union[str, int, bool]], source: str):
        """

        :return:
        """

# dataset of devices
