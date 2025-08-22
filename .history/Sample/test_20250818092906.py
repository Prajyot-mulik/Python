import csv
from collections import defaultdict

def load_job_families(csv1_path):
    """Load job families and their associated skills from CSV1"""
    job_families = defaultdict(list)
    with open(csv1_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            skills = [s.strip().lower() for s in row['Comments'].split(',')]
            job_families[row['Job Family']] = skills
    return job_families

def process_employees(csv2_path, job_families):
    """Match employees to job families based on skills"""
    employees_with_teams = []
    
    with open(csv2_path, mode='r') as file:
        reader = csv.DictReader(file)
        for employee in reader:
            employee_skills = [s.strip().lower() for s in employee['Primary Skills'].split(',')]
            matched_families = set()
            
            # Check which job families match the employee's skills
            for family, required_skills in job_families.items():
                # Check if any employee skill matches the job family's required skills
                if any(skill in employee_skills for skill in required_skills):
                    matched_families.add(family)
            
            if matched_families:
                employees_with_teams.append({
                    'Employee Name': employee['Employee Name'],
                    'Skills': employee['Primary Skills'],
                    'Job Family': ' | '.join(matched_families)
                })
    
    return employees_with_teams

def save_results(output_path, data):
    """Save results to a new CSV"""
    with open(output_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Employee Name', 'Skills', 'Job Family'])
        writer.writeheader()
        writer.writerows(data)

# Main execution
if __name__ == "__main__":
    # File paths
    csv1_path = 'job_families.csv'
    csv2_path = 'employee_skills.csv'
    output_path = 'employee_job_family_assignments.csv'
    
    # Process data
    job_families = load_job_families(csv1_path)
    results = process_employees(csv2_path, job_families)
    save_results(output_path, results)
    
    print(f"Results saved to {output_path}")
    print("\nSample assignments:")
    for i, row in enumerate(results[:3], 1):
        print(f"{i}. {row['Employee Name']} -> {row['Job Family']}")