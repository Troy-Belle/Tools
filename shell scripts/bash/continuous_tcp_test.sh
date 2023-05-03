#!/bin/bash

# prompt the user for the hostname to check
read -p "Enter the hostname to check: " hostname

# prompt the user for the port to check
read -p "Enter the port to check (default is 443): " port
port=${port:-443} # set the default port to 443 if not entered

# prompt the user for the number of iterations
read -p "Enter the number of iterations to perform (default is 100): " num_iterations
num_iterations=${num_iterations:-100} # set the default number of iterations to 100 if not entered

# loop for the specified number of iterations
for ((i=1; i<=$num_iterations; i++))
do
  # use netcat to check the TCP connection
  if nc -z -v -w5 "$hostname" "$port"; then
    echo "Iteration $i: TCP connectivity to $hostname on port $port is successful."
  else
    echo "Iteration $i: TCP connectivity to $hostname on port $port failed."
  fi
done
