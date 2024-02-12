"""

"""

from datetime import datetime
from typing import Union

import json
import numpy as np
import pandas as pd

from device import Device
from provider import Provider


class Patient:
    """

    """

    def __init__(self, patient_id: str, patient_name: str, current_providers: list[Provider],
                 currently_owned_devices: list[Device], currently_used_devices: list[Device]):
        self.id = patient_id
        self.name = patient_name
        self.providers = current_providers
        self.owned_devices = currently_owned_devices
        self.used_devices = currently_used_devices


# dataset of patients
