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
    #"genion": {
    #    "name": 'Genion-2',
    #    "test_results": 'genion_test_results.csv',
    #},
    "financial-bot": {
        "name": 'FinancialBot',
        "test_results": 'financial-bot_test_results.csv',
    },
    "julie": {
        "name": 'Julie',
        "test_results": 'julie_test_results.csv',
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
    "serviceform": {
        "name": 'ServiceForm',
        "test_results": 'serviceform_test_results.csv',
    }

    #"generic": {
    #    "name": 'Generic',
    #    "test_results": 'result.csv',
    #}

}

rule_mapping = {
    "goal_not_completed": "G",
    "no_response": "C",
    "timeout": "T",
    "exceeded_loop_limit": "L",
    "chatbot_fills_all_slots": "GR1", ## NOT SURE
    "chatbot_does_not_repeat": "GR2",
    "non_empty_links": "GR4",
    "chatbot_responds_in_same_language": "GR3",

    "only_talks_about": "OutOfScope",
    "general_multiplication": "Mul",
    "geography": "Geo",
    "adding": "Add",
    "substraction": "Sub",
    "division": "Div",
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

    return df

def one_table(df):
    print(df)
    df["rule"] = df["rule"].map(rule_mapping)
    if df["rule"].isna().any():
        print(df)
        raise ValueError("The 'rule' column contains NaN values after mapping.")

    df["num_conversations"] = df.groupby("chatbot")["checks"].transform("first")

    #df["num_"]
    print(df)

    df_filtered = df[df["fail"] > 0]

    def unique_comma_join(values):
        return ", ".join(sorted(set(values)))

    df_aggregated = df_filtered.groupby("chatbot").agg({
        "num_conversations": "first",
        "checks": "sum",
        #"pass": "sum",
        "fail": "sum",
        "rule": unique_comma_join,

        #"not_applicable": "sum"
    }).reset_index()

    # Rename column rule to "failed rules"

    df_aggregated = df_aggregated.rename(columns={"chatbot": "Chatbot"})
    df_aggregated = df_aggregated.rename(columns={"num_conversations": "\#Conversations"})
    df_aggregated = df_aggregated.rename(columns={"checks": "\#Checks"})
    df_aggregated = df_aggregated.rename(columns={"fail": "\#Failures"})
    df_aggregated = df_aggregated.rename(columns={"rule": "Failing rules"})

    print(df_aggregated)

    print("\n\n")

    # Convert to latex
    print(df_aggregated.to_latex(index=False))

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Report results')
    parser.add_argument('main_folder', type=str, help='Folder with error files')
    args = parser.parse_args()

    df = generate(args.main_folder)
    one_table(df)
