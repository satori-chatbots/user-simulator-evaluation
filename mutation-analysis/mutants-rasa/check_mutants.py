import os
import yaml
import argparse
import re

def process_yml(data):
    errors = data.get("errors", [])
    if len(errors) > 0:
        return True
    return False

def process_all_conversation_ymls(root_folder):
    for dirpath, dirnames, filenames in os.walk(root_folder):
        if "conversation_outputs" in dirpath:
            for filename in filenames:
                if filename.endswith(".yml"):
                    file_path = os.path.join(dirpath, filename)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            yml_content = list(yaml.safe_load_all(f))[0]
                            error = process_yml(yml_content)
                            if error:
                                print("Mutant killed")
                                return
                    except Exception as e:
                        print(f"Failed to process {file_path}: {e}")

    print("Mutant survived")

def process_all_mutant_folders(root_folder):
    for dirpath, dirnames, _ in os.walk(root_folder):
        for dirname in dirnames:
            if "mutant_" in dirname.lower():
                full_path = os.path.join(dirpath, dirname)
                print(f"Processing mutant folder: {full_path}")
                process_all_conversation_ymls(full_path)

def extract_mutant_name(folder_name):
    """
    Extracts the name from a pattern like 'mutant_CRE_001'.
    Returns 'CRE' in this case.
    """
    match = re.match(r"mutant_([^_]+)", folder_name)
    if match:
        return match.group(1)
    return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process all .yml files in conversation_outputs folders.")
    parser.add_argument("root_folder", help="The root directory to start the search from.")
    args = parser.parse_args()

    process_all_mutant_folders(args.root_folder)