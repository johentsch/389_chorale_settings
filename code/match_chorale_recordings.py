# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: bach
#     language: python
#     name: bach
# ---

# %%
from typing import Tuple
import pandas as pd
from musicbrainz_data import get_musicbrainz_data, musicbrainz_useragent

musicbrainz_useragent()
pd.set_option("display.max_rows", None)

def explode_tuple_column(
    col: pd.Series,
    names: Tuple[str, str] = ("value", "href"),
):
    """Turn a column containing tuples into a DataFrame with two columns.
    Used for formatting a table extracted from HTML using `pd.read_html(url, extract_links="all")`.
    """
    df = pd.DataFrame(col.tolist(), index=col.index)
    df.columns = names
    return df

def explode_all_columns(
    df: pd.DataFrame,
    names: Tuple[str, str] = ("value", "href"),
):
    exploded = []
    for name, column in df.items():
        column_df = explode_tuple_column(column, names)
        col_name = name[0].replace(" ", "_").replace(".", "").lower()
        column_df.columns = [f"{col_name}-{col}" for col in column_df.columns]
        exploded.append(column_df)
    return pd.concat(exploded, axis=1)


# %%
url = "https://en.wikipedia.org/wiki/List_of_chorale_harmonisations_by_Johann_Sebastian_Bach"
wikipedia = pd.read_html(url, extract_links="all")[2]
wikipedia = explode_all_columns(wikipedia)
wikipedia.head()

# %%
id389 = wikipedia["389-value"]
wikipedia389 = wikipedia[id389.str.match("^\d{3}$")].sort_values("389-value")
wikipedia389["389"] = wikipedia389["389-value"].astype("Int64")
wikipedia389["title"] = wikipedia389["chorale_text-value"].str.extract(r"([^\(\[]+)[\(\[]?")
# wikipedia389[wikipedia389["389"].isin(wikipedia389.loc[wikipedia389.duplicated("389"), "389"].values)] # show duplicates to manually create drop_index
drop_index = [
    # indices of 389-duplicates to drop (keeping either the one with the title corresponding to the print, or the lower index) # 389-number
    81, 82, #6
    4,   #8
    112, #13
    119, #14
    264, #23
    164, #40
    281, #48
    132, #57
    20,  #73
    233, #80
    126, #90
    190, #100
    26,  #101
    324, #123
    29,  #124
    55,  #144
    335, #145
    339, #151
    207, #163
    345, #172
    177, #220
    376, #228
    129, #230
    192, #268
    406, #286
    48,  #322
    110, #348
    37, 38, #377
]
wikipedia389 = wikipedia389.drop(drop_index)
wikipedia389.head()


# %%
def get_number(lst: list) -> int:
    dct = lst[0]
    return int(dct["value"])

musicbrainz = get_musicbrainz_data("1b6aec18-db22-4f91-98fb-2a5770183374", rels="work")
musicbrainz = pd.json_normalize(musicbrainz)
musicbrainz["389"] = musicbrainz.attributes.map(get_number).astype("Int64")
musicbrainz["title"] = musicbrainz["work.title"].str.extract(r"[\"“„]([^\"“„]+?)[\"”“]$")
#musicbrainz["bwv"] = musicbrainz["work.title"].str.extract("BWV (\d+)")
musicbrainz = musicbrainz.sort_values("389")
musicbrainz.head()

# %%
#joined = wikipedia389.join(musicbrainz, on="389", lsuffix="_wikipedia", rsuffix="_musicbrainz")
joined = pd.merge(musicbrainz, wikipedia389, how="outer", on="389", suffixes=("_musicbrainz", "_wikipedia")).set_index("389")
print(f"Joined dataframe has {len(joined)} rows.")
joined[["title_musicbrainz", "title_wikipedia"]]

# %% [markdown]
# Quoting from the legend for the column `389` in the Wikipedia table:
#
# > Richter/Kalmus Nos. 130, 219 and 387 are not included in the table: see 'In church cantatas' section below.
#
# [There it says:](https://en.wikipedia.org/wiki/List_of_chorale_harmonisations_by_Johann_Sebastian_Bach#In_church_cantatas)
#
# * No. 130: BWV Anh. 31: "Herr Gott, dich loben alle wir" from a doubtful version of BWV 130
# * No. 219: BWV 218/5 = TWV 1:634/5: "Komm, Gott Schöpfer, Heiliger Geist", by Telemann
# * No. 387: BWV 219/5 = TWV 1:1328/5: "Wo Gott der Herr nicht bei uns hält", by Telemann
#
# The latter two are excluded from the Musicbrainz list, too. This is why the `joined` table has only 387 rows.

# %%
joined[joined["title_wikipedia"].isna()]
