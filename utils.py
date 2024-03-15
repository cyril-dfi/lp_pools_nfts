import argparse
import logging
import pandas as pd
import re
import time

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

parser = argparse.ArgumentParser(description = "You need to specify the network (-n) and dex (-d)")
parser.add_argument("-n", "--network", help = "Network or chain (choose between ethereum, arbitrum, optimism or base)", required = True)
parser.add_argument("-d", "--dex", help = "Dex (uniswapv3)", required = True)
parser.add_argument("-k", "--keep_backup_data", help = "Keep all data files", required = False, type=int, default = 0)

argument = parser.parse_args()

logging.info("You have used '-n' or '--network' with argument: {0}".format(argument.network))
network = argument.network

logging.info("You have used '-d' or '--dex' with argument: {0}".format(argument.dex))
dex = argument.dex

keep_backup_data = 0
if argument.keep_backup_data:
     logging.info("You have used '-k' or '--keep_backup_data' with argument: {0}".format(argument.keep_backup_data))
     keep_backup_data = argument.keep_backup_data
     if keep_backup_data==1:
          logging.info("You have have decided to keep the backup data. Every file will be historicized.")


ACTIVE_FILE_NAME = f'data_{network}_{dex}.csv'

def get_pool_address_from_metadata(nft_id, text):
     # Regular expression to match the pool address
     regexp = r"Pool Address: (0x[a-fA-F0-9]{40})"

     if isinstance(text, (str, bytes)):
          # Find all matches in the text
          matches = re.findall(regexp, text)
     else:
          return None
          print("The 'text' variable is not a string or bytes-like object.")

     # Assuming there's at least one match, print the first one
     if matches:
          return matches[0]
     else:
          logging.error(f"Could not find the pool address for NFT ID {nft_id} with text: {text}")
          return None


def get_file_name(time):
     file_name = time.strftime(f"data_{network}_{dex}_%Y_%m_%d__%H.csv")
     return file_name


def get_latest_data_file():
     logging.info(f"Fetching lastest data file {ACTIVE_FILE_NAME}")
     try:
          df = pd.read_csv(ACTIVE_FILE_NAME)
          return df
     except Exception as e:
          logging.info(f"The script did not find a {ACTIVE_FILE_NAME} file. It assumes it is running for the first time.")
          return None