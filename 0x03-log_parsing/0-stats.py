#!/usr/bin/python3
"""
Log Parsing Script
"""

import sys

if __name__ == "__main__":

    total_size = 0
    line_count = 0
    status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    log_stats = {code: 0 for code in status_codes}

    def display_stats(stats, size):
        print(f"File size: {size}")
        for code, count in sorted(stats.items()):
            if count > 0:
                print(f"{code}: {count}")

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            try:
                status = parts[-2]
                if status in log_stats:
                    log_stats[status] += 1
            except Exception:
                pass

            try:
                total_size += int(parts[-1])
            except Exception:
                pass

            if line_count % 10 == 0:
                display_stats(log_stats, total_size)

        display_stats(log_stats, total_size)

    except KeyboardInterrupt:
        display_stats(log_stats, total_size)
        raise
