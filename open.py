#!/usr/bin/python3

import sys

class Disp:

    def DispPath():
        print("The system directories are:")
        print(dir(sys))
        print("\n\nThe path subdirectory are:")
        print(dir(sys.path))

        print("\nCode developed by Masino")
Disp.DispPath()
