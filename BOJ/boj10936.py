
import base64

def base64ToString(s):
    base64_message = s.encode('ascii')
    base64_bytes = base64.b64decode(base64_message)
    message_bytes = base64_bytes.decode('ascii')

    return message_bytes

if __name__ == "__main__":
    s = input()
    print(base64ToString(s))