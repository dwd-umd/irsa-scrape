#! /bin/bash

echo '''

    ======================
    RUNNING PRECOMMIT HOOK
    ======================

'''

# Auto-format all python scripts
.venv/bin/autopep8 -ir pipeline1/**
.venv/bin/autopep8 -ir pipeline2/**
.venv/bin/autopep8 -ir pipeline3/**
git add .
