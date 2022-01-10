import base64

def stringToBase64(s):
    message_bytes = s.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')

    return base64_message

if __name__ == "__main__":
    s = input()
    print(stringToBase64(s))
