import base64
def main():
    data = 'data to be encoded and decoded'
    encoded = data.encode("utf-8")
    b32encoded = base64.b32encode(encoded)
    print(b32encoded)
    print(base64.b32decode(b32encoded).decode("utf-8"))

if __name__=="__main__":
    main()