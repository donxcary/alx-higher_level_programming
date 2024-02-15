#!/usr/bin/python3
"""
reads stdin line by line and computes metrics
"""

import sys
import signal

def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

def print_stats():
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))

total_size = 0
status_codes = {str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}
line_count = 0

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        data = line.split()
        status_code = data[-2]
        file_size = int(data[-1])
        total_size += file_size
        if status_code in status_codes:
            status_codes[status_code] += 1
        line_count += 1
        if line_count % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    pass
finally:
    print_stats()
