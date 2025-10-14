"""
Write a function to remove leading zeroes from an ip address.
assert removezero_ip("216.08.094.196")==('216.8.94.196')
"""


import re

def removezero_ip(ip_address):
    # Split the IP address into its components
    ip_parts = ip_address.split('.')
    # Remove leading zeroes from each part of the IP address
    stripped_ip_parts = [str(int(part)) for part in ip_parts]
    # Reassemble the IP address
    new_ip_address = '.'.join(stripped_ip_parts)
    return new_ip_address

# Example usage
# assert removezero_ip("216.08.094.196") == ('216.8.94.196')
