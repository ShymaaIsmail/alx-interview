#!/usr/bin/python3
"""UTF8 Validator"""


def validUTF8(data):
    """validUTF8"""
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the most significant bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        # Get the most significant 8 bits
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine how many bytes the UTF-8 character has
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask = mask >> 1

            if num_bytes == 0:
                # 1 byte character
                continue

            if num_bytes == 1 or num_bytes > 4:
                # Invalid scenarios
                return False
        else:
            # Check if it is a valid continuation byte
            if not (byte & mask1 and not (byte & mask2)):
                return False
        num_bytes -= 1
    return num_bytes == 0
