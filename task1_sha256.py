
import hashlib

# Take input from user
message = input("Enter a message: ")

# Calculate SHA-256 hash
hash1 = hashlib.sha256(message.encode()).hexdigest()

print("\nOriginal Message:", message)
print("Original Hash:", hash1)

# Change the first character
if message:
    new_char = "A" if message[0] != "A" else "B"
    modified_message = new_char + message[1:]
else:
    modified_message = "A"

# Calculate modified hash
hash2 = hashlib.sha256(modified_message.encode()).hexdigest()

print("\nModified Message:", modified_message)
print("Modified Hash:", hash2)

# Compare hashes
if hash1 == hash2:
    print("Hashes are SAME")
else:
    print("Hashes are DIFFERENT")

print("\nProperty: Avalanche Effect")
