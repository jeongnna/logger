import sys
import logging


fw_logger = logging.getLogger('stdout_forwarding')
fw_logger.setLevel(logging.INFO)


class LoggerWriter:

    def __init__(self, logger, log_level=logging.INFO):
        self.logger = logger
        self.log_level = log_level
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


_loggerwriter = LoggerWriter(fw_logger)
_stdout = sys.stdout
_stderr = sys.stderr


def start(logfile):
    fw_logger.addHandler(logging.StreamHandler())
    fw_logger.addHandler(logging.FileHandler(logfile))

    sys.stdout = _loggerwriter
    sys.stderr = _loggerwriter


def stop():
    fw_logger.handlers = []

    sys.stdout = _stdout
    sys.stderr = _stderr
