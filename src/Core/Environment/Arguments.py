# -*- enconding: utf-8 -*-

import argparse

class Arguments:
    def __init__(self):
        self.__parser = argparse.ArgumentParser(
            prog='alfred',
            description='Alfred - Just another programming language')

        self.__parser.add_argument(
            '-v', '--version',
            action='version', version='%(prog)s v0.5.1')

        self.__parser.add_argument(
            'FILE',
            type=argparse.FileType('r'))
    
    def parse(self):
        args = self.__parser.parse_args()
        if args.FILE:
            args.source = args.FILE.read()
            args.FILE.close()
        return args
