import sys
import logging


logger = logging.getLogger('stdout_forwarding')
logger.setLevel(logging.INFO)


class LogWriter:

    def __init__(self):
        self._linebuf = ''

    def write(self, buf):
        temp_linebuf = self._linebuf + buf
        self._linebuf = ''

        for line in temp_linebuf.splitlines(keepends=True):
            if line[-1] == '\n':
                logger.info(line.rstrip())
            else:
                self._linebuf += line

    def flush(self):
        if self._linebuf != '':
            logger.info(self._linebuf.rstrip())
        self._linebuf = ''


_logwriter = LogWriter()
_stdout = sys.stdout
_stderr = sys.stderr


def start(logfile):
    logger.addHandler(logging.StreamHandler())
    logger.addHandler(logging.FileHandler(logfile))

    sys.stdout = _logwriter
    sys.stderr = _logwriter


def stop():
    logger.handlers = []

    sys.stdout = _stdout
    sys.stderr = _stderr
