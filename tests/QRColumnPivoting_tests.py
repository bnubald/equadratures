#!/usr/bin/env python
import effective_quadratures.QR as qr
import matplotlib.pyplot as plt
import numpy as np
import os
"""

    Testing custom QR factorizations with scipy's inbuilt QRP

    Pranay Seshadri
    ps583@cam.ac.uk

    Copyright (c) 2016 by Pranay Seshadri
"""
def main():

    # Test 1: QR Modified Gram Schmidt
    A = np.random.rand(10,8)
    print A
    Q, R, P = qr.qrColumnPivoting_mgs(A)
    print np.dot(Q.T, Q) # Orthogonality check!
    print R # Check to see if its upper triangular
    print P

    # Test 2: QR Householder
    Q, R, P = qr.qrColumnPivoting_house(A)
    print np.dot(Q.T, Q)
    print R
    print P

main()