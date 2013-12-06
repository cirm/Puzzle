__author__ = 'madis'

import re

a = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
n ="map"

shift = 2

def caesar (string, shift):
    b = ""
    for ch in string:
        if ch.isalpha():
            stayInAlphabet = ord(ch) + shift

            if stayInAlphabet > ord('z'):
                stayInAlphabet -= 26

            finalletter = chr(stayInAlphabet)


            b += finalletter
        else: b += ch

    print (b)


caesar(n, shift)

