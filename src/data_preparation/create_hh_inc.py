"""Prepare ``hgen.dta`` to extract monthly household net income."""
import numpy as np
import pandas as pd

from bld.project_paths import project_paths_join as ppj


VARIABLE_NAMES_HGEN = {
    "hid": "ID_HH",
    "syear": "YEAR",
    "hghinc": "HH_NET_INCOME_MONTHLY",
}

RETAINED_COLUMNS_HGEN = list(VARIABLE_NAMES_HGEN.keys())


def main():
    df = pd.read_stata(ppj("IN_DATA", "hgen.dta"), columns=RETAINED_COLUMNS_HGEN)
    df = df.rename(columns=VARIABLE_NAMES_HGEN)

    df.loc[df.HH_NET_INCOME_MONTHLY < 0, "HH_NET_INCOME_MONTHLY"] = np.nan

    df.dropna(subset=["HH_NET_INCOME_MONTHLY"], axis="rows", inplace=True)

    df.HH_NET_INCOME_MONTHLY = df.HH_NET_INCOME_MONTHLY * 12

    df = df.rename(columns={"HH_NET_INCOME_MONTHLY": "HH_NET_INCOME_YEAR"})

    df.to_pickle(ppj("OUT_DATA", "hh_inc.pkl"))


if __name__ == "__main__":
    main()
