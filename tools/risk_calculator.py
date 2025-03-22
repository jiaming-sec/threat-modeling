# tools/risk_calculator.py

def calculate_risk(likelihood, impact):
    return likelihood * impact
    
threats = [
    {"name": "SQL Injection", "likelihood": 8, "impact": 9},
    {"name": "DDoS Attack", "likelihood": 7, "impact": 10},
    {"name": "Insider Threat", "likelihood": 4, "impact": 7},
]
