#! /bin/bash

# This is just comment, ignored by bash

# echo Enter the number: 
read -p "Enter the number: " num

# echo Enter additional number:
read -p "Enter additional number:" num2

if [ $num -gt 0 -a $num2 -gt 0 ]

then 
	echo Both number is positive
elif
	[ $num -eq 0 ]
then
	echo $num is zero
else
	echo $num is negative
fi
