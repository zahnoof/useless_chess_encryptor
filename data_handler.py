# In your data_handler.py file

def text_to_binary(filename):
    """
    Reads a text file and returns its contents as a single binary string.
    """
    binary_stream = ""
    try:
        with open(filename, 'r') as file:
            text = file.read()
            for char in text:
                ascii_val = ord(char)
                binary_val = bin(ascii_val)[2:].zfill(8)
                binary_stream += binary_val
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    return binary_stream

def binary_to_text(binary_stream):
    """
    Converts a binary string back into text.
    """
    text_result = ""
    try:
        # Split the binary stream into 8-bit chunks
        binary_chunks = [binary_stream[i:i+8] for i in range(0, len(binary_stream), 8)]
        for chunk in binary_chunks:
            # Convert the 8-bit binary chunk back to an integer
            ascii_val = int(chunk, 2)
            # Convert the integer to a character and append it to the result
            text_result += chr(ascii_val)
    except (ValueError, IndexError):
        print("Error: The binary stream is corrupted or has an invalid format.")
        return None
    return text_result