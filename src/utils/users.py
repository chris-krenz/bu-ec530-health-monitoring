"""
Primarily contains the User class with general methods for interacting with devices.
"""

from typing import Union
import numpy as np
import logging as log

import src.utils.identity as id
import src.utils.dataset as dat
import src.utils.devices as dev


def foobar(mat_a: Union[list, tuple, np.array], mat_b: Union[list, tuple, np.array]) -> Union[int, float, np.ndarray]:
    """
    Uses numpy matrix multiplication function (shorthand: @) to multiply two array-like inputs.

    :raises TypeError: If either input is not an array-like, including list, tuple, or np.ndarray.
    """

    if type(mat_a) not in [list, tuple, np.ndarray] or \
       type(mat_b) not in [list, tuple, np.ndarray]:
        raise TypeError  # numpy cannot convert input to an array
    result = np.array(mat_a) @ np.array(mat_b)
    log.info(f'Result: {result}')

    return result


class User:

    def __init__(self, identity: id.Identity, relationships: dat.Dataset, title_or_role: str):
        self.identity = identity
        self.relationships = relationships
        self.role = title_or_role  # e.g., Doctor, Nurse, Patient, etc.

    def authenticate_on_device(self):
        pass

    def interact_with_device(self):
        pass

    def change_setting(self):
        pass

    def restart_device(self):
        pass


class Admin(User):
    """

    """

    def add_user_to_device(self):
        pass

    def remove_user_from_device(self):
        pass

    def change_user_access_to_a_device(self, device: dev.Device):
        pass

    def change_owner_of_a_device(self, device: dev.Device):
        pass

    def hard_reset_a_device(self, device: dev.Device):
        pass

    def diagnose_a_device(self, device: dev.Device):
        pass

    def test_a_device(self, device: dev.Device):
        pass


class Developer(User):
    """
    Developers are able to simulate devices and access some restricted device data in order to facilitate development.
    Types of developers may include developers for Software, Hardware, or Data (e.g. Data Scientist).
    """

    def instantiate_simulated_device(self, device: dev.Device):
        pass

    def destroy_simulated_device(self, device: dev.Device):
        pass
