#!/usr/bin/env python2
# coding: utf-8
# file: ParseCommandArgs.py
# time: 2016/8/6 11:59

import sys

from Cores.ProxySpider import ProxySpider
from utils.ArgParser import ArgParse
from utils.ArgParser.Messages import Version
from utils.data.LoggerHelp import logger

__author__ = "lightless"
__email__ = "root@lightless.me"

__all__ = ["ParseCommandArgs"]


class ParseCommandArgs(object):
    def __init__(self):
        super(ParseCommandArgs, self).__init__()
        self.command_args = ArgParse.pansidong_parse.parse_args()

    def start_parse(self):
        # --version
        if self.command_args.version:
            print Version
            sys.exit(0)

        # --update-proxy-db
        if self.command_args.update_proxy_db:
            logger.debug("Update Proxy DB selected.")
            ps = ProxySpider.ProxySpider()
            ps.load()
            ps.start()
            sys.exit(0)

            # --check
