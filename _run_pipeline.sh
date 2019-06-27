#!/bin/bash

echo '''
    ==========================
        BEGIN SCRAPER
    ==========================
'''

if [[ ! -f pipeline/data1/enriched.html || $1 == '-f1' ]]; then
    python pipeline/stage1.py
fi

if [[ ! -f pipeline/data2/output.csv || $1 == '-f2' || $2 == '-f2' ]]; then
    python pipeline/stage2.py
fi

echo '''
    ==========================
        END SCRAPER
    ==========================
'''
