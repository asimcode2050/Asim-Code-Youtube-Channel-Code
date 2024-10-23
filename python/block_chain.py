import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash
    def __repr__(self):
        return f"Block(index={self.index}, hash={self.hash}, previous_hash={self.previous_hash}, timestamp={self.timestamp}, data={self.data})"
    
def calculate_hash(index, previous_hash, timestamp,data):
        value = f"{index}{previous_hash}{timestamp}{data}".encode()
        return hashlib.sha256(value).hexdigest()
    
def create_genesis_block():
        return Block(0,"0", int(time.time()), "Genesis Block",calculate_hash(0,"0", int(time.time()),"Genesis Block"))
    
def create_new_block(previous_block, data):
        index = previous_block.index + 1
        timestamp = int(time.time())
        hash = calculate_hash(index, previous_block, timestamp, data)
        return Block(index, previous_block.hash, timestamp, data, hash)


if __name__ == "__main__":
      blockchain = [create_genesis_block()]
      num_blocks_to_add = 10

      for i in range(num_blocks_to_add):
            new_block_data =f"Block {i+1} Data"
            new_block = create_new_block(blockchain[-1],new_block_data)
            blockchain.append(new_block)
            print(new_block)

    


    


