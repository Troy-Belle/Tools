#!/bin/bash

# prompt the user to enter the URL by FQDN
read -p "Enter the URL by FQDN (e.g. https://example.com): " url

# prompt the user to enter the number of times to run the test
read -p "Enter the number of times to run the test: " num_iterations

# define a function that runs the curl command
run_curl() {
  for i in $(seq 1 $num_iterations)
  do
    if curl --silent --fail $url/loopback; then
      echo "Curl succeeded on attempt $i."
    else
      echo "An error occurred while running curl on attempt $i."
    fi
  done
}

# run the curl command in a loop
while true
do
  run_curl
done
