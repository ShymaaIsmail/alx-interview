#!/usr/bin/python3
"""Log Parsing to calculate statistics"""

import sys
import re
import signal


class LogParser:
    def __init__(self):
        self.statistics = {}
        self.file_size = 0
        self.line_count = 0
        ip = (
            r'(?P<ip>\b((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}'
            r'(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\b)'
        )
        dt_ptr = r'\[(?P<date>.*?)\]'
        s_ptr = r'(?P<status>200|301|400|401|403|404|405|500)'
        sz_ptr = r'(?P<size>\d+)'
        # Combine the patterns into the final log pattern
        self.log_pattern = re.compile(
            rf'{ip} - {dt_ptr} "GET /projects/260 HTTP/1.1" {s_ptr} {sz_ptr}'
        )
        signal.signal(signal.SIGINT, self.signal_handler)

    def print_statistics(self):
        """Function to print the current statistics."""
        print(f"File size: {self.file_size}")
        sorted_stats = dict(sorted(self.statistics.items()))
        for status, count in sorted_stats.items():
            print(f"{status}: {count}")

    def signal_handler(self, signum, frame):
        """Handle keyboard interruption (CTRL + C) to print statistics."""
        self.print_statistics()
        sys.exit(0)

    def process_line(self, line):
        """Process each line of the log."""
        match = re.match(self.log_pattern, line)
        if match:
            log_info = match.groupdict()
            status = log_info['status']
            self.statistics[status] = self.statistics.get(status, 0) + 1
            self.file_size += int(log_info['size'])
        self.line_count += 1

        # Print statistics every 10 lines
        if self.line_count % 10 == 0:
            self.print_statistics()

    def print_remaining_statistics(self):
        """Print remaining statistics after finishing the input."""
        if self.line_count % 10 != 0:
            self.print_statistics()

    def run(self):
        """Run the log parser."""
        for line in sys.stdin:
            self.process_line(line)
        self.print_remaining_statistics()


if __name__ == '__main__':
    parser = LogParser()
    parser.run()
