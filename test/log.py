from MainModuleADM.Logging.logging_config import write_log, conf_logging

import logging

logger = logging.getLogger()
if not logger.handlers:
    logger.addHandler(conf_logging(nama_log='testing'))

logname = 'Initial Project Testing'

write_log(logger, logname, 'Testing Log')