import sys
import logging


fw_logger = logging.getLogger('stdout_forwarding')
fw_logger.setLevel(logging.INFO)


class LoggerWriter:

    def __init__(self, logger, level=logging.INFO):
        self.logger = logger
        self.level = level
        self._msg_buf = ''

    def write(self, msg):
        full_msg = self._msg_buf + msg
        self._msg_buf = ''

        for line in full_msg.splitlines(keepends=True):
            if line[-1] == '\n':
                self._log(line.rstrip())
            else:
                self._msg_buf += line

    def flush(self):
        if self._msg_buf != '':
            self._log(self._msg_buf.rstrip())

        self._msg_buf = ''

    def _log(self, msg):
        self.logger.log(self.level, msg)


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
