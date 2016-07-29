PYTHON=-I/Users/jmorton/Applications/anaconda2/include/python2.7
NUMPY=-I/Users/jmorton/Applications/anaconda2/pkgs/numpy-1.10.2-py27_0/lib/python2.7/site-packages/numpy/core/include/
SRC=src/c
LIB=lib
BIN=bin
LD_LIBRARY_PATH?=$(CURDIR)/$(LIB)
export LD_LIBRARY_PATH


ccdc:
	gcc -std=c99 -g -shared -fpic $(SRC)/ccdc.c $(PYTHON) $(NUMPY) -o $(LIB)/ccdc.so
	gcc -std=c99 -Wall -o $(BIN)/ccdc $(SRC)/ccdc.c

index:
	gcc -std=c99 -g -shared -fpic $(SRC)/index.c -o $(LIB)/index.so
	gcc -std=c99 -o $(BIN)/index $(SRC)/index.c

mylib:
	gcc -std=c99 -g -shared -fpic $(SRC)/mylib.c -o $(LIB)/mylib.so
	gcc -std=c99 -o $(BIN)/mylib $(SRC)/mylib.c

build: ccdc index mylib

run: ccdc
	$(BIN)/ccdc

debug: ccdc
	gdb $(BIN)/ccdc

clean:
	rm $(LIB)/*
	rm $(BIN)/*

test: build
	python src/python/test.py

notebook: build
	jupyter notebook --notebook-dir="src/python" --no-browser

ipython: build
	cd src/python; \
	ipython

docker: FORCE
	mkdir -p ./docker/lcmap-model-wrapper/science
	cp -rf ./bin ./docker/lcmap-model-wrapper/science
	cp -rf ./lib ./docker/lcmap-model-wrapper/science
	cp -rf ./src ./docker/lcmap-model-wrapper/science
	cp -rf ./config ./docker/lcmap-model-wrapper/science/.usgs
	docker build -t "usgseros/lcmap-model-wrapper" docker/lcmap-model-wrapper
	rm -rf ./docker/lcmap-model-wrapper/science

docker-cleanup:
	docker rm $(shell docker ps --no-trunc --all --quiet)

docker-bash: docker
	@docker run \
	-e LD_LIBRARY_PATH=/home/science/lib \
        -it usgseros/lcmap-model-wrapper \
	/bin/bash

FORCE:
