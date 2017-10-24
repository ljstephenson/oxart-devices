#!/usr/bin/env python3.5

import argparse
import sys

from oxart.devices.holzworth_synth.driver import HolzworthSynth
from artiq.protocols.pc_rpc import simple_server_loop
from artiq.tools import verbosity_args, simple_network_args, init_logger


def get_argparser():
    parser = argparse.ArgumentParser(description="ARTIQ controller for the Holzworth synth on the Quadrupole laser system")
    simple_network_args(parser, 4000)
    verbosity_args(parser)
    return parser


def main():
    args = get_argparser().parse_args()
    init_logger(args)

    dev = HolzworthSynth() # Starts frequency update loop to track cavity drift

    try:
        simple_server_loop({"HolzworthSynth": dev}, args.bind, args.port)
    finally:
        dev.close()


if __name__ == "__main__":
    main()
