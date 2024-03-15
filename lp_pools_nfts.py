from datetime import datetime, timedelta
import requests
import shutil

from config import *
from utils import *


# list_of_pools = ['0xc2e9f25be6257c210d7adf0d4cd6e3e881ba25f8', '0xcbcdf9626bc03e24f779434178a73a0b4bad62ed']
# Filter on list of pools. Could be useful later, not using it at the moment.

start_time = datetime.utcnow()
alchemy_url = alchemy_urls[network]

params = {'contractAddress': addresses[network][dex], 'withMetadata': 'true'}
headers = {'accept': 'application/json'}


data = get_latest_data_file()

if data is None:
     logging.info(f"The script is running for the first time.")
     startToken = 0
else:
     startToken = max(data['nft_id'].tolist())+1
     logging.info(f"The script is running from NFT ID {startToken} onwards.")


new_nfts = []

while True:
     params['startToken'] = startToken
     logging.info(f"Calling Alchemy API for NFTs ID {startToken} to {startToken+99}")
     last_update = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
     response = requests.get(f'{alchemy_url}/getNFTsForContract', headers=headers, params=params).json()
     nfts = response['nfts']

     for nft in nfts:
          nft_id = nft['tokenId']
          try:
               metadata_description = nft['description']
          except Exception as e:
               logging.error(f"Could not find the metadata description for NFT ID {nft_id}, with error message {e}.")
               continue
     
          pool_address = get_pool_address_from_metadata(nft_id, metadata_description)
          # if pool_address in list_of_pools:
          new_nfts.append([nft_id, pool_address, last_update])

     if len(nfts) > 0 and len(nfts) < 100:
          # We arrived at the end, no new NFTs
          logging.info(f"All new NFTs have been gathered. Latest NFT ID added: {startToken+len(nfts)-1}")
          break
     elif len(nfts) == 0:
          logging.error(f"The API call is responding with an empty array.")
          break

     startToken+=100


# Define column names
column_names = ['nft_id', 'pool_address', 'last_update']

# Create the DataFrame
df_new_nfts = pd.DataFrame(new_nfts, columns=column_names)

df = pd.concat([data, df_new_nfts], ignore_index=True)
df.reset_index()

file_name = get_file_name(start_time)


# If keep back-up data, copy the active data file with the new file
if keep_backup_data==1:
     logging.info(f"Saving data to {file_name} for future reference")
     df.to_csv(file_name, index=False)

logging.info(f"Erasing active data file {ACTIVE_FILE_NAME} with new data")
df.to_csv(ACTIVE_FILE_NAME, index=False)
