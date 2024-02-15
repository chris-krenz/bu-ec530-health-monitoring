"""
Contains classes and subclasses relating to Devices.
"""

from typing import Union, IO
from abc import ABC

import pandas as pd

import src.utils.dataset as dat


class Device(ABC):
    """
    Contains generic attributes and methods for all devices. Must be instantiated as a specific subclass.
    Methods in User classes relate to the initiation of interactions. Methods here relate to the internal workings of
    the device.
    """

    def __init__(self, uuid: str, type: str, owner: dat.Dataset, users: dat.Dataset, admins: dat.Dataset,
                 settings: dict[Union[str, int, bool]], dataset: dat.Dataset,
                 logs: Union[list[str], tuple[str], str, IO]):
        self.id = uuid
        self.type = type
        self.owner = owner
        self.users = users
        self.admins = admins
        # TODO: Validate data
        self.settings = pd.DataFrame(settings)
        self.dataset = pd.DataFrame(dataset)
        self.logs = logs

    # User Methods
    def authenticate_user(self):
        pass

    def add_user(self):
        pass

    def remove_user(self):
        pass

    def change_setting(self):
        pass

    def restart_device(self):
        pass

    # IO/Data Methods
    def receive_interaction(self):
        pass

    def update_display(self):
        pass

    def play_sound(self):
        pass

    def take_reading(self):
        pass

    def write_to_dataset(self):
        pass

    def read_from_dataset(self):
        pass


class Thermometer(Device):

    def __post_init__(self):
        pass

    def read_temp(self):
        pass

    def display_temp(self):
        pass

    def record_temp(self):
        pass

    def calibrate(self):
        pass

    def change_units(self):
        pass


class Pulse(Device):

    def __post_init__(self):
        pass

    def read_pulse(self):
        pass

    def display_pulse(self):
        pass

    def record_pulse(self):
        pass

    def calibrate(self):
        pass


class BP(Device):

    def __post_init__(self):
        pass

    def start_bp_procedure(self):
        pass

    def display_last_bp(self):
        pass

    def record_bp(self):
        pass

    def calibrate(self):
        pass


class Glucometer(Device):

    def __post_init__(self):
        pass

    def read_glucose(self):
        pass

    def display_glucose(self):
        pass

    def record_glucose(self):
        pass

    def calibrate(self):
        pass
