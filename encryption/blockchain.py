import hashlib
import time
class Block:
    def __init__(self, index, previous_hash, timestamp, data, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = self.compute_hash()
    def compute_hash(self):
        block_string = f'{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.nonce}'
        return hashlib.sha256(block_string.encode()).hexdigest()
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
    def create_genesis_block(self):
        return Block(0, '0', time.time(), 'Genesis Block')
    def get_latest_block(self):
        return self.chain[-1]
    def add_block(self, data):
        previous_block = self.get_latest_block()
        new_block = Block(previous_block.index + 1, previous_block.hash, time.time(), data)
        self.chain.append(new_block)
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.compute_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True
if __name__ == '__main__':
    my_blockchain = Blockchain()
    my_blockchain.add_block('First Transaction Data')
    my_blockchain.add_block('Second Transaction Data')
    for block in my_blockchain.chain:
        print(f'Index: {block.index}')
        print(f'Timestamp: {block.timestamp}')
        print(f'Data: {block.data}')
        print(f'Hash: {block.hash}')
        print(f'Previous Hash: {block.previous_hash}')
    print(f'Blockchain Valid: {my_blockchain.is_chain_valid()}')
