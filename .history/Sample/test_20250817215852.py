import csv 
from collections import defaultdict

def load_team_mapping(csv1_path):
    team_mappings = defaultdict(list)
    with open(csv1_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            category = ro