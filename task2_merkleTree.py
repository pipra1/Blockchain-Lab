
import hashlib

# SHA-256 hash function
def sha256(data):
    return hashlib.sha256(data.encode()).hexdigest()

# Four transactions
transactions = [
    "Alice pays Bob 5 BTC",
    "Bob pays Charlie 2 BTC",
    "Charlie pays David 1 BTC",
    "David pays Eva 3 BTC"
]

# Step 1: Calculate leaf hashes
h1 = sha256(transactions[0])
h2 = sha256(transactions[1])
h3 = sha256(transactions[2])
h4 = sha256(transactions[3])

print("Leaf Hashes:")
print("H1:", h1)
print("H2:", h2)
print("H3:", h3)
print("H4:", h4)

# Step 2: Calculate parent hashes
h12 = sha256(h1 + h2)
h34 = sha256(h3 + h4)

print("\nParent Hashes:")
print("H12:", h12)
print("H34:", h34)

# Step 3: Calculate Merkle Root
root = sha256(h12 + h34)

print("\nMerkle Root:", root)
