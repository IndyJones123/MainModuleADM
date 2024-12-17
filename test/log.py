from MainModuleADM.Logging.logging_config import i_conf_logging, i_write_log

import logging

logger = logging.getLogger()
if not logger.handlers:
    logger.addHandler(i_conf_logging(nama_log='testing'))

logname = 'Initial Project Testing'

i_write_log(logger, logname, 'Testing Log')