"""
Contains classes relating to any type of organization.
"""

from dataclasses import dataclass
import uuid

import src.utils.dataset as dat


@dataclass
class Organization:
    """
    May include companies, hospitals, health system, divisions, units, households, etc.
    """
    id: uuid
    type: str
    divisions: dat.Dataset
    members: dat.Dataset
    owned_devices: dat.Dataset
