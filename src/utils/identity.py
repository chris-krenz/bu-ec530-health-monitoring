"""
Primarily contains Identity class used for all users of all devices.
"""

from datetime import datetime
from dataclasses import dataclass, field
import uuid


@dataclass
class LastFirstMiddleName:
    """
    Full name, including: last and, optionally, first and middle
    """
    last:   str
    first:  str = field(default='')
    middle: str = field(default='')

    last_verified: datetime.today = field(default=datetime.today())

    def update(self, last: str, first: str = '', middle: str = ''):
        # TODO: Validate Name formatting
        self.last = last
        self.first = first
        self.middle = middle

        self.verify()

    def verify(self):
        self.last_verified = datetime.today()
        print("User Name verified")

    def __repr__(self):
        return f"{str(self.first)} {str(self.last)}"


@dataclass
class SSN:
    """
    Social Security Number
    """
    __ssn: str

    @property
    def __ssn(self) -> str:
        return self.__ssn

    @__ssn.setter
    def __ssn(self, ssn: str) -> None:
        """
        ssn: The new SSN to replace the old one; should be 11 character string that includes the '-' separators
        """

        # TODO: Add caller authentication step

        area, group, serial = ssn.split('-')
        if (len(area), len(group), len(serial) == 3, 2, 4) and area.isdigit() and group.isdigit() and serial.isdigit():
            # TODO: Implement cross-reference of existing SSNs to ensure no duplicate (and external check?)...
            self.__ssn = ssn
        else:
            print("SSN Change Rejected: SSN is malformed.")

    @__ssn.deleter
    def __ssn(self) -> None:

        # TODO: Add caller authentication step

        del self.__ssn

    @__ssn.getter
    def __ssn(self) -> str:

        # TODO: Add caller authentication step

        return self.__ssn


@dataclass
class Address:
    """
    Standardized address parameters: street, unit, city, state, zip, country, other
    """
    street:  str = field(default='')
    unit:    str = field(default='')
    city:    str = field(default='')
    state:   str = field(default='')
    zip:     str = field(default='')
    country: str = field(default='')
    other:   str = field(default='')

    last_verified: datetime.today = field(default=datetime.today())

    def update(self, street: str = '', unit: str = '', city: str = '', state: str = '', zip: str = '',
               country: str = '', other: str = ''):
        # TODO: Validate address formatting
        self.street = street
        self.unit = unit
        self.city = city
        self.state = state
        self.zip = zip
        self.country = country
        self.other = other

        self.verify()

    def verify(self):
        self.last_verified = datetime.today()
        print("User Address verified")


@dataclass
class Email:
    """
    Formatted email address and known status of the
    """
    email: str
    last_verified: datetime.today = field(default=datetime.today())

    def update(self, email: str = ''):
        # TODO: Validate email formatting
        self.email = email

        self.verify()

    def verify(self):
        self.last_verified = datetime.today()
        print("User Email verified")


@dataclass
class Identity:
    """
    Represents a unique user. Corresponds to a single row in the Users database. Each Identity can be used to
    instantiate multiple different class identities.
    """
    id: uuid
    name: LastFirstMiddleName
    ssn: SSN
    address: Address
    email: Email
