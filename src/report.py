import sys
import os
import argparse
import pandas as pd

chatbots = {
    "ada": {
        "name": 'Ada',
        "test_results": 'ada_test_results.csv',
    },
    "catalina": {
        "name": 'Catalina',
        "test_results": 'catalina_test_results.csv',
    },
    # financial-bot
    "kuki": {
        "name": 'Kuki',
        "test_results": 'kuki_test_results.csv',
    },
    "lola": {
        "name": 'Lola',
        "test_results": 'lola_test_results.csv',
    },
    "millie": {
        "name": 'Millie',
        "test_results": 'millie_test_results.csv',
    },
    "saic_malaga": {
        "name": 'SAIC',
        "test_results": 'saic_malaga_test_results.csv',
    },

    #"generic": {
    #    "name": 'Generic',
    #    "test_results": 'result.csv',
    #}

}

def chatbot_report_name(filename):
    for k, c in chatbots.items():
        if c["test_results"] == filename:
            return c["name"]

def generate(main_folder):
    # Get all CSV files from main_folder, recursively
    df = None
    for root, _, files in os.walk(main_folder):
        for file in files:
            chatbot_name = chatbot_report_name(file)
            if file.endswith('.csv') and chatbot_name is not None:
                current = pd.read_csv(os.path.join(root, file))
                # Add a first column with the chatbot name
                current.insert(0, 'chatbot', chatbot_name)
                if df is None:
                    df = current
                else:
                    df = pd.concat([df, current])

    print(df)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Report results')
    parser.add_argument('main_folder', type=str, help='Folder with error files')
    args = parser.parse_args()

    generate(args.main_folder)