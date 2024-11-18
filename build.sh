#!/bin/bash

DIR=docs

rm -r $DIR
mdbook build
cp -a static/* $DIR
