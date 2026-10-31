from ecdsa import SigningKey, SECP256k1, BadSignatureError

private_key = SigningKey.generate(curve=SECP256k1)
public_key = private_key.verifying_key

print(private_key.to_string().hex())
print(public_key.to_string().hex())

message = input('Enter your message: ')
messageBytes = message.encode()

signature = private_key.sign(messageBytes)

print("Original message: ", message)
print("Signature: ", signature.hex())

try:
  result = public_key.verify(signature, messageBytes)
  print("Original verification: ", result)
except BadSignatureError:
  print("Original verification False")

new_char = 'a' if message[0] != 'a' else 'b'
modified_message = new_char + message[1:]
modified_messageBytes = modified_message.encode()

print("Modified message: ", modified_message)

try:
  result = public_key.verify(signature, modified_messageBytes)
  print("Modified verificaton: ", result)
except BadSignatureError: 
  print("Modified verification: False")

print("Why does verification fail after modifying the message? Because the digital signature was generated for the original message. When even one character is changed, the original signature no longer matches the modified message. Therefore, verification fails.")
