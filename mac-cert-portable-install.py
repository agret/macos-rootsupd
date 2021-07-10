#!/usr/bin/env python3

# This script pulls the list of Mozilla trusted certificate authorities
# from the web at the "mozurl" below, parses the file to grab the PEM
# for each cert, and then generates DER files in a new ./certs directory
# The DER files are imported into the MacOS trusted root keystore and
# the generated DER files are then deleted,
#
# Original script by Earle F. Philhower, III.  Released to the public domain.
#
# Taken by Agret from:
# https://github.com/esp8266/Arduino/blob/master/libraries/ESP8266WiFi/examples/BearSSL_CertStore/certs-from-mozilla.py
# and modified to update the MacOS cert store

import os
import sys
import glob

for der in glob.iglob('certs/*.der'):
    arCmd = ['sudo','security','add-trusted-cert','-k','/Library/Keychains/System.keychain','-d', der];
    call( arCmd )
