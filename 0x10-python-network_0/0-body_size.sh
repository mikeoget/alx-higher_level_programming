#!/bin/bash
# Script to do stuff
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2
