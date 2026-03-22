#project: risk score calculator
#purpose: learn lists and loops
#relevance: GRC (Governance, Risk, and Compliance) engineering rotation at ING
print("Welcome to the Risk Score Calculator!")
#---SECTION 1: LIST OF RISK FACTORS---
risks = [
    {"id": "R001", "description": "Unauthorised access to customer data", "category": "Confidentiality", "likelihood": 4, "impact": 5},
    {"id": "R002", "description": "System downtime during peak trading", "category": "Availability", "likelihood": 4, "impact": 4},
    {"id": "R003", "description": "Misconfigured cloud storage bucket", "category": "Confidentiality", "likelihood": 2, "impact": 5},
    {"id": "R004", "description": "Outdated software with known vulnerabilities", "category": "Integrity", "likelihood": 4, "impact": 3},
    {"id": "R005", "description": "Phishing attack on employee credentials", "category": "Confidentiality", "likelihood": 5, "impact": 4},
]
#---SECTION 2: RISK SCORE FUNCTION---
def calculate_risk(risk):
    score = risk["likelihood"] * risk["impact"]
    if score >= 15:
        risk_level = "High"
    elif score >= 8:
        risk_level = "Medium"
    else:
        risk_level = "Low"
    return score, risk_level
#---SECTION 3: LOOP THROUGH RISKS---
print("="*50)
print("     IT RISK ASSESSMENT REPORT - ING BANK UK")
print("="*50)
for risk in risks:
    score, level = calculate_risk(risk)
    print(f"Risk ID: {risk['id']}")
    print(f"Description: {risk['description']}")
    print(f"Category: {risk['category']}")
    print(f"Likelihood: {risk['likelihood']}")
    print(f"Impact: {risk['impact']}")
    print(f"Risk Score: {score} - {level} Risk")
    print("-"*50)
#---SECTION 4: SUMMARY---
high = 0
medium = 0
low = 0
for risk in risks:
    score, level = calculate_risk(risk)
    if level == "High":
        high += 1
    elif level == "Medium":
        medium += 1
    else:
        low += 1
print("\n" + "="*50)  
print("     RISK ASSESSMENT SUMMARY")   
print("="*50)   
print(f"High Risk: {high} risks")
print(f"Medium Risk: {medium} risks")
print(f"Low Risk: {low} risks")
print(f"\nTotal Risks Assessed: {high + medium + low}")
print ("="*50)
print("Thank you for using the Risk Score Calculator! Stay vigilant and manage your risks effectively.")