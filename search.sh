#! /bin/bash

read -p "Enter the file name for search: " file

if [[ -e $file ]]
then
	echo The file $file exists
else
	echo No such file
fi
