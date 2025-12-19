import json
from groq import Groq
from dotenv import load_dotenv
import os
load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=API_KEY)

def generate_bill(project_profile):
    if not project_profile:
        return None, "Project profile is empty."
    
    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": "You're a Cloud Cost Optimizer and you're required to response answer in strictly JSON format. and you must ignore other input apart from related to cloud functions and optimization and response Invalid input. Now you'll be given an Input of Project Profile in JSON format and you're supposed to return realistic budget-aware synthetic cloud billing (12 - 20 realistic records) in JSON format as shown below. Records include: month, service, usage_quantity, unit, cost_inr, region, etc.\n\nInput :\n{\n\"name\": \"Ecommerce Market Analysis Tool\",\n\"budget_inr_per_month\": 3000,\n\"description\": \" Hi, I want to build a market analysis tool for e-commerce. The tool should track\nthe highest-selling products each month. For the front end, I am using React, for the backend\nNode.js, and MongoDB for storing the data. I’ll use Nginx as a proxy server and AWS for hosting.\nMy monthly budget is 3000.\",\n\"tech_stack\": {\n\"frontend\": \"react\",\n\"backend\": \"nodejs\",\n\"database\": \"mongodb\",\n\"proxy\": \"nginx\",\n\"hosting\": \"aws\"\n},\n\"non_functional_requirements\": []\n}\n\nOutput:\n[\n{\n\"month\": \"2025-01\",\n\"service\": \"EC2\",\n\"resource_id\": \"i-ecommerce-web-01\",\n\"region\": \"ap-south-1\",\n\"usage_type\": \"Linux/UNIX (on-demand)\",\n\"usage_quantity\": 720,\n\"unit\": \"hours\",\n\"cost_inr\": 900,\n\"desc\": \"Ecommerce web server\"\n},\n{\n\"month\": \"2025-01\",\n\"service\": \"EC2\",\n\"resource_id\": \"i-ecommerce-api-01\",\n\"region\": \"ap-south-1\",\n\"usage_type\": \"Linux/UNIX (on-demand)\",\n\"usage_quantity\": 360,\n\"unit\": \"hours\",\n\"cost_inr\": 450,\n\"desc\": \"Ecommerce API server\"\n},\n]"
                },
                {
                    "role": "user",
                    "content": "Hello world"
                },
                {
                    "role": "assistant",
                    "content": "{\n  \"error\": \"Invalid input\"\n}"
                },
                {
                    "role": "user",
                    "content": "{\n  \"name\": \"Electronic Device Vendor App\",\n   \"budget_inr_per_month\": 150000,\n   \"description\": \"A scalable platform serving ~50k electronics shoppers per month.\",\n   \"tech_stack\": {\n      \"backend\": \"Node.js\",\n      \"database\": \"PostgreSQL\",\n      \"storage\": \"Object Storage (images, media)\",\n      \"monitoring\": \"Basic uptime & performance\",\n      \"analytics\": \"Basic user analytics\"\n   },\n   \"non_functional_requirements\": [\n      \"Scalability\",\n      \"Cost efficiency\",\n      \"Monitoring\",\n      \"Uptime Monitoring\"\n   ]\n}"
                },
                {
                    "role": "assistant",
                    "content": "{\n  \"January 2025\": [\n      {\n         \"month\": \"2025-01\",\n         \"service\": \"RDS\",\n         \"resource_id\": \"r-electronicsdb-01\",\n         \"region\": \"ap-south-1\",\n         \"usage_type\": \"PostgreSQL\",\n         \"usage_quantity\": 7200,\n         \"unit\": \"hours\",\n         \"cost_inr\": 10800,\n         \"desc\": \"PostgreSQL database for electronic device vendor\"\n      },\n      {\n         \"month\": \"2025-01\",\n         \"service\": \"EC2\",\n         \"resource_id\": \"i-electronics-01\",\n         \"region\": \"ap-south-1\",\n         \"usage_type\": \"Linux/UNIX (on-demand)\",\n         \"usage_quantity\": 7200,\n         \"unit\": \"hours\",\n         \"cost_inr\": 10800,\n         \"desc\": \"Compute instance for the application\"\n      },\n      {\n         \"month\": \"2025-01\",\n         \"service\": \"S3\",\n         \"resource_id\": \"s-electronics-media-01\",\n         \"region\": \"ap-south-1\",\n         \"usage_type\": \"Standard Storage (SSD)\",\n         \"usage_quantity\": 3600,\n         \"unit\": \"GB-Mo\",\n         \"cost_inr\": 900,\n         \"desc\": \"Storage for media files in S3\"\n      },\n      {\n         \"month\": \"2025-01\",\n         \"service\": \"CloudWatch\",\n         \"resource_id\": \"c-w-vendorappmetrics-01\",\n         \"region\": \"ap-south-1\",\n         \"usage_quantity\": 2400,\n         \"unit\": \"data points\",\n         \"cost_inr\": 2400,\n         \"desc\": \"Monitoring metrics and logs\"\n      },\n      {\n         \"month\": \"2025-01\",\n         \"service\": \"APIGateway\",\n         \"resource_id\": \"api-gateway-vendorapp-01\",\n         \"region\": \"ap-south-1\",\n         \"usage_quantity\": 360,\n         \"unit\": \"\",\n         \"cost_inr\": 0.0048,\n         \"desc\": \"API Gateway requests\"\n      }\n   ],\n   \"February 2025\": [\n      {\n         \"month\": \"2025-02\",\n         \"service\": \"RDS\",\n         \"resource_id\": \"r-electronicsdb-01\",\n         \"region\": \"ap-south-1\",\n         \"usage_type\": \"PostgreSQL\",\n         \"usage_quantity\": 8400,\n         \"unit\": \"hours\",\n         \"cost_inr\": 12600,\n         \"desc\": \"PostgreSQL database for electronic device vendor\"\n      },\n      {\n         \"month\": \"2025-02\",\n         \"service\": \"EC2\",\n         \"resource_id\": \"i-electronics-01\",\n         \"region\": \"ap-south-1\",\n         \"usage_type\": \"Linux/UNIX (on-demand)\",\n         \"usage_quantity\": 8400,\n         \"unit\": \"hours\",\n         \"cost_inr\": 12600,\n         \"desc\": \"Compute instance for the application\"\n      },\n      {\n         \"month\": \"2025-02\",\n         \"service\": \"S3\",\n         \"resource_id\": \"s-electronics-media-01\",\n         \"region\": \"ap-south-1\",\n         \"usage_type\": \"Standard Storage (SSD)\",\n         \"usage_quantity\": 4000,\n         \"unit\": \"GB-Mo\",\n         \"cost_inr\": 1000,\n         \"desc\": \"Storage for media files in S3\"\n      },\n      {\n         \"month\": \"2025-02\",\n         \"service\": \"CloudWatch\",\n         \"resource_id\": \"c-w-vendorappmetrics-01\",\n         \"region\": \"ap-south-1\",\n         \"usage_quantity\": 3120,\n         \"unit\": \"data points\",\n         \"cost_inr\": 3120,\n         \"desc\": \"Monitoring metrics and logs\"\n      },\n      {\n         \"month\": \"2025-02\",\n         \"service\": \"APIGateway\",\n         \"resource_id\": \"api-gateway-vendorapp-01\",\n         \"region\": \"ap-south-1\",\n         \"usage_quantity\": 432,\n         \"unit\": \"\",\n         \"cost_inr\": 0.00672,\n         \"desc\": \"API Gateway requests\"\n      }\n   ],\n   \"March 2025\": [\n      {\n         \"month\": \"2025-03\",\n         \"service\": \"RDS\",\n         \"resource_id\": \"r-electronicsdb-01\",\n         \"region\": \"ap-south-1\",\n         \"usage_type\": \"PostgreSQL\",\n         \"usage_quantity\": 9600,\n         \"unit\": \"hours\",\n         \"cost_inr\": 14400,\n         \"desc\": \"PostgreSQL database for electronic device vendor\"\n      },\n      {\n         \"month\": \"2025-03\",\n         \"service\": \"EC2\",\n         \"resource_id\": \"i-electronics-01\",\n         \"region\": \"ap-south-1\",\n         \"usage_type\": \"Linux/UNIX (on-demand)\",\n         \"usage_quantity\": 9600,\n         \"unit\": \"hours\",\n         \"cost_inr\": 14400,\n         \"desc\": \"Compute instance for the application\"\n      },\n      {\n         \"month\": \"2025-03\",\n         \"service\": \"S3\",\n         \"resource_id\": \"s-electronics-media-01\",\n         \"region\": \"ap-south-1\",\n         \"usage_type\": \"Standard Storage (SSD)\",\n         \"usage_quantity\": 4800,\n         \"unit\": \"GB-Mo\",\n         \"cost_inr\": 1200,\n         \"desc\": \"Storage for media files in S3\"\n      },\n      {\n         \"month\": \"2025-03\",\n         \"service\": \"CloudWatch\",\n         \"resource_id\": \"c-w-vendorappmetrics-01\",\n         \"region\": \"ap-south-1\",\n         \"usage_quantity\": 3840,\n         \"unit\": \"data points\",\n         \"cost_inr\": 3840,\n         \"desc\": \"Monitoring metrics and logs\"\n      },\n      {\n         \"month\": \"2025-03\",\n         \"service\": \"APIGateway\",\n         \"resource_id\": \"api-gateway-vendorapp-01\",\n         \"region\": \"ap-south-1\",\n         \"usage_quantity\": 504,\n         \"unit\": \"\",\n         \"cost_inr\": 0.00768,\n         \"desc\": \"API Gateway requests\"\n      }\n   ]\n}"
                },
                {
                    "role": "user",
                    "content": project_profile
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

def save_bill(bill_json, file_path="output/mock_billing.json"):
    try:
        os.makedirs("output", exist_ok=True)
        with open(file_path, 'w', encoding="utf-8") as f:
            f.write(bill_json)
        return True, None
    except Exception as e:
        return False, str(e)
