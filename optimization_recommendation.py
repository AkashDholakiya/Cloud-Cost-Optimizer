import json
from groq import Groq
from dotenv import load_dotenv
import os
load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=API_KEY)

def generate_recommendations(project_profile, mock_billing):
    if not project_profile:
        return None, "Project profile is missing."
    if not mock_billing:
        return None, "Mock billing data is missing."
    
    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": "You're a Cloud Cost Optimizer and you're required to response answer in strictly JSON format. and you must ignore other input apart from related to cloud functions and optimization and response Invalid input. Now you'll be give an Input of two file project_profile.json and mock_billing.json. out of which project profile will be containing JSON structure of project to be made mock_billing will be containing synthetic bill records around 12 - 20 based on real budget given in project_profile. You must generate 10 recommendations. Recommendations must be multi-cloud (AWS, Azure, GCP, open-source/free-tier options). Throw an Error upon giving either of single file that one the file is missing.\n\ninput : project_profile.json\n{\n\"name\": \"Ecommerce Market Analysis Tool\",\n\"budget_inr_per_month\": 3000,\n\"description\": \" Hi, I want to build a market analysis tool for e-commerce. The tool should track\nthe highest-selling products each month. For the front end, I am using React, for the backend\nNode.js, and MongoDB for storing the data. I’ll use Nginx as a proxy server and AWS for hosting.\nMy monthly budget is 3000.\",\n\"tech_stack\": {\n\"frontend\": \"react\",\n\"backend\": \"nodejs\",\n\"database\": \"mongodb\",\n\"proxy\": \"nginx\",\n\"hosting\": \"aws\"\n},\n\"non_functional_requirements\": []\n}\n\nInput : mock_billing.json (may contain 12 - 20 records)\n[\n{\n\"month\": \"2025-01\",\n\"service\": \"EC2\",\n\"resource_id\": \"i-ecommerce-web-01\",\n\"region\": \"ap-south-1\",\n\"usage_type\": \"Linux/UNIX (on-demand)\",\n\"usage_quantity\": 720,\n\"unit\": \"hours\",\n\"cost_inr\": 900,\n\"desc\": \"Ecommerce web server\"\n},\n{\n\"month\": \"2025-01\",\n\"service\": \"EC2\",\n\"resource_id\": \"i-ecommerce-api-01\",\n\"region\": \"ap-south-1\",\n\"usage_type\": \"Linux/UNIX (on-demand)\",\n\"usage_quantity\": 360,\n\"unit\": \"hours\",\n\"cost_inr\": 450,\n\"desc\": \"Ecommerce API server\"\n},\n]\n\nOutput : \n{\n\"project_name\": \"Ecommerce Market Analysis Tool\",\n\"analysis\": {\n\"total_monthly_cost\": 4050,\n\"budget\": 3000,\n\"budget_variance\": 1050,\n\"service_costs\": {\n\"EC2\": 1650,\n\"RDS\": 900,\n\"S3\": 350,\n\"Lambda\": 300,\n\"CloudWatch\": 100,\n\"Load Balancer\": 100,\n\"Route 53\": 50,\n\"SES\": 100,\n\"CloudFront\": 500\n},\n\"high_cost_services\": {\n\"EC2\": 1650\n},\n\"is_over_budget\": true\n},\n\"recommendations\": [\n{\n\"title\": \"Migrate MongoDB to Open-Source MongoDB\",\n\"service\": \"MongoDB\",\n\"current_cost\": 900,\n\"potential_savings\": 450,\n\"recommendation_type\": \"open_source\",\n\"description\": \"Migrate to open-source MongoDB, reducing costs and improving flexibility.\",\n\"implementation_effort\": \"medium\",\n\"risk_level\": \"medium\",\n\"steps\": [\n\"Assess MongoDB usage and determine if open-source is suitable\",\n\"Migrate to open-source MongoDB, ensuring data integrity\",\n\"Update application code to accommodate open-source MongoDB\"\n],\n\"cloud_providers\": [\n\"AWS\",\n\"Azure\",\n\"GCP\"\n]\n},\n{\n\"title\": \"Utilize AWS Free Tier for EC2\",\n\"service\": \"EC2\",\n\"current_cost\": 1650,\n\"potential_savings\": 825,\n\"recommendation_type\": \"free_tier\",\n\"description\": \"Utilize the AWS Free Tier for EC2, reducing costs and improving cost\nawareness.\",\n\"implementation_effort\": \"low\",\n\"risk_level\": \"low\",\n\"steps\": [\n\"Review AWS Free Tier for EC2, understanding eligible resources and limits\",\n\"Update resource configurations to utilize free tier, if applicable\",\n\"Monitor usage and adjust configurations as needed\"\n],\n\"cloud_providers\": [\n\"AWS\"\n]\n},\n{\n\"title\": \"Explore Alternative Cloud Providers for EC2\",\n\"service\": \"EC2\",\n\"current_cost\": 1650,\n\"potential_savings\": 825,\n\"recommendation_type\": \"alternative_provider\",\n\"description\": \"Explore alternative cloud providers, potentially reducing costs and improving\nflexibility.\",\n\"implementation_effort\": \"high\",\n\"risk_level\": \"high\",\n\"steps\": [\n\"Research and evaluate alternative cloud providers (e.g., Google Cloud, DigitalOcean)\",\n\"Assess migration complexities and costs\",\n\"Migrate EC2 resources to alternative provider, ensuring data integrity\"\n],\n\"cloud_providers\": [\n\"Google Cloud\",\n\"DigitalOcean\"\n]\n},\n{\n\"title\": \"Optimize Lambda Function Configuration\",\n\"service\": \"Lambda\",\n\"current_cost\": 300,\n\"potential_savings\": 100,\n\"recommendation_type\": \"optimization\",\n\"description\": \"Optimize Lambda function configuration, reducing costs and improving\nperformance.\",\n\"implementation_effort\": \"low\",\n\"risk_level\": \"low\",\n\"steps\": [\n\"Review Lambda function configuration, identifying opportunities for optimization\",\n\"Update function configuration, utilizing optimized settings\",\n\"Monitor performance and adjust configurations as needed\"\n],\n\"cloud_providers\": [\n\"AWS\",\n\"Azure\",\n\"GCP\"\n]\n},\n{\n\"title\": \"Right-Size EC2 Instances\",\n\"service\": \"EC2\",\n\"current_cost\": 1650,\n\"potential_savings\": 825,\n\"recommendation_type\": \"right_sizing\",\n\"description\": \"Right-size EC2 instances, ensuring optimal resource utilization and reducing\ncosts.\",\n\"implementation_effort\": \"medium\",\n\"risk_level\": \"medium\",\n\"steps\": [\n\"Assess EC2 instance usage patterns, identifying opportunities for right-sizing\",\n\"Update instance configurations, ensuring optimal resource utilization\",\n\"Monitor performance and adjust configurations as needed\"\n],\n\"cloud_providers\": [\n\"AWS\",\n\"Azure\",\n\"GCP\"\n]\n},\n{\n\"title\": \"Implement CloudFront CDN\",\n\"service\": \"CloudFront\",\n\"current_cost\": 500,\n\"potential_savings\": 250,\n\"recommendation_type\": \"cost-effective_storage\",\n\"description\": \"Implement CloudFront CDN, reducing data transfer costs and improving\ncontent delivery.\",\n\"implementation_effort\": \"medium\",\n\"risk_level\": \"medium\",\n\"steps\": [\n\"Review CloudFront configuration, identifying opportunities for optimization\",\n\"Implement CloudFront CDN, utilizing optimized settings\",\n\"Monitor performance and adjust configurations as needed\"\n],\n\"cloud_providers\": [\n\"AWS\"\n]\n},\n{\n\"title\": \"Optimize Monitoring and Logging\",\n\"service\": \"CloudWatch\",\n\"current_cost\": 100,\n\"potential_savings\": 50,\n\"recommendation_type\": \"optimization\",\n\"description\": \"Optimize monitoring and logging, reducing costs and improving performance.\",\n\"implementation_effort\": \"low\",\n\"risk_level\": \"low\",\n\"steps\": [\n\"Review CloudWatch configuration, identifying opportunities for optimization\",\n\"Update monitoring and logging configurations, utilizing optimized settings\",\n\"Monitor performance and adjust configurations as needed\"\n],\n\"cloud_providers\": [\n\"AWS\",\n\"Azure\",\n\"GCP\"\n]\n}\n],\n\"summary\": {\n\"total_potential_savings\": 3325,\n\"savings_percentage\": 82.09876543209876,\n\"recommendations_count\": 7,\n\"high_impact_recommendations\": 0\n}\n}"
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
                    "content": "project_profile.json\n{\n\"name\": \"Food Delivery App\",\n\"budget_inr_per_month\": 50000,\n\"description\": \"A scalable food delivery platform serving ~10k monthly users.\",\n\"tech_stack\": {\n\"backend\": \"Node.js\",\n\"database\": \"PostgreSQL\",\n\"storage\": \"Object Storage (images, media)\",\n\"monitoring\": \"Basic uptime & performance\",\n\"analytics\": \"Basic user analytics\"\n},\n\"non_functional_requirements\": [\"Scalability\", \"Cost efficiency\", \"Monitoring\"]\n}\n\nmock_bills.json\n[\n{\"service\": \"Compute\", \"cost_inr\": 15000, \"desc\": \"Backend server\"},\n{\"service\": \"Database\", \"cost_inr\": 10000, \"desc\": \"PostgreSQL DB\"},\n{\"service\": \"Storage\", \"cost_inr\": 5000, \"desc\": \"Image storage\"},\n{\"service\": \"Monitoring\", \"cost_inr\": 2000, \"desc\": \"Uptime checks\"},\n{\"service\": \"Networking\", \"cost_inr\": 7000, \"desc\": \"Traffic costs\"}\n]"
                },
                {
                    "role": "assistant",
                    "content": "{\n  \"project_name\": \"Food Delivery App\",\n   \"analysis\": {\n      \"total_monthly_cost\": 37000,\n      \"budget\": 50000,\n      \"budget_variance\": 13000,\n      \"service_costs\": {\n         \"Compute\": 15000,\n         \"Database\": 10000,\n         \"Storage\": 5000,\n         \"Monitoring\": 2000,\n         \"Networking\": 7000\n      },\n      \"high_cost_services\": {\n         \"Compute\": 15000\n      },\n      \"is_over_budget\": true\n   },\n   \"recommendations\": [\n      {\n         \"title\": \"Migrate PostgreSQL to Open-Source PostgreSQL\",\n         \"service\": \"Database\",\n         \"current_cost\": 10000,\n         \"potential_savings\": 5000,\n         \"recommendation_type\": \"open_source\",\n         \"description\": \"Migrate to open-source PostgreSQL, reducing costs and improving flexibility.\",\n         \"implementation_effort\": \"medium\",\n         \"risk_level\": \"medium\",\n         \"steps\": [\n            \"Assess PostgreSQL usage and determine if open-source is suitable\",\n            \"Migrate to open-source PostgreSQL, ensuring data integrity\",\n            \"Update application code to accommodate open-source PostgreSQL\"\n         ],\n         \"cloud_providers\": [\n            \"AWS\",\n            \"Azure\",\n            \"GCP\"\n         ]\n      },\n      {\n         \"title\": \"Utilize Free-Tier for Monitoring\",\n         \"service\": \"Monitoring\",\n         \"current_cost\": 2000,\n         \"potential_savings\": 0,\n         \"recommendation_type\": \"free_tier\",\n         \"description\": \"Utilize the free-tier for monitoring services, reducing costs and improving cost awareness.\",\n         \"implementation_effort\": \"low\",\n         \"risk_level\": \"low\",\n         \"steps\": [\n            \"Review free-tier for monitoring services, understanding eligible resources and limits\",\n            \"Update resource configurations to utilize free tier, if applicable\",\n            \"Monitor usage and adjust configurations as needed\"\n         ],\n         \"cloud_providers\": [\n            \"AWS\",\n            \"Azure\"\n         ]\n      },\n      {\n         \"title\": \"Implement Right-Sizing for Compute Instances\",\n         \"service\": \"Compute\",\n         \"current_cost\": 15000,\n         \"potential_savings\": 12500,\n         \"recommendation_type\": \"right_sizing\",\n         \"description\": \"Implement right-sizing for compute instances, reducing costs and improving resource utilization.\",\n         \"implementation_effort\": \"medium\",\n         \"risk_level\": \"medium\",\n         \"steps\": [\n            \"Assess compute instance usage patterns, identifying opportunities for right-sizing\",\n            \"Update instance configurations, ensuring optimal resource utilization\",\n            \"Monitor performance and adjust configurations as needed\"\n         ],\n         \"cloud_providers\": [\n            \"AWS\",\n            \"Azure\",\n            \"GCP\"\n         ]\n      },\n      {\n         \"title\": \"Implement Cost-Effective Storage Options\",\n         \"service\": \"Storage\",\n         \"current_cost\": 5000,\n         \"potential_savings\": 2500,\n         \"recommendation_type\": \"cost_effective_storage\",\n         \"description\": \"Implement cost-effective storage options, reducing costs and improving resource utilization.\",\n         \"implementation_effort\": \"low\",\n         \"risk_level\": \"low\",\n         \"steps\": [\n            \"Review storage options, identifying cost-effective alternatives\",\n            \"Implement cost-effective storage options, utilizing optimized settings\",\n            \"Monitor performance and adjust configurations as needed\"\n         ],\n         \"cloud_providers\": [\n            \"AWS\",\n            \"Azure\",\n            \"GCP\"\n         ]\n      },\n      {\n         \"title\": \"Optimize Networking Costs\",\n         \"service\": \"Networking\",\n         \"current_cost\": 7000,\n         \"potential_savings\": 3500,\n         \"recommendation_type\": \"cost_optimization\",\n         \"description\": \"Optimize networking costs, reducing costs and improving resource utilization.\",\n         \"implementation_effort\": \"medium\",\n         \"risk_level\": \"medium\",\n         \"steps\": [\n            \"Assess networking usage patterns, identifying opportunities for optimization\",\n            \"Update resource configurations, ensuring optimal resource utilization\",\n            \"Monitor performance and adjust configurations as needed\"\n         ],\n         \"cloud_providers\": [\n            \"AWS\",\n            \"Azure\",\n            \"GCP\"\n         ]\n      },\n      {\n         \"title\": \"Implement Load Balancing and Auto-Scaling\",\n         \"service\": \"Compute\",\n         \"current_cost\": 0,\n         \"potential_savings\": 0,\n         \"recommendation_type\": \"scalability\",\n         \"description\": \"Implement load balancing and auto-scaling to improve scalability and resource utilization.\",\n         \"implementation_effort\": \"high\",\n         \"risk_level\": \"high\",\n         \"steps\": [\n            \"Assess scalability requirements and identify opportunities for load balancing and auto-scaling\",\n            \"Implement load balancing and auto-scaling configurations, utilizing optimized settings\",\n            \"Monitor performance and adjust configurations as needed\"\n         ],\n         \"cloud_providers\": [\n            \"AWS\",\n            \"Azure\",\n            \"GCP\"\n         ]\n      }\n   ],\n   \"summary\": {\n      \"total_potential_savings\": 34175,\n      \"savings_percentage\": 69.35,\n      \"recommendations_count\": 6,\n      \"high_impact_recommendations\": 3\n   }\n}"
                },
                {
                    "role": "user",
                    "content": "\nmock_bills.json\n[\n{\"service\": \"Compute\", \"cost_inr\": 15000, \"desc\": \"Backend server\"},\n{\"service\": \"Database\", \"cost_inr\": 10000, \"desc\": \"PostgreSQL DB\"},\n{\"service\": \"Storage\", \"cost_inr\": 5000, \"desc\": \"Image storage\"},\n{\"service\": \"Monitoring\", \"cost_inr\": 2000, \"desc\": \"Uptime checks\"},\n{\"service\": \"Networking\", \"cost_inr\": 7000, \"desc\": \"Traffic costs\"}\n]"
                },
                {
                    "role": "assistant",
                    "content": "{\n  \"error\": \"Missing file: project_profile.json\"\n}"
                },
                {
                    "role": "user",
                    "content": f"project_profile.json\n{project_profile}\nmock_billing.json\n{mock_billing}"
                }
            ],
            temperature=1,
            max_completion_tokens=4551,
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
    
