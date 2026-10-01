# Double Burden of Wheat Security: analysis code and data

This repository holds the code, processed data and outputs for the Master's thesis:

> Dhar, S. (2026). *Mapping the double burden of wheat security in conflict-prone Middle Eastern countries: An integrated spatial analysis of conflict, climate, and geopolitical shocks* [Master's thesis, Deakin University].

- **Study area:** Egypt, Lebanon and Yemen. The unit of analysis is the governorate (58 units).
- **Study period:** January 2018 to December 2024. The shock period starts in February 2022 with the Russian invasion of Ukraine.

The analysis covers four objectives:
1. Overlap between armed conflict and wheat production potential (Getis–Ord Gi* hotspots, Fisher's exact test, Spearman correlation, bivariate Moran's I).
2. Wheat import dependence and supplier concentration (UN Comtrade, FAOSTAT).
3. Price transmission and volatility (WFP retail prices, World Bank prices, panel pass-through models).
4. A Double Burden composite vulnerability index (10 indicators, Monte Carlo uncertainty analysis, LISA clusters, IPC validation).

**Archived release:** the Zenodo record and DOI are linked in this repository's description and release page.

---

## Repository structure

```
run_all.py                     runs every analysis step in order (s00 → s10)
requirements.txt               Python 3.11 package versions used
src/config.py                  every analytical parameter and file path (random seed 20260917)
src/s00_prepare_acled.py       combine and quality-check the ACLED event exports
src/s01_study_area.py          governorate boundaries, crosswalks, study-area summary
src/s01b_population.py         WorldPop zonal population
src/s02a_obj1_conflict_hotspots.py  Objective 1: 5-arc-minute grid, Gi* hotspots (9,999 permutations, BH-FDR)
src/s02_obj1_conflict_agro.py  Objective 1: GAEZ v5 wheat potential, overlap, Spearman, bivariate Moran's I
src/s03a_prepare_trade.py      clean UN Comtrade and FAOSTAT Food Balance data
src/s03_obj2_trade_v2.py       Objective 2: composite importer/mirror matrix, supplier shares, HHI, import dependency
src/s05b_conflict_shock.py     conflict rates Feb 2022–Dec 2024 (ACLED aggregates via HDX)
src/s04_obj3_prices_v2.py      Objective 3: volatility, Brown–Forsythe, ADF, pass-through (Driscoll–Kraay, wild bootstrap)
src/s05_covariates_v2.py       rainfall anomaly, Subnational HDI, remoteness, port distance, RWI check
src/s05c_ipc.py                IPC Phase 3+ shares by governorate
src/s06_obj4_index.py          Objective 4: index, PCA weights, Monte Carlo, LISA, IPC validation, typology
src/s07_export_gis.py          GIS layers for Objective 1 (GeoPackage)
src/s07b_export_gis_obj2_4.py  GIS layers for Objectives 2–4 (GeoPackage)
src/s08_excel_figures.py       chart data workbook for the thesis figures
src/s08c_figure_pngs.py        600 dpi PNGs of the charts
src/s09_build_map_package.py   map-ready package for ArcGIS Pro
src/s10_export_supplementary.py  supplementary dataset workbook (Supplementary Material S4)
src/superseded/                earlier versions of steps 3–5, kept for transparency; not used in the final run
tests/                         synthetic-data generator and parameter-recovery test of the pass-through estimator
data/raw/                      raw inputs; only openly licensed small files are included (see DATA_ACCESS.md)
data/crosswalk/                name and code crosswalks to the geoBoundaries ADM1 units
data/processed/                analysis-ready governorate tables and grids produced by s00–s06
outputs/tables/                every statistical result reported in the thesis (CSV and JSON)
outputs/supplementary/         supplementary dataset workbook and index indicator matrices
outputs/gis/                   GeoPackages and field dictionaries used for the maps
outputs/excel/                 chart data workbook
```

## Reproducing the analysis

1. Install Python 3.11, then run `pip install -r requirements.txt`.
2. Download the raw data listed in `DATA_ACCESS.md` and save each file under `data/raw/` with the name shown. The SHA-256 checksums show whether a download matches the version used.
3. Run `python run_all.py`. Each step writes to `data/processed/` and `outputs/`, and logs to `outputs/logs/`.
4. Optional software checks, which do not produce results:
   - `DB_MODE=synthetic python tests/make_synthetic_data.py && DB_MODE=synthetic python run_all.py` runs the pipeline end to end on synthetic inputs.
   - `python tests/test_passthrough_recovery.py` checks that the pass-through estimator recovers known parameters.

Every stochastic step (permutation tests, bootstrap, Monte Carlo) uses the fixed seed in `src/config.py`, so a re-run reproduces the reported values exactly.

The processed tables and outputs are already included. The results can therefore be inspected without re-running anything; start with `outputs/supplementary/DoubleBurden_Supplementary_Dataset.xlsx`.

## Data that are not redistributed

- **Raw ACLED event records**, and ACLED monthly aggregates downloaded from HDX: excluded under ACLED's terms of use. The processed governorate totals derived from them are included.
- **Raw UN Comtrade flows:** excluded under UN Comtrade's terms of use. The country-year indicators and supplier shares derived from them are included.
- **Large public rasters and tables** (GAEZ v5, CHIRPS subnational rainfall, WFP prices, FAOSTAT, World Bank, Global Data Lab, IPC, OCHA P-code tables): not stored here for size. Download them as described in `DATA_ACCESS.md`.

## Maps and charts

- The maps in the thesis were made in ArcGIS Pro from the GeoPackages in `outputs/gis/`.
- The data behind every chart are in `outputs/excel/Thesis_Figures_Data_v2.xlsx`. In the flour-price chart, the gap in Lebanon's series (August 2023 to April 2024) is filled by interpolation for display only, as explained on the `Imputation_note` sheet. All tests use observed prices only.

## Use of software tools

The use of software tools in preparing the thesis is described in Supplementary Material S1 of the thesis.

## Licence

- Code: MIT Licence (see `LICENSE`).
- Processed data and outputs: Creative Commons Attribution 4.0 (CC BY 4.0), subject to the terms of the original data providers.

Please cite the Zenodo record of this repository.
