#!/usr/bin/python3

import json, sys
from src import analyse

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("[Error] Expecting the path to the configuration file!")
    else:
        try:
            with open(sys.argv[1], 'r') as f:
                data = json.load(f)
        except:
            print("Could not read {} file...".format(sys.argv[1]))
            exit(1)
        analyse.analyse(data)
