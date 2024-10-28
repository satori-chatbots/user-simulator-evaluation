#!/bin/bash
set -o xtrace

# Default values
SENSEI_PATH="../user-simulator"
CHATBOT=""
PERSONALITY=""
PERSONALITY_FLAG=""

# Parse command-line options
while getopts ":p:c:n:" opt; do
  case $opt in
    p) SENSEI_PATH="$OPTARG" ;;
    c) CHATBOT="$OPTARG" ;;
    n) PERSONALITY="$OPTARG" ;;
    \?) echo "Invalid option: -$OPTARG" >&2; exit 1 ;;
  esac
done

# Validate CHATBOT input
if [[ "$CHATBOT" != "lola" && "$CHATBOT" != "kuki" && "$CHATBOT" != "saic_malaga" && "$CHATBOT" != "serviceform" && "$CHATBOT" != "financial-bot" && "$CHATBOT" != "ada"  && "$CHATBOT" != "millionbot" && "$CHATBOT" != "catalina" && "$CHATBOT" != "julie" && "$CHATBOT" != "genion" ]]; then
  echo "Invalid chatbot: $CHATBOT. Valid options are: ada, catalina, lola, kuki, millionbot, julie, saic_malaga, serviceform, genion.\nExample: -m saic_malaga"
  exit 1
fi

if [ "$PERSONALITY" = "normal" ]; then
    PERSONALITY_FLAG=""
elif [ "$PERSONALITY" = "direct" ]; then
    PERSONALITY_FLAG="--personality $SENSEI_PATH/personalities/direct-user.yml"
else
    PERSONALITY="normal"
fi

echo "Using personality: $PERSONALITY"
	

if [ "$CHATBOT" = "lola" ]; then
  python3 "$SENSEI_PATH/src/autotest.py" --technology lola --chatbot whatever --user chatbots/lola/conversations --extract output/lola/$PERSONALITY $PERSONALITY_FLAG
elif [ "$CHATBOT" = "ada" ]; then
  python3 "$SENSEI_PATH/src/autotest.py" --technology ada-uam --chatbot whatever --user chatbots/ada/conversations --extract output/ada/$PERSONALITY $PERSONALITY_FLAG
elif [ "$CHATBOT" = "catalina" ]; then
  python3 "$SENSEI_PATH/src/autotest.py" --technology rivas_catalina --chatbot whatever --user chatbots/catalina/conversations --extract output/catalina/$PERSONALITY $PERSONALITY_FLAG
elif [ "$CHATBOT" = "julie" ]; then
  python3 "$SENSEI_PATH/src/autotest.py" --technology julie --chatbot whatever --user chatbots/julie/conversations --extract output/julie/$PERSONALITY $PERSONALITY_FLAG
elif [ "$CHATBOT" = "kuki" ]; then
  python3 "$SENSEI_PATH/src/autotest.py" --technology kuki --chatbot whatever --user chatbots/kuki/conversations --extract output/kuki/$PERSONALITY $PERSONALITY_FLAG
elif [ "$CHATBOT" = "saic_malaga" ]; then
  python3 "$SENSEI_PATH/src/autotest.py" --technology saic_malaga --chatbot whatever --user chatbots/saic_malaga/conversations --extract output/saic_malaga/$PERSONALITY $PERSONALITY_FLAG
elif [ "$CHATBOT" = "serviceform" ]; then
  python3 "$SENSEI_PATH/src/autotest.py" --technology serviceform --chatbot whatever --user chatbots/serviceform/conversations --extract output/serviceform/$PERSONALITY $PERSONALITY_FLAG
elif [ "$CHATBOT" = "millionbot" ]; then
  python3 "$SENSEI_PATH/src/autotest.py" --technology millionbot --chatbot whatever --user chatbots/millie/conversations --extract output/millie/$PERSONALITY $PERSONALITY_FLAG
elif [ "$CHATBOT" = "genion" ]; then
  python3 "$SENSEI_PATH/src/autotest.py" --technology genion --chatbot whatever --user chatbots/genion/conversations --extract output/genion/$PERSONALITY $PERSONALITY_FLAG
elif [ "$CHATBOT" = "financial-bot" ]; then
  python3 "$SENSEI_PATH/src/autotest.py" --technology rasa --chatbot http://0.0.0.0:5005/webhooks/rest/webhook --user chatbots/financial-bot/conversations --extract output/financial-bot/$PERSONALITY $PERSONALITY_FLAG
else
  echo "CHATBOT is set to $CHATBOT. No action taken."
fi
