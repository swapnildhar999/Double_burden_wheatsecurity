# Data access

Save each raw file under `data/raw/` at the path shown. The analysis scripts read these exact names; `src/config.py` holds the paths.
The SHA-256 checksum identifies the version used in the thesis. A different checksum after re-downloading means the provider has revised the file, and results may differ slightly.
The **In repo** column shows whether the file is included here. Files not included must be downloaded from the source; the reason is given in brackets.

| Dataset | Path under data/raw/ | Source and query | In repo | SHA-256 |
|---|---|---|---|---|
| ACLED events, Egypt | `acled/acled_egypt_2026-08-03.csv` | ACLED Data Export Tool (acleddata.com, registration required); Egypt, all event types, export of 3 Aug 2026 | No (ACLED terms) | `267b42a6cd6eb5132facc68dc8aafb685f67d3d06264344c433a930128e5a3a5` |
| ACLED events, Lebanon | `acled/acled_lebanon_2026-08-03.csv` | As above, Lebanon | No (ACLED terms) | `74c550b04cb8fc488d3accb2a640e59fe9563336e31fdf0927ced4631ca764c0` |
| ACLED events, Yemen | `acled/acled_yemen_2026-08-03.csv` | As above, Yemen | No (ACLED terms) | `a62a912cdbe8f737a77183cf621e8fcd2d58d57627ae34a945c1a3b643918303` |
| ACLED political violence, Egypt, country-month | `acled_hdx/EGY_acled_pv_country_month_2026-09-10.xlsx` | HDX: 'Egypt - Political Violence Events and Fatalities' (as of 10 Sep 2026); sheet 'Data' | No (ACLED terms) | `9530816209af559de80f475008298a63a7fc10bc4a25654f73a2c1ed08b09ab7` |
| ACLED political violence, Lebanon, admin2-month | `acled_hdx/LBN_acled_pv_adm2_month_2026-09-17.xlsx` | HDX: 'Lebanon - Political Violence Events and Fatalities' (as of 17 Sep 2026) | No (ACLED terms) | `967fdfd4175a5991ee7c1274bddadb0eab1849910765406819e1ba772bb5bc69` |
| ACLED political violence, Yemen, admin2-month | `acled_hdx/YEM_acled_pv_adm2_month_2026-09-17.xlsx` | HDX: 'Yemen - Political Violence Events and Fatalities' (as of 17 Sep 2026) | No (ACLED terms) | `6af8391fcec382b16620c37de6164d52a75ee6c95bf705ab17eaee5cda3ce037` |
| UN Comtrade, HS 1001, importer reports | `comtrade/comtrade_hs1001_reporter_EGY_LBN_YEM_2018_2024.csv` | comtradeplus.un.org: annual, HS 1001, reporters Egypt (818), Lebanon (422), Yemen (887), imports, all partners, 2018-2024 | No (Comtrade terms) | `49aaa9d078764590426d1d514c0fac906c058cb78cdb6c40edc4352815f5525e` |
| UN Comtrade, HS 1001, mirror reports | `comtrade/comtrade_hs1001_mirror_to_EGY_LBN_YEM_2018_2024.csv` | comtradeplus.un.org: annual, HS 1001, all reporters, exports to partners 818, 422, 887, 2018-2024 | No (Comtrade terms) | `b57e7b6364e9994f001e384b6b3256a5e33476d545c3b9a9852bae674869b23b` |
| FAOSTAT Food Balances, wheat and products | `faostat/faostat_fbs_wheat_EGY_LBN_YEM_2010_2023.csv` | fao.org/faostat: Food Balances (2010-), Egypt, Lebanon, Yemen, item 'Wheat and products', 2010-2023 | No (size/terms; free download) | `4cee734946c87a590e6d1371164fe14000f7b054c2ac21262d7ad977910e431f` |
| WFP market prices, Egypt | `wfp/wfp_food_prices_egy.csv` | HDX: 'Egypt - Food Prices' (WFP) | No (free download) | `088271f457491be8be32e1f6baa5e015d7d0513920b95e28c5435145be26d0b6` |
| WFP market prices, Lebanon | `wfp/wfp_food_prices_lbn.csv` | HDX: 'Lebanon - Food Prices' (WFP) | No (free download) | `cdd9f0e9c99a3a62a485ed136c3ad4f91869a89051352c5aba3aa7e41dd0058d` |
| WFP market prices, Yemen | `wfp/wfp_food_prices_yem.csv` | HDX: 'Yemen - Food Prices' (WFP) | No (free download) | `bbf33838f3ca995f0419c02c465bf93e6f904f9f3461be43af85d688a02cae60` |
| World Bank Pink Sheet, monthly | `worldbank/CMO-Historical-Data-Monthly_2026-09-02.xlsx` | worldbank.org/commodities: 'Monthly prices' Excel file (downloaded 2 Sep 2026); column 'Wheat, US HRW' | No (free download) | `9fdcfa8a2aed9a1bb545a10c1a5ce036c6a0acd4766f450424ca800b4b5a0225` |
| CHIRPS subnational rainfall, Egypt | `rainfall/egy-rainfall-subnat-full.csv` | HDX: 'Egypt - Subnational Rainfall Indicators' (WFP, CHIRPS) | No (size) | `12eb455ccd03cc0ca2c53394fc27190290fdf537bc4da8700bdbf597904017c0` |
| CHIRPS subnational rainfall, Lebanon | `rainfall/lbn-rainfall-subnat-full.csv` | HDX: 'Lebanon - Subnational Rainfall Indicators' | No (size) | `3088cf7e78c2780a2556339c5b5fcddd2a5cee05b0bc9232f51498bfa1a1ddb9` |
| CHIRPS subnational rainfall, Yemen | `rainfall/yem-rainfall-subnat-full.csv` | HDX: 'Yemen - Subnational Rainfall Indicators' | No (size) | `609fa3909ff294958c6d05f09bf7d8280be0dcc6dadc4fcf9ee06ece1082636e` |
| GDL Subnational HDI, 2018-2023 | `shdi/gdl_shdi_EGY_LBN_YEM_2018_2023.csv` | globaldatalab.org/shdi: Egypt, Lebanon, Yemen, all indicators, 2018-2023 (combined from the yearly downloads) | No (free download) | `a35582c21d79d64ac2f3cbfb617f141799ae7539b33892f776a3ca8c6ac731e6` |
| IPC acute food insecurity, Lebanon | `ipc/ipc_lbn_level1_long.csv` | HDX: 'Lebanon - Acute Food Insecurity Country Data', file ipc_lbn_level1_long.csv | No (free download) | `6e6b01992ba1bfb34bcddeb604299461610a6baa5e6984367281aadb40e1cfc4` |
| IPC acute food insecurity, Yemen | `ipc/ipc_yem_level1_long.csv` | HDX: 'Yemen - Acute Food Insecurity Country Data', file ipc_yem_level1_long.csv | No (free download) | `21ccae5d974e987e4b460b83ecb012b9e1ff344e160e4f42c443805dc4919d63` |
| Relative Wealth Index, Egypt | `rwi/egy_relative_wealth_index.csv` | HDX: 'Relative Wealth Index' (Meta Data for Good), Egypt | No (free download) | `57a1cf1788836e75c39a363ac58a48c81130de568849bd852d7adb4c7060e1c0` |
| OCHA administrative boundary tables, Egypt | `cod/egy_admin_boundaries.xlsx` | HDX: 'cod-ab-egy', tabular Excel file | No (free download) | `9d8ed34df98f328048b0c2e8be28f2fcab27484f00b3f6fd55aa8851850a0250` |
| OCHA administrative boundary tables, Lebanon | `cod/lbn_admin_boundaries.xlsx` | HDX: 'cod-ab-lbn', tabular Excel file | No (free download) | `02d9bdbc54963bff92c813cd200e15fcdbb3e5436f98a4dc7d5b8be1c4855aba` |
| OCHA administrative boundary tables, Yemen | `cod/yem_admin_boundaries.xlsx` | HDX: 'cod-ab-yem', tabular Excel file | No (free download) | `85864561186541e44df7b55a4ef6725e4de40175881d5ce162eac8b9e9577135` |
| GAEZ v5 RES05-YCX HILM | `gaez/GAEZ-V5.RES05-YCX.HP0120.AGERA5.HIST.WHE.HILM.tif` | FAO GAEZ v5 public bucket: https://storage.googleapis.com/fao-gismgr-gaez-v5-data/DATA/GAEZ-V5/MAPSET/<CODE>/<file> (see src/config.py) | No (size) | `d2bed2d1e087e005678da145bf6e777a2a9cfd157421dc975c9897f0b53f8446` |
| GAEZ v5 RES05-YCX HRLM | `gaez/GAEZ-V5.RES05-YCX.HP0120.AGERA5.HIST.WHE.HRLM.tif` | FAO GAEZ v5 public bucket: https://storage.googleapis.com/fao-gismgr-gaez-v5-data/DATA/GAEZ-V5/MAPSET/<CODE>/<file> (see src/config.py) | No (size) | `678d2523344bf0f3fffc564e6d556ce65c0e03c2a50f5371fa62ccda6e2a6084` |
| GAEZ v5 RES06-HAR WSI | `gaez/GAEZ-V5.RES06-HAR.WHE.WSI.tif` | FAO GAEZ v5 public bucket: https://storage.googleapis.com/fao-gismgr-gaez-v5-data/DATA/GAEZ-V5/MAPSET/<CODE>/<file> (see src/config.py) | No (size) | `222eda935982daf3b0c5e24dd73947c102787e6c3c38c2aca4e4eac09d547f32` |
| GAEZ v5 RES06-HAR WST | `gaez/GAEZ-V5.RES06-HAR.WHE.WST.tif` | FAO GAEZ v5 public bucket: https://storage.googleapis.com/fao-gismgr-gaez-v5-data/DATA/GAEZ-V5/MAPSET/<CODE>/<file> (see src/config.py) | No (size) | `737d956434c5257131d2d64de2060bd4d40141cd6378ca50f84c32e45255b7af` |
| GAEZ v5 RES06-PRD WSI | `gaez/GAEZ-V5.RES06-PRD.WHE.WSI.tif` | FAO GAEZ v5 public bucket: https://storage.googleapis.com/fao-gismgr-gaez-v5-data/DATA/GAEZ-V5/MAPSET/<CODE>/<file> (see src/config.py) | No (size) | `dfc35f3bcbba64d9626a8f9502a893214247b70822efe1cd05aa1b7763e49914` |
| GAEZ v5 RES06-PRD WST | `gaez/GAEZ-V5.RES06-PRD.WHE.WST.tif` | FAO GAEZ v5 public bucket: https://storage.googleapis.com/fao-gismgr-gaez-v5-data/DATA/GAEZ-V5/MAPSET/<CODE>/<file> (see src/config.py) | No (size) | `f5861002576c5ca9ea3fd410a3725f92ac2776841d232781eb0526c08cf83836` |
| GAEZ v5 RES06-YLD WST | `gaez/GAEZ-V5.RES06-YLD.WHE.WST.tif` | FAO GAEZ v5 public bucket: https://storage.googleapis.com/fao-gismgr-gaez-v5-data/DATA/GAEZ-V5/MAPSET/<CODE>/<file> (see src/config.py) | No (size) | `e497f21275d7027479468994d0a641b2b604074cfb0dd8f215b9b84d7623ec51` |
| GAEZ v5 RES07-QGA WST | `gaez/GAEZ-V5.RES07-QGA.WHE.WST.tif` | FAO GAEZ v5 public bucket: https://storage.googleapis.com/fao-gismgr-gaez-v5-data/DATA/GAEZ-V5/MAPSET/<CODE>/<file> (see src/config.py) | No (size) | `c5ff02a404d7a0dec07d0712374b3d17c3fcb7171c516c6c4ca10849b7b6e1bd` |
| WorldPop 2020 constrained, 1 km, R2025A | `worldpop/egy_pop_2020_CN_1km_R2025A_UA_v1.tif` | worldpop.org: Population Counts, constrained, UN-adjusted, 2020, R2025A | Yes (CC BY 4.0) | `8375d463629d108cb3d7cee284eb392e215444b7c451d77e10f73288e64c76ff` |
| WorldPop 2020 constrained, 1 km, R2025A | `worldpop/lbn_pop_2020_CN_1km_R2025A_UA_v1.tif` | worldpop.org: Population Counts, constrained, UN-adjusted, 2020, R2025A | Yes (CC BY 4.0) | `a96a281dac61a8a4a8d13cec4071d08593d934b16ea6cba6c229d38420bde4be` |
| WorldPop 2020 constrained, 1 km, R2025A | `worldpop/yem_pop_2020_CN_1km_R2025A_UA_v1.tif` | worldpop.org: Population Counts, constrained, UN-adjusted, 2020, R2025A | Yes (CC BY 4.0) | `2c7143dc7511519e3b8f8dd0e52cdb8065f0057674b157444d48c75304d8fdb3` |
| geoBoundaries gbOpen ADM1 (geoboundaries.org) | `boundaries/EGY_adm1.geojson` | geoBoundaries gbOpen ADM1 (geoboundaries.org) | Yes (open licence) | `c8b4bb9dc215cf302d030f3e93c0f249ed97e50951f058323346d510ec48886f` |
| geoBoundaries gbOpen ADM1 (geoboundaries.org) | `boundaries/EGY_meta.json` | geoBoundaries gbOpen ADM1 (geoboundaries.org) | Yes (open licence) | `9d17d61a415ea4506a0ff2dad81140de902cc2a62b053ef8bf7c864630c4e574` |
| geoBoundaries gbOpen ADM1 (geoboundaries.org) | `boundaries/LBN_adm1.geojson` | geoBoundaries gbOpen ADM1 (geoboundaries.org) | Yes (open licence) | `a96e1ddee1b8599b715ae2db7b973bc29896412bf331e38a696ab86d6d1bf6d0` |
| geoBoundaries gbOpen ADM1 (geoboundaries.org) | `boundaries/LBN_meta.json` | geoBoundaries gbOpen ADM1 (geoboundaries.org) | Yes (open licence) | `9619821532e16e497eeec238b51f0ff823c24ceb80d00ad3c14d1ed85ca1b98e` |
| geoBoundaries gbOpen ADM1 (geoboundaries.org) | `boundaries/YEM_adm1.geojson` | geoBoundaries gbOpen ADM1 (geoboundaries.org) | Yes (open licence) | `c8f37864007dd5a75dcd069d7b54823db7876dd42ad217bf48420f05304944b5` |
| geoBoundaries gbOpen ADM1 (geoboundaries.org) | `boundaries/YEM_meta.json` | geoBoundaries gbOpen ADM1 (geoboundaries.org) | Yes (open licence) | `001bb48d87a8719e82d5d1128219a7f63cd1986dfef70ae12dda42426d246575` |
| Natural Earth admin-0 countries (context map) | `boundaries/ne_countries.geojson` | Natural Earth admin-0 countries (context map) | Yes (open licence) | `239eec57ac17f100a11e2536cffc56752c318b50ae765b0918ff7aab4ce8f255` |
| Grain-import ports (compiled by the author) | `ports/grain_ports.csv` | Compiled from public port information; approximate harbour centroids | Yes | `f97abf28cff683cb496338b85d7dcf229772afabcaac2929b1f6c3b5fd17a5cc` |

## Derived inputs built by the pipeline
- `data/raw/acled/acled_EGY_LBN_YEM_combined.csv`: built by `s00_prepare_acled.py` from the three ACLED exports.
- `data/raw/ipc/ipc_adm1_phase3plus.csv`: built by `s05c_ipc.py` from the IPC level-1 files.

## Terms of use
- ACLED data are used under ACLED's terms of use. Raw events and HDX aggregates are not redistributed; only derived governorate totals are included in `data/processed/`.
- UN Comtrade data are used under the UN Comtrade terms. Raw flows are not redistributed; only the derived indicators in `outputs/tables/` are included.
- All other sources are openly available. Cite them as listed in the thesis reference list.
