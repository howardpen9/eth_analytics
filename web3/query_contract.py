# We use Alchemy to connect to a node and query smart contracts directly.
import json

# Import Alchemy API Key
from dotenv import dotenv_values

config = dotenv_values("../.env")

# I prefer Alchemy as the pricing plans are friendly for people who aren't loaded : )
w3 = Web3(
    Web3.HTTPProvider("https://eth-mainnet.alchemyapi.io/v2/" + config["API_KEY"])
)

with open("abi.json") as f:
    abi = json.load(f)

contract_address = Web3.toChecksumAddress("0x5d3a536e4d6dbd6114cc1ead35777bab948e3643")

# Address field should be the checksum address at which the contract was deployed
compound_dai_contract = w3.eth.contract(address=contract_address, abi=abi)

# past blocks, requires archive node
total_supply = compound_dai_contract.functions.totalSupply().call(
    block_identifier=-100000
)
# total_supply = compound_dai_contract.functions.totalSupply().call(block_identifier='latest')

# total supply in cDAI, use conversion factor
print(total_supply / 46.72)
