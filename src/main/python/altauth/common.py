__author__ = 'Mirko Rossini'

import sys

if sys.version < '3':
    def b(x):
        return bytes(x)
else:
    def b(x):
        return bytes(x, "utf8") if isinstance(x, str) else x
