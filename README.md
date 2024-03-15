# LP Pools NFTs
The objective of this script is to get the list of NFT positions for all liquidity provider of a DEX.

Input = Chain (Choose between ethereum, arbitrum, optimism and base) and DEX (Uniswap v3 is the only support DEX at the moment)

Output = A CSV File with the list of all LP Position NFT IDs with the relevant pool address


# Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.10+ installed
- An Alchemy API key for network connections


# Installation
Follow these steps to install:

- Clone the repository:
```git clone git@github.com:cyril-dfi/lp_pools_nfts.git```

- Install required Python packages:
```pip install -r requirements.txt```

- Create a `.env` file in the root directory with your Alchemy API key:
```
ALCHEMY_KEY=your_alchemy_api_key_here
```

# Usage
To use the project, execute the following command line:
```
python lp_pools_nfts.py -n yournetwork -d yourdex
```
Replace "yournetwork" by a compatible chain (`ethereum`, `arbitrum`, `optimism` or `base`) and "yourdex" by a compatible DEX (only `uniswapv3` is supported at the moment)

The output will be stored in the following file 
```
ACTIVE_FILE_NAME = f'data_{network}_{dex}.csv'
```
The output file will have 3 columns: `nft_id`, `pool_address`, and `last_update`
