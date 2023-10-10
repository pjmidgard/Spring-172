import os
#Author Jurijus Pacalovas
def compress_file(input_file, output_file, num_bytes_to_remove):
    with open(input_file, 'rb') as f_in:
        data = bytearray(f_in.read())

    # Remove the specified number of bytes
    for _ in range(num_bytes_to_remove):
        data.pop()

    with open(output_file, 'wb') as f_out:
        f_out.write(data)

def decompress_file(input_file, output_file, num_bytes_to_add):
    with open(input_file, 'rb') as f_in:
        data = bytearray(f_in.read())

    # Add the specified number of bytes
    for _ in range(num_bytes_to_add):
        data.append(0)

    with open(output_file, 'wb') as f_out:
        f_out.write(data)

def main():
    print("Options:")
    print("1. Compress")
    print("2. Extract")
    
    option = input("Enter your choice (1 or 2): ")
    
    if option == "1":
        input_file = input("Enter the name of the input file: ")
        num_bytes_to_remove = int(input("Enter the number of bytes to remove in each compression: "))
        num_iterations = int(input("Enter the number of times to compress and save: "))
        base_name = input("Enter the base name for the saved binary files: ")

        # Perform compressions and save binary files
        for i in range(num_iterations):
            compressed_file = f"{base_name}_compressed_{i}.bin"
            compress_file(input_file, compressed_file, num_bytes_to_remove)
            input_file = compressed_file  # Use the compressed file for the next iteration

        print(f"Compressed and saved {num_iterations} times as binary files.")

    elif option == "2":
        input_file = input("Enter the name of the compressed file: ")
        num_bytes_to_add = int(input("Enter the number of bytes to add during decompression: "))
        num_iterations = int(input("Enter the number of times to extract and save: "))
        base_name = input("Enter the base name for the saved binary files: ")

        # Perform extractions and save binary files
        for i in range(num_iterations):
            extracted_file = f"{base_name}_extracted_{i}.bin"
            decompress_file(input_file, extracted_file, num_bytes_to_add)
            input_file = extracted_file  # Use the extracted file for the next iteration

        print(f"Extracted and saved {num_iterations} times as binary files.")

    else:
        print("Invalid choice. Please enter 1 for compress or 2 for extract.")

if __name__ == "__main__":
    main()
