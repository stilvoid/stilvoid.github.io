.PHONY: all

DOCS = ./docs
STATIC = ./static

all:
	@ rm -rf $(DOCS)
	@ bleng
	@ cp -a $(STATIC)/* $(DOCS)
