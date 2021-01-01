import base64
def main():
    data =  'data to be encoded'
    encoded = data.encode("utf-8")
    b16encoded = base64.b16encode(encoded)
    print(b16encoded)
    print(base64.b16decode(b16encoded).decode("utf-8"))
if __name__ == "__main__":
    main()