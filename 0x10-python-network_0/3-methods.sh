#!/bin/bash
# Curl options
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-
