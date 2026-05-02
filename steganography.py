import cv2

# Convert text → binary
def to_binary(text):
    return ''.join(format(ord(i), '08b') for i in text)

# Encoding function
def encode(img, message):
    message += "#####"
    binary_msg = to_binary(message)

    data_index = 0
    total_data = len(binary_msg)

    for row in img:
        for pixel in row:
            for i in range(3):  # R, G, B
                if data_index < total_data:
                    pixel[i] = int(format(pixel[i], '08b')[:-1] + binary_msg[data_index], 2)
                    data_index += 1
    return img

# Decoding function
def decode(img):
    binary_data = ""

    for row in img:
        for pixel in row:
            for i in range(3):
                binary_data += format(pixel[i], '08b')[-1]

    # Split into 8 bits
    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]

    message = ""
    for byte in all_bytes:
        message += chr(int(byte, 2))
        if message.endswith("#####"):
            break

    return message.replace("#####", "")