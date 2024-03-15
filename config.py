import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

supported_networks = ['ethereum', 'arbitrum', 'optimism', 'base']

# Connect to JSON-RPC node
alchemy_key = os.environ.get('ALCHEMY_KEY')


alchemy_urls = {}
alchemy_urls['ethereum'] = f'https://eth-mainnet.g.alchemy.com/nft/v3/{alchemy_key}'
alchemy_urls['arbitrum'] = f'https://arb-mainnet.g.alchemy.com/nft/v3/{alchemy_key}'
alchemy_urls['optimism'] = f'https://opt-mainnet.g.alchemy.com/nft/v3/{alchemy_key}'
alchemy_urls['base'] = f'https://base-mainnet.g.alchemy.com/nft/v3/{alchemy_key}'


addresses = {}
for supported_network in supported_networks:
  addresses[supported_network] = {}

# Uniswap v3 NFT Address # Cf "NonfungiblePositionManager" on https://docs.uniswap.org/contracts/v3/reference/deployments
addresses['ethereum']['uniswapv3'] = '0xc36442b4a4522e871399cd717abdd847ab11fe88'
addresses['arbitrum']['uniswapv3'] = '0xc36442b4a4522e871399cd717abdd847ab11fe88'
addresses['optimism']['uniswapv3'] = '0xc36442b4a4522e871399cd717abdd847ab11fe88'
addresses['base']['uniswapv3'] = '0x03a520b32C04BF3bEEf7BEb72E919cf822Ed34f1'