# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 19:18:51 2021

@author: Envydeus Project
"""

# This entrypoint file to be used in development. Start by reading README.md
import arithmetic_arranger
from pytest import main

from arithmetic_arranger import arithmetic_arranger


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))


# Run unit tests automatically
main()