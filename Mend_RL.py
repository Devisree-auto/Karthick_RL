import requests

# Replace these with your actual values
API_TOKEN = "your_mend_api_token"
ORG_ID = "your_organization_id"
PROJECT_ID = "your_project_id"

url = "https://api.mend.io/api/v3/vulnerabilities"

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

params = {
    "organizationId": ORG_ID,
    "projectIds": PROJECT_ID,
    "hasCve": "true",
    "severity": "CRITICAL",
    "limit": 50  # Optional: Fetch first 50 results
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    vulnerabilities = response.json().get("data", [])
    for vuln in vulnerabilities:
        print(f"Title      : {vuln.get('title')}")
        print(f"Package    : {vuln.get('package', {}).get('name')}")
        print(f"CVEs       : {', '.join(vuln.get('cveIdentifiers', []))}")
        print(f"Severity   : {vuln.get('severity')}")
        print(f"URL        : {vuln.get('url')}")
        print("-" * 50)
else:
    print(f"Error: {response.status_code} - {response.text}")
