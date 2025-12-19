import os
import json
import shutil
from dotenv import load_dotenv
from profile_extraction import read_project_description, extract_profile, save_profile
from bill_generation import generate_bill, save_bill
from optimization_recommendation import generate_recommendations, save_recommendations, generate_html_report, save_html_report

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
if not API_KEY:
    print("Error: GROQ_API_KEY not found in .env file.")
    exit(1)

PROJECT_DESCRIPTION_FILE = "project_description.txt"
PROJECT_PROFILE_FILE = "output/project_profile.json"
MOCK_BILLING_FILE = "output/mock_billing.json"
RECOMMENDATIONS_FILE = "output/cost_optimization_report.json"
REPORT_FILE = "output/cost_report.html"


def display_menu():
    print("1. Enter a new project description")
    print("2. Run Complete Cost Analysis")
    print("3. View Recommendations")
    print("4. Export Report")
    print("5. Exit")

def enter_project_description():
    print("\nEnter your project description (press Enter twice to finish):")
    lines = []
    empty_count = 0
    
    try:
        while True:
            line = input()
            if line == "":
                empty_count += 1
                if empty_count >= 2:
                    break
            else:
                empty_count = 0
            lines.append(line)
        
        description = "\n".join(lines).strip()
        if not description:
            print("Error: Project description cannot be empty.")
            return False
        
        with open(PROJECT_DESCRIPTION_FILE, "w", encoding="utf-8") as f:
            f.write(description)
        
        directory = "output"
        if os.path.exists(directory):
            shutil.rmtree(directory)
        print(f"Project description saved.")
        return True
    except Exception as e:
        print(f"Error: {str(e)}")
        return False


def run_cost_analysis():
    print("\nRunning Cost Analysis...")
    
    project_description = read_project_description(PROJECT_DESCRIPTION_FILE)
    if not project_description:
        print("Error: project_description.txt not found. Use option 1 first.")
        return False
    
    print("Extracting profile...")
    profile, error = extract_profile(project_description)
    if not profile:
        print(f"Error occured at Profile Extraction phase: {error}")
        return False
    save_profile(profile)
    
    print("Generating billing...")
    bill, error = generate_bill(profile)
    if not bill:
        print(f"Error occured at Bill Generation phase: {error}")
        return False
    save_bill(bill)
    
    print("Generating recommendations...")
    recommendations, error = generate_recommendations(profile, bill)
    if not recommendations:
        print(f"Error occured at Recommendation Generation phase: {error}")
        return False
    save_recommendations(recommendations)
    
    print("Cost Analysis Completed!")
    return True


def view_recommendations():
    try:
        if not os.path.exists(RECOMMENDATIONS_FILE):
            print("Error: No analysis found. Run option 2 first.")
            return False
        
        with open(RECOMMENDATIONS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        if "analysis" in data:
            a = data["analysis"]
            print(f"\nCost: ₹{a.get('total_monthly_cost', 'N/A')} | Budget: ₹{a.get('budget', 'N/A')} | Over: {'Yes' if a.get('is_over_budget') else 'No'}")
        
        if "recommendations" in data:
            print("\nRecommendations:")
            for i, rec in enumerate(data["recommendations"], 1):
                print(f"  {i}. {rec.get('title', 'N/A')} - Savings: ₹{rec.get('potential_savings', 'N/A')}")
        
        if "summary" in data:
            s = data["summary"]
            print(f"\nTotal Savings: ₹{s.get('total_potential_savings', 'N/A')} ({s.get('savings_percentage', 'N/A')}%)")
        
        return True
    except Exception as e:
        print(f"Error: {str(e)}")
        return False


def export_report():
    print("\nGenerating HTML Report...")
    
    try:
        if not os.path.exists(PROJECT_PROFILE_FILE):
            print("Error: project_profile.json not found. Run option 2 first.")
            return False
        if not os.path.exists(MOCK_BILLING_FILE):
            print("Error: mock_billing.json not found. Run option 2 first.")
            return False
        if not os.path.exists(RECOMMENDATIONS_FILE):
            print("Error: cost_optimization_report.json not found. Run option 2 first.")
            return False
        
        with open(PROJECT_PROFILE_FILE, "r", encoding="utf-8") as f:
            profile = f.read()
        with open(MOCK_BILLING_FILE, "r", encoding="utf-8") as f:
            billing = f.read()
        with open(RECOMMENDATIONS_FILE, "r", encoding="utf-8") as f:
            recommendations = f.read()
        
        html_report, error = generate_html_report(profile, billing, recommendations)
        if not html_report:
            print(f"Error generating report: {error}")
            return False
        
        success, error = save_html_report(html_report)
        if not success:
            print(f"Error saving report: {error}")
            return False
        
        print(f"Report exported to {REPORT_FILE}")
        
        open_report = input("Open report in browser? (y/n): ").strip().lower()
        if open_report == 'y':
            import webbrowser
            webbrowser.open(f"file://{os.path.abspath(REPORT_FILE)}")
        
        return True
    except Exception as e:
        print(f"Error: {str(e)}")
        return False

def main():
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            enter_project_description()
        elif choice == "2":
            run_cost_analysis()
        elif choice == "3":
            view_recommendations()
        elif choice == "4":
            export_report()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Enter 1-5.")

if __name__ == "__main__":
    main()