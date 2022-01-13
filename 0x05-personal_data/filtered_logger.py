#!/usr/bin/env python3
"""regex"""
import re
from typing import List
import logging
import os
import mysql.connector


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.f = fields

    def format(self, record: logging.LogRecord) -> str:
        """format the record"""
        form = logging.Formatter(self.FORMAT).format(record)
        return filter_datum(self.f, self.REDACTION, form, self.SEPARATOR)


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:
    """delim func"""
    for i in fields:
        search = i + "=" + ".*?" + separator
        replace = i + "=" + redaction + separator
        message = re.sub(search, replace, message)
    return message


def get_logger() -> logging.Logger:
    """get logger function"""
    obj = logging.getLogger('user_data')
    obj.propagate = False
    obj.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setFormatter(RedactingFormatter(PII_FIELDS))
    obj.addHandler(ch)
    return obj


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ function to connect to database
    from the env variables and retuen a mysql connector
    object
    """
    db_user = os.getenv(
        'PERSONAL_DATA_DB_USERNAME', "root")  # PERSONAL_DATA_DB_USERNAME
    # PERSONAL_DATA_DB_PASSWORD
    db_pwd = os.getenv('PERSONAL_DATA_DB_PASSWORD', "")
    db_host = os.getenv(
        'PERSONAL_DATA_DB_HOST',
        "localhost")  # PERSONAL_DATA_DB_HOST
    db_name = os.getenv(
        'PERSONAL_DATA_DB_NAME',
        "my_db")  # PERSONAL_DATA_DB_NAME

    cnx = mysql.connector.connect(user=db_user, password=db_pwd,
                                  host=db_host,
                                  database=db_name)
    return cnx


def main():
    """main function"""
    connect = get_db()
    query = connect.cursor()
    query.execute("SELECT * FROM users")
    rslt = query.fetchall()

    Logger = get_logger()

    for i in rslt:
        f = "name={}; email={}; phone={}; ".format(i[0], i[1], i[2])
        f += "ssn={}; password={}; ip={}; ".format(i[3], i[4], i[5])
        f += "last_login={}; user_agent={};".format(i[6], i[7])
        Logger.info(f)

    query.close()


if __name__ == "__main__":
    main()
