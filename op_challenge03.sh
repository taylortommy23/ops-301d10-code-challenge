#!/bin/bash


# input directory path
read -p "Enter directory path: " dir_path

# input permission number
read -p "Enter permission number: " permission_num

cd "$dir_path"

# Change all file inside
chmod _R "$permission_num" *
# print directory list
ls -l
