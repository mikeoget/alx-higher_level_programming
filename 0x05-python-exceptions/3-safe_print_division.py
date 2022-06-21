#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        m = a / b
    except ZeroDivisionError:
        m = None
    finally:
        print("Inside result: {}".format(m))
    return m
