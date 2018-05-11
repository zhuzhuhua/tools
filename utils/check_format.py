# -*- coding: UTF-8 -*-
import datetime



def format_datetime_string(data):
    data = str(data)
    if len(data) != 6:
        return False

    try:
        datetime.datetime.strptime(data, '%Y%m')
    except:
        return False
    return True


def format_datetime(data):
    data = str(data)
    try:
        datetime.datetime.strptime(data, '%Y%m')
    except:
        return False
    return True


