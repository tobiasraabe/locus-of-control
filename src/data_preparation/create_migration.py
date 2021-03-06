"""Prepares ``ppfad.dta`` to extract MIGRATION_STATUS."""
import numpy as np
import pandas as pd

from bld.project_paths import project_paths_join as ppj


VARIABLE_NAMES_PPFAD = {
    "pid": "ID",  # permanent personal id
    "migback": "MIGRATION_STATUS",
}

RETAINED_COLUMNS_PPFAD = list(VARIABLE_NAMES_PPFAD.keys())


def main():
    df = pd.read_stata(ppj("IN_DATA", "ppfad.dta"), columns=RETAINED_COLUMNS_PPFAD)
    df = df.rename(columns=VARIABLE_NAMES_PPFAD)

    migration_status = {
        "[-1] keine Angabe": np.nan,
        "[1] kein Migrationshintergrund": False,
        "[2] direkter Migrationshintergrund": True,
        "[3] indirekter Migrationshintergrund": True,
        "[4] Migrationshintergrund - n. w. differenz.": True,
    }
    df.MIGRATION_STATUS.replace(migration_status, inplace=True)

    df.to_pickle(ppj("OUT_DATA", "migration.pkl"))


if __name__ == "__main__":
    main()
