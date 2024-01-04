#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as excep_message:
        excep_message = str(excep_message)
        message = "Exception: {:s}\n".format(excep_message)
        sys.stderr.write(message)
        return None
    else:
        return result
