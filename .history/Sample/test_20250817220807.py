import csv
from collections import defaultdict

def load_team_mappings(csv1_path):
    """Load skill to team mappings from CSV1"""
    team_mappings = defaultdict(list)
    with open(csv1_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            category = row['Skill Category'].split(' - ')[0]
            technology = row['Technology'].lower()
            team_mappings[technology].append({
                'team_name': row['Skill Category'],
                'provider': row['Providers']
            })
    return team_mappings

def process_employees(csv2_path, team_mappings):
    """Process employees and assign teams based on skills"""
    employees_with_teams = []
    
    with open(csv2_path, mode='r') as file:
        reader = csv.DictReader(file)
        for employee in reader:
            skills = [s.strip().lower() for s in employee['Primary Skills'].split(',')]
            assigned_teams = set()
            
            for skill in skills:
                if skill in team_mappings:
                    for mapping in team_mappings[skill]:
                        team_info = f"{mapping['team_name']} ({mapping['provider']})"
                        assigned_teams.add(team_info)
            
            if assigned_teams:
                employees_with_teams.append({
                    'Employee Name': employee['Employee Name'],
                    'Skills': employee['Primary Skills'],
                    'Teams': ' | '.join(assigned_teams)
                })
    
    return employees_with_teams

def save_results(output_path, data):
    """Save results to new CSV"""
    with open(output_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Employee Name', 'Skills', 'Teams'])
        writer.writeheader()
        writer.writerows(data)

# Main execution
if __name__ == "__main__":
    # File paths
    csv1_path = 'skills_to_teams.csv'
    csv2_path = 'employee_skills.csv'
    output_path = 'employee_team_assignments.csv'
    
    # Process the data
    team_mappings = load_team_mappings(csv1_path)
    results = process_employees(csv2_path, team_mappings)
    save_results(output_path, results)
    
    print(f"Processing complete. Results saved to {output_path}")
    print("\nSample results:")
    for i, row in enumerate(results[:3], 1):
        print(f"{i}. {row['Employee Name']} -> {row['Teams']}")