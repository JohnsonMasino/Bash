#!/usr/bin/python3

"""
This file creates functions that
creates and tears down modules
"""

def SetUpModule():
    openConnection()

def TearDownModule():
    CloseConnection()

print("\nCode developed by Masino")
