#!/bin/bash
set -o xtrace

# Default values
SENSEI_PATH="../user-simulator"
EVALUATION_PATH=`pwd`
CHATBOT=""

cd $SENSEI_PATH

CHATBOTS="ada catalina julie kuki lola millie saic_malaga serviceform"

export PYTHONPATH=$SENSEI_PATH

# Parse command-line options
while getopts ":p:c:n:" opt; do
  case $opt in
    p) SENSEI_PATH="$OPTARG" ;;
    c) CHATBOT="$OPTARG" ;;
    \?) echo "Invalid option: -$OPTARG" >&2; exit 1 ;;
  esac
done

for name in $CHATBOTS; do
    if [[ -z "$CHATBOT" || "$nombre" == "$CHATBOT" ]]; then
      python3 src/metamorphic_tester.py \
              --rules $EVALUATION_PATH/chatbots/$name/rules \
              --conversations $EVALUATION_PATH/output/$name/ \
              --dump $EVALUATION_PATH/output/$name/"$name"_test_results.csv

      # If the result is not 0, exit the script
      if [ $? -ne 0 ]; then
        echo "Error running the tests for $name"
        #exit 1
      fi
    fi
done
