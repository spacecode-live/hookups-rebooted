#!/bin/sh

# Code Style Tests.
echo "Testing Code style..."

echo "Testing Hookup/ code style..."
out=$(pycodestyle Hookup/)
if [ "$out" == "" ]; then
	echo "Success."
fi

echo "Testing HookupsRebooted/ code style..."
out=$(pycodestyle HookupsRebooted/)
if [ "$out" == "" ]; then
	echo "Success."
fi

# Unit Tests
echo "Running Unit Tests..."
python2 -m unittest discover
