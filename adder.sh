#! /bin/bash

if [ $# -ne 2 ]
then echo "Usage is ./adder.sh <param1> <param2>"
	exit 1
fi

if [[ "$1" =~ ^-?[0-9]+$ ]] && [[ "$2" =~ ^-?[0-9]+$ ]]
then

let num=$1+$2
echo $num

else echo Only numbers are valid in this script
	exit 1
fi
