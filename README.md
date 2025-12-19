# Cloud Cost Optimizer

A CLI-based Cloud Cost Optimization tool that analyzes project descriptions and generates cost-saving recommendations using AI (Groq LLM).

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Examples](#examples)
- [Output Files](#output-files)
- [Tools Used](#tools-used)

## Features

- **Project Profile Extraction** - Converts free-form project descriptions into structured JSON
- **Mock Billing Generation** - Creates realistic cloud billing data based on project requirements
- **Cost Optimization Recommendations** - Generates multi-cloud (AWS, Azure, GCP) optimization suggestions
- **HTML Report Export** - Professional, printer-friendly reports generated via AI
- **Budget Analysis** - Identifies over-budget scenarios and high-cost services
- **Error Handling** - Validates input and breaks flow on invalid data

## Prerequisites

- Python 3.10+
- Groq API Key ([Get one here](https://console.groq.com/keys))

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/AkashDholakiya/Cloud-Cost-Optimizer.git
   cd Cloud-Cost-Optimizer
   ```

2. **Create virtual environment**
   ```bash
   python -m venv env
   ```

3. **Activate virtual environment**
   
   Windows:
   ```bash
   .\env\Scripts\activate
   ```
   
   macOS/Linux:
   ```bash
   source env/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. **Create a `.env` file** in the project root:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

## Usage

### Run the Application

```bash
python cost_optimizer.py
```

### Menu Options

```
1. Enter a new project description
2. Run Complete Cost Analysis
3. View Recommendations
4. Export Report
5. Exit
```

### Step-by-Step Workflow

1. **Option 1** - Enter your project description
2. **Option 2** - Run the complete cost analysis pipeline
3. **Option 3** - View recommendations in terminal
4. **Option 4** - Export professional HTML report
5. **Option 5** - Exit the application

## Examples

### Example 1: E-Commerce Platform

Create `project_description.txt`:

```
I am building an E-commerce application where monthly users could be around 1 million. 
The application will have features like user authentication, product catalog, shopping cart, 
payment gateway integration, order management, and user reviews.

Tech stack: React Next.js for frontend and backend, Firebase for database.

The application should be scalable to handle high traffic during sales events and secure 
to protect user data and payment information. Using Nginx for proxy and load balancing.

Monthly Budget: 50,000 INR
```

### Example 2: Food Delivery App

```
We are building a food delivery app for 10,000 users per month.
Budget: ₹50,000 per month.

Tech stack: Node.js backend, PostgreSQL database, object storage for images, 
monitoring, and basic analytics.

Non-functional requirements: scalability, cost efficiency, uptime monitoring.
```

### Example 3: Fitness Coaching Platform

```
Building an online fitness coaching platform for ~8,000 monthly subscribers.

Features: Video streaming for workout sessions, user authentication, subscription management,
progress tracking, and coach-student messaging.

Tech Stack:
- Backend: Django
- Database: PostgreSQL
- Cache: Redis
- Storage: AWS S3 for media
- Frontend: React

Requirements: High availability, secure authentication, stable video streaming, low latency.

Monthly Budget: 35,000 INR
```

## Output Files

| File | Description |
|------|-------------|
| `project_profile.json` | Structured project profile with tech stack, budget, requirements |
| `mock_billing.json` | Synthetic cloud billing records (12-20 entries) |
| `cost_optimization_report.json` | Detailed recommendations with savings analysis |
| `cost_report.html` | Professional HTML report |

### Sample Output Structure

**project_profile.json**
```json
{
  "name": "E-Commerce Platform",
  "budget_inr_per_month": 50000,
  "description": "A scalable e-commerce platform...",
  "tech_stack": {
    "frontend": "React Next.js",
    "backend": "Next.js API Routes",
    "database": "Firebase"
  },
  "non_functional_requirements": ["Scalability", "Security", "High Availability"]
}
```

**mock_billing.json**
```json
{
"January 2025": [
    {
        "month": "2025-01",
        "service": "EC2",
        "resource_id": "i-crm-01",
        "region": "ap-south-1",
        "usage_type": "Linux/UNIX (on-demand)",
        "usage_quantity": 7200,
        "unit": "hours",
        "cost_inr": 10800,
        "desc": "Spring Boot application instance"
    },
    {
        "month": "2025-01",
        "service": "RDS",
        "resource_id": "r-crmdb-01",
        "region": "ap-south-1",
        "usage_type": "MySQL",
        "usage_quantity": 7200,
        "unit": "hours",
        "cost_inr": 10800,
        "desc": "MySQL database for CRM"
    },
    {
        "month": "2025-01",
        "service": "S3",
        "resource_id": "s-crm-storage-01",
        "region": "ap-south-1",
        "usage_type": "Standard Storage (SSD)",
        "usage_quantity": 1200,
        "unit": "GB-Mo",
        "cost_inr": 180,
        "desc": "Storage for CRM documents in S3"
    },
    {
        "month": "2025-01",
        "service": "CloudWatch",
        "resource_id": "c-w-crmmetrics-01",
        "region": "ap-south-1",
        "usage_quantity": 1920,
        "unit": "data points",
        "cost_inr": 1920,
        "desc": "Monitoring metrics and logs"
    }
]
}
```

**cost_optimization_report.json**
```json
{
  "project_name": "E-Commerce Platform",
  "analysis": {
    "total_monthly_cost": 65000,
    "budget": 50000,
    "budget_variance": 15000,
    "is_over_budget": true
  },
  "recommendations": [...],
  "summary": {
    "total_potential_savings": 25000,
    "savings_percentage": 38.46
  }
}
```

## Tools Used

- [Groq LLM](https://www.groq.com/) - For AI-driven text analysis and generation
- [Github Copilot](https://github.com/features/copilot) - For Assistance

## Demo Video: [Cloud Cost Optimizer](https://drive.google.com/file/d/1I306wG-VgsJpjJGxrhpgDqn8075gaape/view)