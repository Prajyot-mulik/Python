import csv 
from collections import defaultdict

def load_team_mapping(csv1_path):
    team_mappings = defaultdict(list)
    with open(csv1_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            category = row['Skill Category'].split('-')[0]
            technology = row['Technology'].lower()
            team_mappings[technology].append({
                'team_name': row['Skill Category'],
                
            })