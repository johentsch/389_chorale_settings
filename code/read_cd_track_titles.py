# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import os
import pandas as pd
pd.set_option("display.max_rows", None)

# %%
path = "/mnt/DATA/Music/Choral Classics_ Bach (Chorales)/"
regex = r"0(?P<cd>\d)-(?P<track>\d+) (?P<title>.+)"
files = pd.DataFrame({"filename": os.listdir(path)})
files = pd.concat([files, files.filename.str.extract(regex)], axis=1)
files

# %%
