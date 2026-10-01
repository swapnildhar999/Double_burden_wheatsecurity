"""Run the full Double Burden pipeline in order.

    python run_all.py                    # real data in data/raw
    DB_MODE=synthetic python run_all.py  # code test on synthetic inputs (tests/synthetic) - NOT results
"""
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

import s00_prepare_acled, s01_study_area, s01b_population, s02a_obj1_conflict_hotspots, s02_obj1_conflict_agro, s03a_prepare_trade, s03_obj2_trade_v2, s05b_conflict_shock, s04_obj3_prices_v2, s05_covariates_v2, s05c_ipc, s06_obj4_index, s07_export_gis, s07b_export_gis_obj2_4, s10_export_supplementary  # noqa: E402

STEPS = [s00_prepare_acled, s01_study_area, s01b_population, s02a_obj1_conflict_hotspots, s02_obj1_conflict_agro,
         s03a_prepare_trade, s03_obj2_trade_v2, s05b_conflict_shock, s04_obj3_prices_v2, s05_covariates_v2, s05c_ipc,
         s06_obj4_index, s07_export_gis, s07b_export_gis_obj2_4, s10_export_supplementary]

if __name__ == "__main__":
    for step in STEPS:
        t0 = time.time()
        print(f"\n=== {step.__name__} ===")
        step.main()
        print(f"=== {step.__name__} finished in {time.time() - t0:.1f} s ===")
