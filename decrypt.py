import base64

encoded_str = "EnCt2497f06c6f5357508ec0ccf64727d5773a325d274497f06c6f5357508ec0ccf64u2hslwvPnAP..."
decoded_bytes = base64.b64decode(encoded_str)
decoded_str = decoded_bytes.decode('utf-8', errors='ignore')  # errors='ignore' to handle any non-UTF-8 characters
print(decoded_str)
