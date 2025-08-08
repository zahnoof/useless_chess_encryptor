# In your data_handler.py file

def text_to_binary(input_data, is_file=True):
    """
    Reads a text file or a string and returns its contents as a single binary string.
    """
    binary_stream = ""
    text = ""
    try:
        if is_file:
            with open(input_data, 'r') as file:
                text = file.read()
        else:
            text = input_data
            
        for char in text:
            ascii_val = ord(char)
            binary_val = bin(ascii_val)[2:].zfill(8)
            binary_stream += binary_val
    except FileNotFoundError:
        print(f"Error: The file '{input_data}' was not found.")
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