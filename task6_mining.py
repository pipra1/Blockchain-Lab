import hashlib
import time

class Block:
    def __init__(self, transactions, previous_hash):
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.timestamp = time.time()
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = str(self.transactions) + str(self.previous_hash) + str(self.nonce) + str(self.timestamp)
        return hashlib.sha256(data.encode()).hexdigest()

    def mine_block(self, difficulty):
        start = time.time()
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()

        end = time.time()

        print("Block mined:", self.hash)
        print("Nonce:", self.nonce)
        print("Mining time:", end - start, "seconds")


# Mining difficulty
difficulty = 3

# Genesis Block
print("Mining Genesis Block...")
block = Block( ["Transaction 1", "Transaction 2", "Transaction 3"], "0" * 64 )
block.mine_block(difficulty)

# Block 1
print("\nMining Block 1...")
block1 = Block( ["Transaction 4", "Transaction 5"], block.hash )
block1.mine_block(difficulty)

# Block 2
print("\nMining Block 2...")
block2 = Block( ["Transaction 6", "Transaction 7"], block1.hash )
block2.mine_block(difficulty)