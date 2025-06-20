import requests
import json

# Configuration
API_TOKEN = "your_mend_api_token"
ORG_ID = "your_org_id"
PROJECT_ID = "your_project_id"
BASE_URL = "https://api.mend.io"

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

def fetch_vulnerabilities(org_id, project_id):
    url = f"{BASE_URL}/api/v1/projects/{project_id}/vulnerabilities?organizationId={org_id}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        vulnerabilities = data.get('vulnerabilities', [])

        # Filter only those with CVEs
        cve_list = [v for v in vulnerabilities if v.get("cveIdentifiers")]

        for v in cve_list:
            print(f"Package: {v['packageName']}")
            print(f"Severity: {v['severity']}")
            print(f"CVEs: {', '.join(v['cveIdentifiers'])}")
            print(f"Description: {v.get('description', 'N/A')}")
            print(f"Link: {v.get('vulnerabilityURL', 'N/A')}")
            print("-" * 50)

        return cve_list
    else:
        print(f"Failed to fetch data: {response.status_code} - {response.text}")
        return []

if __name__ == "__main__":
    fetch_vulnerabilities(ORG_ID, PROJECT_ID)
