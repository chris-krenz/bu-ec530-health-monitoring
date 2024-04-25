"""

"""

from time import sleep
import logging as log
import uuid
from concurrent.futures import ProcessPoolExecutor  # https://www.geeksforgeeks.org/processpoolexecutor-class-in-python/
from requests import post, get, delete

from config import SQL_URL
from src.utils import logger
from src.utils import id, usr

from src.app import app

user_ids = ['1', '2', '3']


def gen_user_report(user_id):
    user_data = get(SQL_URL + 'users/' + user_id).json()
    return user_data


def main():

    logger.config_logger()

    with ProcessPoolExecutor(max_workers=3) as exe:
        reports = exe.map(gen_user_report, user_ids)

    for report in reports:
        log.info(report)

    # test_name = id.LastFirstMiddleName('Doe', 'John', '')
    # test_ssn  = id.SSN('111-11-1111')
    # test_address = id.Address('123 Street', 'Apt 1', 'Boston', 'MA', '02215', 'United States')
    # test_email   = id.Email('jdoe@bu.edu')
    # test_identity = id.Identity(uuid.uuid4(), test_name, test_ssn, test_address, test_email)
    # # log.info(test_identity)
    #
    # test_user = usr.User(test_identity)
    # test_user.gen_self_report()


if __name__ == '__main__':

    main()
