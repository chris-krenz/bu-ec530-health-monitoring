"""

"""

from datetime import datetime
from typing import Union

import numpy as np
import pandas as pd

from device import Device
from provider import Provider


class Admin:
    """

    """

    def __init__(self, admin_id: str, admin_name: str, designated_providers: list[Provider],
                 currently_owned_devices: list[Device], currently_used_devices: list[Device]):
        self.id = admin_id
        self.name = admin_name
        self.providers = designated_providers
        self.owned_devices = currently_owned_devices
        self.used_devices = currently_used_devices

# dataset of admins
