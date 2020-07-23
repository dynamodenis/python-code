#!/usr/bin/env python3.6

import pyqrcode # pip install pyqrcode
import png #pip install pypng

from pyqrcode import QRCode
QRstr= "https://dynamodenis.herokuapp.com/" # You can change to your prefered url

url=pyqrcode.create(QRstr)
url.png('Desktop\\qr.png',scale=8)

