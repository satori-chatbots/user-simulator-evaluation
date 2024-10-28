import argparse
# Dynamically load ../user-simulator/src
import os
import sys
sys.path.append(os.path.abspath('../user-simulator/src'))

import metamorphic_tester as mt

def times(folder):
    total_tests = 0
    ours_total = 0
    ours_interactions = 0
    avg_times = []

    tests = mt.get_tests_from_yaml_files(folder)
    for t in tests:
        if "direct-user" in t.file_name:
            continue

        print(t.file_name)
        if len(t.assistant_times) > 0:
            total_tests = total_tests + 1

            total_assistant = sum(t.assistant_times)

            ours_total += t.conversation_time - total_assistant
            ours_interactions += len(t.interaction) - len(t.assistant_times)
            avg_times.append((t.conversation_time - total_assistant) / (len(t.interaction) - len(t.assistant_times)))

    print("Average time per conversation (our): ", ours_total / total_tests)
    #print("Average time per interaction  (our): ", (ours_total / ours_interactions) / total_tests)
    print("Average time per interaction  (our): ", sum(avg_times) / len(avg_times))


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Report results')
    parser.add_argument('main_folder', type=str, help='Folder with error files')
    args = parser.parse_args()

    df = times(args.main_folder)

