PYTHON=-I/Users/jmorton/Applications/anaconda2/include/python2.7
NUMPY=-I/Users/jmorton/Applications/anaconda2/pkgs/numpy-1.10.2-py27_0/lib/python2.7/site-packages/numpy/core/include/
SRC=src/c
LIB=lib
BIN=bin
LD_LIBRARY_PATH?=$(CURDIR)/$(LIB)
export LD_LIBRARY_PATH


ccdc:
	gcc -std=c99 -g -shared -fpic $(SRC)/ccdc.c $(PYTHON) $(NUMPY) -o $(LIB)/ccdc.so
	gcc -std=c99 -o $(BIN)/ccdc $(LIB)/ccdc.so

index:
	gcc -std=c99 -g -shared -fpic $(SRC)/index.c -o $(LIB)/index.so
	gcc -std=c99 -o $(BIN)/index $(LIB)/index.so

mylib:
	gcc -std=c99 -g -shared -fpic $(SRC)/mylib.c -o $(LIB)/mylib.so
	gcc -std=c99 -o $(BIN)/mylib $(LIB)/mylib.so

build: ccdc index mylib

run: ccdc
	$(BIN)/ccdc

debug: ccdc
	gdb $(BIN)/ccdc

clean:
	rm $(LIB)/*
	rm $(BIN)/*

test: ccdc
	python src/python/test.py

notebook: build
	jupyter notebook --notebook-dir="src/python" --no-browser

ipython: build
	cd src/python; \
	ipython

docker: FORCE
	CONTEXT=./docker/lcmap-model-wrapper
	mkdir ./docker/build
	cp ~/.usgs/lcmap.ini ./docker/build
	docker build -t "usgseros/lcmap-model-wrapper" $(CONTEXT)


FORCE:
