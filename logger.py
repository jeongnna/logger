import sys
import logging


class Logger:

    def __init__(self, filename, init_file=False, log_level=logging.INFO):
        if init_file:
            open(filename, 'w').close()

        self.logger = logging.getLogger()
        self.log_level = log_level

        self.logger.addHandler(logging.FileHandler(filename))
        self.logger.addHandler(logging.StreamHandler())

        self._linebuf = ''

    def write(self, buf):
        temp_linebuf = self._linebuf + buf
        self._linebuf = ''

        for line in temp_linebuf.splitlines(keepends=True):
            if line[-1] == '\n':
                self.logger.log(self.log_level, line.rstrip())
            else:
                self._linebuf += line

    def flush(self):
        if self._linebuf != '':
            self.logger.log(self.log_level, self._linebuf.rstrip())
        self._linebuf = ''


def config(filename, init_file=False, log_level=logging.INFO):
    logger = Logger(filename, init_file, log_level)
    sys.stdout = logger
    sys.stderr = logger


# Usage:
# ------
# import logger
# logger.config('out.log')
# print(123) # It will be printed on both stdout and file 'out.log'.
