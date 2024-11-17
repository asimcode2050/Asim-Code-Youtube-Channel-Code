def hexdump(data):
    for i in range(0, len(data), 16):
        chunk = data[i:i + 16]
        hex_values = ' '.join(f'{byte:02x}' for byte in chunk)
        ascii_values = ''.join(chr(byte) if 32 <= byte <=
                               126 else '.' for byte in chunk)
        print(f'{i:08x}  {hex_values:<47}  {ascii_values}')


data = b"Hello, this is an example of hexdump!"
hexdump(data)
