# Blockchain Lab

This repository contains Python implementations and demonstrations of
fundamental blockchain and Bitcoin concepts. Each task is a standalone script
that can be run from the project directory.

## Topics covered

| File | Topic | Description |
| --- | --- | --- |
| [`task1_sha256.py`](./task1_sha256.py) | SHA-256 and avalanche effect | Hashes a message, changes one character, and compares the resulting hashes. |
| [`task2_merkleTree.py`](./task2_merkleTree.py) | Merkle tree | Calculates transaction leaf hashes, parent hashes, and a Merkle root. |
| [`task3.signature.py`](./task3.signature.py) | Digital signatures | Generates a secp256k1 key pair, signs a message, and verifies the signature before and after the message is modified. |
| [`task4_addressGenerate.py`](./task4_addressGenerate.py) | Bitcoin address generation | Generates a key pair and derives a Base58Check-encoded Bitcoin mainnet address. |
| [`task5_bitcoinTransactions.py`](./task5_bitcoinTransactions.py) | Bitcoin transactions | Creates and signs a legacy Bitcoin testnet transaction, then verifies and displays it. |
| [`task6_mining.py`](./task6_mining.py) | Proof-of-Work mining | Mines a genesis block and two additional blocks using a configurable difficulty. |
| [`task7_51Attack.py`](./task7_51Attack.py) | 51% attack detection | Builds a simple blockchain and detects when one miner controls at least 51% of the blocks. |
| [`practice.py`](./practice.py) | Practice implementation | Additional blockchain and 51% attack practice code. |

## Requirements

- Python 3.8 or newer
- `ecdsa`
- `base58`
- `bitcoinlib`

The first two tasks and the mining examples use only Python's standard
library. The remaining scripts require third-party packages.

## Installation

Create and activate a virtual environment, then install the dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install ecdsa base58 bitcoinlib
```

On Windows PowerShell, activate the environment with:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install ecdsa base58 bitcoinlib
```

## Running the examples

Run any script with Python:

```bash
python task1_sha256.py
python task2_merkleTree.py
python task3.signature.py
python task4_addressGenerate.py
python task5_bitcoinTransactions.py
python task6_mining.py
python task7_51Attack.py
```

`task1_sha256.py` and `task3.signature.py` prompt for a message. The mining
and 51% attack examples perform proof-of-work, so execution time depends on
the difficulty configured in each script.

## Learning objectives

After completing the exercises, you should be able to:

- Explain how SHA-256 hashes identify data and demonstrate the avalanche effect.
- Construct a Merkle tree from transaction data.
- Generate and verify elliptic-curve digital signatures.
- Describe the steps involved in creating a Base58Check Bitcoin address.
- Create, sign, and verify a basic Bitcoin transaction.
- Explain nonce-based proof-of-work mining.
- Identify a simple majority-miner condition associated with a 51% attack.

## Disclaimer

These scripts are educational demonstrations. They are not production-ready
implementations of a blockchain, wallet, transaction system, or attack
detection mechanism. Do not use generated private keys or transactions with
real funds.
