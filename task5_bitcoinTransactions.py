from bitcoinlib.keys import Key
from bitcoinlib.transactions import Transaction, SIGHASH_ALL

sender_key = Key(network='testnet')
receiver_key = Key(network='testnet')

tx = Transaction(network='testnet', witness_type='legacy')

tx.add_input(
  prev_txid='a' * 64, 
  output_n=0, 
  value=100000,
  keys=sender_key, 
  script_type='sig_pubkey',
  witness_type='legacy'
)

tx.add_output(
  value=90000, 
  address=receiver_key.address())

tx.sign(keys=sender_key, hash_type=SIGHASH_ALL)

# 6. Display
print("Sender Address  :", sender_key.address())
print("Receiver Address:", receiver_key.address())
print("Signature valid :", tx.verify())
print("TXID            :", tx.txid)
print("\nSigned Transaction Hex:\n", tx.as_hex())
print()
tx.info()
