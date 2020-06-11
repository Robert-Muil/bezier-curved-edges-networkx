#!/usr/bin/env bash
url="https://snap.stanford.edu/data/facebook_combined.txt.gz"
fpath="$(basename url)"
wget "$url"
echo "fetched \"$fpath\""