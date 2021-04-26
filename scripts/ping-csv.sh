#!/usr/bin/env bash

set -eu

NUM_PACKETS=10
HOST=$1

echo -n ${HOST},
ping -c ${NUM_PACKETS} ${HOST} | tail -1 | sed -r 's/^.+ = (.*) ms$/\1/' | tr '/' ','
