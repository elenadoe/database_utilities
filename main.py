# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 16:35:50 2022

@author: doeringe
"""


import SearchMask
import os
import sys
sys.path.append('Documents/T-POT/Scripts/')

# %%
searchmask = SearchMask.SearchMask()
searchmask.mainloop()

# %%
final_groups = SearchMask.getSelection(
    searchmask.final_groups, "group")
final_sex = SearchMask.getSelection(
    searchmask.final_sex, "sex")
final_data = SearchMask.getSelection(
    searchmask.final_data, "data")
# %%

# TODO get required info from table
# TODO os find data
# TODO os copy data into correct folders
