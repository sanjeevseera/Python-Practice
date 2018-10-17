"""
Write a Python program to remove leading zeros from an IP address
"""

import re
ip = "00216.008.094.196"
ip = re.sub('\.[0]+', '.', ip)
ip = re.sub('^[0]+', '', ip)
print(ip)
