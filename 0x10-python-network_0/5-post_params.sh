#!/bin/bash
# This script sends a post request with data.
curl -sX POST -d "email=test@gmail.com.com&subject=I will always be here for PLD" "$1"
