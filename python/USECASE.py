# Program to create a hash (message digest) of a file

import hashlib

# Step 1: Get the filename from user
filename = input("Enter the filename: ")

# Step 2: Create a hash object (you can use md5(), sha1(), sha256(), etc.)
hash_func = hashlib.sha256()

# Step 3: Open the file in binary mode
with open(filename, "rb") as f:
    # Step 4: Read the file in chunks
    while chunk := f.read(4096):
        hash_func.update(chunk)

# Step 5: Generate the hexadecimal digest
file_hash = hash_func.hexdigest()

# Step 6: Display the hash
print("\nThe SHA-256 hash (message digest) of the file is:")
print(file_hash)

# Step 7: Optionally, write it to a separate file
with open("hash_output.txt", "w") as hash_file:
    hash_file.write(f"Filename: {filename}\nSHA-256 Hash: {file_hash}\n")

print("\nHash saved to 'hash_output.txt'")
