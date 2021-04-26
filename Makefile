DATA := data
CSV_DIR := $(DATA)/csv
CSV := $(CSV_DIR)/all.csv
HOSTS := $(DATA)/hosts.txt
HEATMAP := $(DATA)/heatmap.pdf

SHELL := /bin/bash

.PHONY: all
all: $(HEATMAP)

$(HEATMAP): $(HOSTS) $(CSV)
	python src/cluster_ping.py --csv $(CSV) --hosts $(HOSTS) --out $@

$(HOSTS): $(CSV)
	cat <(cut -d',' -f1 $^) <(cut -d',' -f2 $^) | sort | uniq > $@

$(CSV):
	cat $(CSV_DIR)/* | grep -P '^[^,]+(,[^,]+){5}$' | sort | uniq > $@
