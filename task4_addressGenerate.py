import hashlib
from ecdsa import SigningKey, SECP256k1
import base58

alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

def base58_encode(data):
    num = int.from_bytes(data, 'big')
    result = ""
    while num > 0:
        num, remainder = divmod(num, 58)
        result = alphabet[remainder] + result

    # Prepend '1' for each leading 0x00 byte
    for byte in data:
        if byte == 0:
            result = '1' + result
        else:
            break
    return result

# 1. Generate keys
private_key = SigningKey.generate(curve=SECP256k1)
public_key = private_key.verifying_key

# 2. Get uncompressed public key bytes
public_bytes = b'\x04' + public_key.to_string()

# 3. Hash160 (SHA-256 followed by RIPEMD-160)
sha_hash = hashlib.sha256(public_bytes).digest()
ripemd_hash = hashlib.new('ripemd160', sha_hash).digest()

# 4. Add Mainnet Version Byte (0x00)
extended_data = b'\x00' + ripemd_hash 

# 5. Calculate Checksum (Double SHA-256, first 4 bytes)
checksum = hashlib.sha256(hashlib.sha256(extended_data).digest()).digest()[:4]

# 6. Combine data and checksum (FIXED HERE)
final_data = extended_data + checksum

# 7. Encode to Base58
address = base58_encode(final_data)

print("Public Key (Hex):", public_key.to_string().hex())
print("SHA-256:", sha_hash.hex())
print("RIPEMD-160:", ripemd_hash.hex())
print("Checksum:", checksum.hex())
print("Bitcoin Address:", address)
print("Final data:", final_data.hex())

decoded = base58.b58decode(address)

print(decoded.hex())