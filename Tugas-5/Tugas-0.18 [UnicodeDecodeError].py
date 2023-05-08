bytes = b'H\x8fllo'
string = bytes.decode('utf-8') # UnicodeDecodeError: 'utf-8' codec can't decode byte 0x8f in position 1: invalid start byte
