import hashlib, time
from collections import Counter

class Block:
  def __init__(self, transactions, miner, previous_hash, difficulty = 3):
    self.transactions = transactions
    self.nonce = 0
    self.miner = miner
    self.time = time.time()
    self.previous_hash = previous_hash
    self.difficulty = difficulty
    self.hash = self.mine_block()

  def calculate_hash(self):
    data = str(self.transactions) + str(self.previous_hash) + str(self.time) + str(self.nonce)
    return hashlib.sha256(data.encode()).hexdigest()

  def mine_block(self):
    start = time.time()
    while True:
      self.hash = self.calculate_hash()
      if self.hash[:self.difficulty] == '0' * self.difficulty:
        return self.hash
      self.nonce += 1


class Blockchain:
  def __init__(self, difficulty=3):
    self.difficulty = difficulty
    self.chain = [Block("Genesis Block", "System", "0" * 64, self.difficulty)]

  def add_block(self, data, miner):
    previous_hash = self.chain[-1].hash
    new_block = Block(data, miner, previous_hash, self.difficulty)
    self.chain.append(new_block)

  def validate_chain(self):
    for i in range(1, len(self.chain)):
      current = self.chain[i]
      previous = self.chain[i-1]

      if current.hash != current.calculate_hash():
        print(f"Invalid block hash at index {i}")
        return False
      if current.hash[:self.difficulty] != '0' * self.difficulty:
        print(f"Block {i} does not meet the Proof-of-Work difficulty target")
        return False
      if current.previous_hash != previous.hash:
        print(f"Invalid previous hash link at index {i}")
        return False
    print("Blockchain is valid")
    return True

  def get_chain_length(self):
    return len(self.chain)

  def verify_51_percent_attack(self):
    total_blocks = len(self.chain)
    miner_counts = Counter(block.miner for block in self.chain)

    attack = False
    dominant_miner = ""
    for miner, count in miner_counts.items():
      percentage = (count / total_blocks) * 100
      if percentage >= 51.0:
        attack = True
        dominant_miner = miner

    if attack:
      print("51 % Attack detected, ", dominant_miner)
    else:
      print("No 51% attack detected")
    return attack


my_blockchain = Blockchain()
my_blockchain.add_block("Alice sent Bob 5 BTC", miner="Miner_A")
my_blockchain.verify_51_percent_attack()
my_blockchain.add_block("Bob sent Charlie 2 BTC", miner="Miner_B")
my_blockchain.verify_51_percent_attack()
my_blockchain.add_block("Charlie sent David 1 BTC", miner="Miner_A")
my_blockchain.verify_51_percent_attack()
my_blockchain.add_block("David sent Eve 0.5 BTC", miner="Miner_B")
my_blockchain.add_block("David sent Eve 0.5 BTC", miner="Miner_B")
my_blockchain.add_block("David sent Eve 0.5 BTC", miner="Miner_B")
my_blockchain.verify_51_percent_attack()
