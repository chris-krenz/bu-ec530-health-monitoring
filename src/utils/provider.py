"""

"""

from datetime import datetime
from typing import Union

import json
import numpy as np
import pandas as pd

from device import Device
from patient import Patient
from admin import Admin


class Provider:
    """

    """

    def __init__(self, provider_id: str, provider_name: str, current_patients: list[Patient],
                 designated_admins: list[Admin], currently_owned_devices: list[Device],
                 currently_used_devices: list[Device]):
        self.id = provider_id
        self.name = provider_name
        self.patients = current_patients
        self.admins = designated_admins
        self.owned_devices = currently_owned_devices
        self.used_devices = currently_used_devices


# dataset of providers
