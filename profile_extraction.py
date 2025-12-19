import json
from groq import Groq
from dotenv import load_dotenv
import os
load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=API_KEY)

def read_project_description(file_path="project_description.txt"):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return None

def extract_profile(project_description):
    if not project_description:
        return None, "Project description is empty."
        
    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": "You're a Cloud Cost Optimizer and you're required to response answer in strictly JSON format. and you must ignore other input apart from related to cloud functions and optimization and response Invalid input. Now you'll be given an Input of Project Description in Plain Text format and you're supposed to return Project profile in JSON format as shown below.\n\nInput :\nWe are building a food delivery app for 10,000 users per month.\nBudget: ₹50,000 per month.\nTech stack: Node.js backend, PostgreSQL database, object storage for images, monitoring, and\nbasic analytics.\nNon-functional requirements: scalability, cost efficiency, uptime monitoring.\n\nOutput:\n{\n\"name\": \"Food Delivery App\",\n\"budget_inr_per_month\": 50000,\n\"description\": \"A scalable food delivery platform serving ~10k monthly users.\",\n\"tech_stack\": {\n\"backend\": \"Node.js\",\n\"database\": \"PostgreSQL\",\n\"storage\": \"Object Storage (images, media)\",\n\"monitoring\": \"Basic uptime & performance\",\n\"analytics\": \"Basic user analytics\"\n},\n\"non_functional_requirements\": [\"Scalability\", \"Cost efficiency\", \"Monitoring\"]\n}"
                },
                {
                    "role": "user",
                    "content": "hello world"
                },
                {
                    "role": "assistant",
                    "content": "{\n  \"error\": \"Invalid input\"\n}"
                },
                {
                    "role": "user",
                    "content": "We are building a Electronic Device Vendor app for 50,000 users per month.\nand the budget is about 1,50,000 Rs. Decided Tech Stack is Node.js backend, PostgreSQL database, object storage for images, monitoring, and basic analytics. Non-functional requirements are scalability, cost efficiency, uptime monitoring."
                },
                {
                    "role": "assistant",
                    "content": "{\n  \"name\": \"Electronic Device Vendor App\",\n   \"budget_inr_per_month\": 150000,\n   \"description\": \"A scalable platform serving ~50k electronics shoppers per month.\",\n   \"tech_stack\": {\n      \"backend\": \"Node.js\",\n      \"database\": \"PostgreSQL\",\n      \"storage\": \"Object Storage (images, media)\",\n      \"monitoring\": \"Basic uptime & performance\",\n      \"analytics\": \"Basic user analytics\"\n   },\n   \"non_functional_requirements\": [\n      \"Scalability\",\n      \"Cost efficiency\",\n      \"Monitoring\",\n      \"Uptime Monitoring\"\n   ]\n}"
                },
                {
                    "role": "user",
                    "content": project_description
                }
            ],
            temperature=1,
            max_completion_tokens=2161,
            top_p=1,
            stream=False,
            response_format={"type": "json_object"},
            stop=None
        )
        
        response = completion.choices[0].message.content
        
        try:
            data = json.loads(response)
            if "error" in data:
                return None, data["error"]
        except json.JSONDecodeError:
            return None, "Invalid JSON response from API."

        return response, None
    except Exception as e:
        return None, str(e)

def save_profile(profile_json, file_path="output/project_profile.json"):
    try:
        os.makedirs("output", exist_ok=True)
        with open(file_path, 'w', encoding="utf-8") as f:
            f.write(profile_json)
        return True, None
    except Exception as e:
        return False, str(e)