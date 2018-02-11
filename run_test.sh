#!/bin/sh

# Code Style Tests.
echo "Testing Code style..."

echo "Testing matchmaker/ code style..."
out=$(pycodestyle matchmaker/)
if [ "$out" == "" ]; then
	echo "Success."
else
	echo "$out"
fi

echo "Testing HookupsRebooted/ code style..."
out=$(pycodestyle HookupsRebooted/)
if [ "$out" == "" ]; then
	echo "Success."
else
	echo "$out"
fi

# Unit Tests
echo "Running Unit Tests..."
python2 -m unittest discover
