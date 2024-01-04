#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except Exception as excep_message:
        excep_message = str(excep_message)
        message = "Exception: {:s}\n".format(excep_message)
        sys.stderr.write(message)
        return False
    else:
        return True
