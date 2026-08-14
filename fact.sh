#! /bin/bash

# 4! = 1*2*3*4=24

# read -p "Input the number for factorial calculation: " fact

x=1
for i in $(seq 1 $1)
do
	x=$((x*i))
done
echo $x
