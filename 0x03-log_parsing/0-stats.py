#!/usr/bin/python3
import sys
import signal

total_size = 0
status_codes_count = {200: 0, 301: 0, 400: 0,
                      401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
valid_codes = set(status_codes_count.keys())
line_count = 0


def print_statistics():
    """Print the accumulated statistics"""
    print(f"File size: {total_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")


def signal_handler(sig, frame):
    """Handle the SIGINT signal to print statistics and exit"""
    print_statistics()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    try:
        parts = line.split()
        if len(parts) != 9:
            continue
        ip, dash, date, get_request, http_version, status_code, file_size = (
            parts[0], parts[1], parts[2], parts[3],
            parts[4], parts[6], parts[8]
        )

        if get_request != "\"GET" or http_version != "HTTP/1.1\"":
            continue

        status_code = int(status_code)
        file_size = int(file_size)

        if status_code in valid_codes:
            status_codes_count[status_code] += 1
            total_size += file_size

        line_count += 1

        if line_count % 10 == 0:
            print_statistics()

    except Exception:
        continue

print_statistics()
