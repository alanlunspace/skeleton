#!/usr/bin/env python3
import json
import os
import logging
import logging.config
import coloredlogs
import fileinput

log_config_filepath = open('config/logging_conf.json')
log_config_json = json.load(log_config_filepath)
log_filename = log_config_json['handlers']['file']['filename']
log_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.dirname(log_filename))

if not os.path.exists(log_dir):
    try:
        os.makedirs(log_dir)
    except OSError as e:
        raise e

logging.config.dictConfig(log_config_json)
logger = logging.getLogger(__name__)

logger.debug(f"Hellow World!")
