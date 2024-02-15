"""
Primarily contains the User class with general methods for interacting with devices.
"""

import src.utils.identity as id
import src.utils.dataset as dat
import src.utils.devices as device


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

    def change_user_access_to_a_device(self, device: device.Device):
        pass

    def change_owner_of_a_device(self, device: device.Device):
        pass

    def hard_reset_a_device(self, device: device.Device):
        pass

    def diagnose_a_device(self, device: device.Device):
        pass

    def test_a_device(self, device: device.Device):
        pass


class Developer(User):
    """
    Developers are able to simulate devices and access some restricted device data in order to facilitate development.
    Types of developers may include developers for Software, Hardware, or Data (e.g. Data Scientist).
    """

    def instantiate_simulated_device(self, device: device.Device):
        pass

    def destroy_simulated_device(self, device: device.Device):
        pass
