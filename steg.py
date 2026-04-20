from PIL import Image
import hashlib

def to_bits(s):
    return ''.join(f'{b:08b}' for b in s.encode())

def from_bits(b):
    return bytes(int(b[i:i+8], 2) for i in range(0, len(b), 8)).decode()

def encode(inp, out, msg, pwd):
    img = Image.open(inp).convert('RGB')
    px = img.load()

    key = hashlib.sha256(pwd.encode()).hexdigest()[:16]
    data = to_bits(key + msg)
    data = f'{len(data):032b}' + data   # length header

    if len(data) > img.size[0] * img.size[1]:
        raise ValueError('Message too large')

    i = 0
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            if i == len(data): 
                break
            r,g,b = px[x,y]
            px[x,y] = (r & ~1 | int(data[i]), g, b)
            i += 1

    img.save(out)

def decode(inp, pwd):
    img = Image.open(inp).convert('RGB')
    px = img.load()

    bits = ''.join(str(px[x,y][0] & 1)
                   for y in range(img.size[1])
                   for x in range(img.size[0]))

    n = int(bits[:32], 2)
    msg = from_bits(bits[32:32+n])

    key = hashlib.sha256(pwd.encode()).hexdigest()[:16]
    if msg.startswith(key):
        print("Hidden message:", msg[len(key):])
    else:
        print("Wrong password or no message")

print("1. Hide, 2. Reveal")
choice = input("Choice: ")

ip = input("Image Path: ")
password = input("Password: ")

if int(choice) == 1:
    data = input("Message: ")
    out = input("Output: ")
    encode(ip, out, data, password)
elif int(choice) == 2:
    decode(ip, password)
