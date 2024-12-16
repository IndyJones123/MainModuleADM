import logging
import os
import re
import platform
from logging.handlers import TimedRotatingFileHandler


def conf_logging(nama_log: str = 'root'):
    path = os.getcwd()
    # system = platform.system().upper()

    fullpath = f'{path}/logging'

    if not os.path.exists(fullpath):
        os.makedirs(fullpath)

    fullpath2 = f'{path}/dblogging'

    if not os.path.exists(fullpath2):
        os.makedirs(fullpath2)

    logname = f"logging/{nama_log}.log"
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s.%(msecs)03d %(name)-12s %(levelname)-s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S', )

    console = TimedRotatingFileHandler(logname, when="Midnight", interval=1)
    console.suffix = '%Y-%m-%d_%H-%M-%S'
    formatter = logging.Formatter('%(asctime)s.%(msecs)03d %(name)-12s %(levelname)-ls %(message)s', '%Y-%m-%d %H:%M:%S')
    console.setFormatter(formatter)
    # console.extMatch = re.compile(r"^\d{8}$")

    return console


def write_log(logger: logging.Logger, nama_fungsi: str, ket: str):
    try:
        logger.info(f'fc:{nama_fungsi}(): {ket}')
    except PermissionError:
        print(f'fc:{nama_fungsi}(): {ket}')
    except AttributeError:
        print(f'fc:{nama_fungsi}(): {ket}')
    except IOError:
        print(f'fc:{nama_fungsi}(): {ket}')
