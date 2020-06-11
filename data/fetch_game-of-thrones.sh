#!/usr/bin/env bash
urls="https://raw.githubusercontent.com/mathbeveridge/gameofthrones/master/data/got-s<season>-<type>.csv"
NSEASONS=8
for ((season = 1; season <= NSEASONS; season++)); do
  for type in "edges" "nodes"; do
    url=${urls/<season>/$season}
    url=${url/<type>/$type}
    fpath="$(basename $url)"
    wget "$url"
    echo "fetched \"$fpath\""
  done
done
