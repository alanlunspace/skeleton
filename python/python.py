#!/usr/bin/env python3
from lib.log import log
import os

basename = os.path.basename(__file__)
dirname = os.path.dirname(basename)

log.debug(__file__)