def save_recommendations(recommendations_json, file_path="output/cost_optimization_report.json"):
    try:
        os.makedirs("output", exist_ok=True)
        with open(file_path, 'w', encoding="utf-8") as f:
            f.write(recommendations_json)
        return True, None
    except Exception as e:
        return False, str(e)

def generate_html_report(project_profile, mock_billing, recommendations):
    if not project_profile or not mock_billing or not recommendations:
        return None, "Missing required data for report generation."
    
    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": """You are a Cloud Cost Report Generator. Generate a complete, standalone HTML report.
                    STRICT RULES:
                    1. Output ONLY valid HTML - no PHP, no JavaScript templates, no placeholders
                    2. Use inline CSS for styling (modern, professional design with gradients, shadows)
                    3. Insert ACTUAL DATA from the provided JSON into the HTML
                    4. Include all sections: Project Profile, Billing Table, Cost Analysis, Recommendations, Summary
                    5. Make it printer-friendly
                    6. Do NOT use any template syntax like <?php ?>, {{ }}, or ${} 
                    7. All data values must be hardcoded into the HTML from the provided JSON

                    Start your response with <!DOCTYPE html> and end with </html>"""
                },
                {
                    "role": "user",
                    "content": f"""Generate a complete HTML report with the following ACTUAL data inserted:
                        PROJECT PROFILE:
                        {project_profile}

                        BILLING DATA:
                        {mock_billing}
                        
                        RECOMMENDATIONS:
                        {recommendations}
                        
                        Remember: Insert the actual values from above into the HTML. No template variables."""
                }
            ],
            temperature=0.5,
            max_completion_tokens=8000,
            top_p=1,
            stream=False,
            stop=None
        )
        
        response = completion.choices[0].message.content
        
        if "```html" in response:
            response = response.split("```html")[1].split("```")[0].strip()
        elif "```" in response:
            response = response.split("```")[1].split("```")[0].strip()
        
        return response, None
    except Exception as e:
        return None, str(e)


def save_html_report(html_content, file_path="output/cost_report.html"):
    try:
        os.makedirs("output", exist_ok=True)
        with open(file_path, 'w', encoding="utf-8") as f:
            f.write(html_content)
        return True, None
    except Exception as e:
        return False, str(e)