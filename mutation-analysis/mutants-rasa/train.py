import os
import re
import random
import subprocess
import argparse
from collections import defaultdict

def sample_mutant_folders(root_dir, N=5, seed=42):
    """
    Traverses the root directory, groups mutant folders by category, 
    and returns a sample of N folders from each category.

    Args:
        root_dir (str): Path to the root directory containing mutant folders.
        N (int): Number of folders to sample per category.

    Returns:
        dict: {category: [sampled_folder_names]}
    """
    random.seed(seed)
    pattern = re.compile(r"mutant_([A-Z0-9]+)_\d+")
    category_map = defaultdict(list)

    for item in os.listdir(root_dir):
        if os.path.isdir(os.path.join(root_dir, item)):
            match = pattern.fullmatch(item)
            if match:
                category = match.group(1)
                category_map[category].append(item)

    # Sample N folders from each category
    sampled = {}
    for category, folders in category_map.items():
        sampled[category] = random.sample(folders, min(N, len(folders)))

    return sampled

def train_sampled_mutants(root_dir, N=5, seed=42):
    """
    Samples folders and trains a Rasa model inside each.

    Args:
        root_dir (str): Root directory with mutant folders.
        N (int): Number of folders to sample per category.
        seed (int): Seed for reproducibility.
    """
    sampled = sample_mutant_folders(root_dir, N, seed)
    train_mutants(root_dir, sampled)


def train_mutants(root_dir, sampled):
    for category, folder_paths in sampled.items():
        print(f"\n== Training category: {category} ==")
        for path in folder_paths:
            print(f"Training in: {path}")
            try:
                cwd = os.path.join(root_dir, path)
                subprocess.run(["rasa", "train"], cwd=cwd, check=True)
            except subprocess.CalledProcessError as e:
                print(f"❌ Failed to train in {path}: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sample and train Rasa models in mutant folders.")
    parser.add_argument("root_dir", help="Path to the root directory containing mutant folders.")
    parser.add_argument("--n", type=int, default=5, help="Number of samples per category.")
    parser.add_argument("--seed", type=int, default=42, help="Random seed for reproducibility.")
    parser.add_argument("--list", type=str, required=False, help="list of mutants.")

    args = parser.parse_args()
    if args.list is not None:
        with open(args.list, 'r') as f:
            file_names = [line.strip() for line in f]

        train_mutants(args.root_dir, {'category': file_names})
    else:
        train_sampled_mutants(args.root_dir, N=args.n, seed=args.seed)
