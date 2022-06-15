# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 16:51:05 2022

@author: doeringe
"""

# %%
import os
import getpass
import pandas as pd

from pysciebo import ScieboClient

# %%


class DownloadData:
    def downloadData(self):
        url = "https://uni-koeln.sciebo.de"
        username = input("Enter sciebo user domain: ")
        password = getpass.getpass('Enter password:')

        # Login
        client = ScieboClient(url, username, password)

        # %%
        # Download a file from sciebo (local path is optional)
        self.store_at = input("A copy of the demographics table will be stored locally.\
                         Where should I store it? Enter desired name for table \
                         at end of path. ")
        # Documents/T-POT/Participants.csv
        client.download("T-POT Orga/Participants.csv", self.store_at)
        print("File successfully downloaded and stored to ", self.store_at)

    # TODO get data in csv file
