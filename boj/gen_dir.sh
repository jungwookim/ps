#!/bin/sh

prob_num=$1

if [ -z "$prob_num" ]
  then
    echo "Problem's number is needed"
    exit 1
fi

if [ -d "$prob_num" ]
  then
    echo "already exist file"
    exit
fi

mkdir $prob_num
touch ./$prob_num/a.py ./$prob_num/input.txt

echo The No.$prob_num Problem is generated.