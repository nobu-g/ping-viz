#!/usr/bin/env bash

set -eu

DIR=$1
DEST=$2

cat - >>"$1/$2".csv
