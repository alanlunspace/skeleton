#!/usr/bin/env python3
import json
import os
import logging
import logging.config

log_config_filepath = open('config/log.json')
log_config_json = json.load(log_config_filepath)
log_filename = log_config_json['handlers']['file']['filename']
log_filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), log_filename)
log_dir = os.path.dirname(log_filename)

if not os.path.exists(log_dir):
    try:
        os.makedirs(log_dir)
    except OSError as e:
        raise e

open(log_filename, 'w')

logging.config.dictConfig(log_config_json)
log = logging.getLogger(__name__)

# log.debug(__file__)
