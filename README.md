# irsa-scrape

## What's This?

This is a bash-python script to scrape irsa. It uses selenium to control a Chrome browser instance as it loads [this view](https://irsa.ipac.caltech.edu/applications/wise/#id=Hydra_wise_wise_5&RequestClass=ServerRequest&DoSearch=true&subsize=0.16666666800000002&cat_overlay=_none_&schema=allsky-4band&band=1,2,3,4&obj_name=606%20Brangane&obj_naifid=2000606&obj_prim_designation=2000606&preliminary_data=no&projectId=wise&searchName=wise_5&shortDesc=Solar%20System%20Object/Orbit&isBookmarkAble=true&isDrillDownRoot=true&isSearchResult=true) from [irsa.ipac.caltech.edu](irsa.ipac.caltech.edu) then performs clicks and keystrokes to load the target data, and then parses the enriched html to extract the target data from html tables and then outputs it into a csv file.

## Quick Start

From a Mac:

- Install `chromedriver` with `brew cask install chromedriver`

- Make sure you also have the following installed and find-able in your `$PATH` paths:

  - `git`
  - `python3`
  - `pipenv` (run `pip3 install --user pipenv`; you might need to add `~/.local/bin` to your `$PATH` paths).

- Run `git clone https://github.com/dwd-umd/irsa-scrape.git; cd irsa-scrape`

- Run `cp .env-template .env` and set the value of `PYTHON_3_5_OR_HIGHER` to point to your `python3` executable

- Run `source _initial_setup.sh`

- Run `./_run_pipeline`

The pipeline script will execute two python scripts: `pipeline/stage1.py` and `pipeline/stage2.py`. The first stage generates the enriched html to `pipeline/data1/enriched.html`, the second stage extracts the data to a csv file to `pipeline/data2/output.csv`. If either of these output files is already created, the pipeline will skip that stage. To force the pipeline to recompute either stage, add flags `-f1` and/or `-f2` to 'force' stage1 and/or stage2 to re-run.
