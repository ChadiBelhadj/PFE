import requests
import json

def test_standalone_api():
    # Base URL (for the standalone API on port 8001)
    base_url = "http://localhost:8001"
    
    # Test endpoints
    print("Testing standalone API endpoints:")
    
    # Test root endpoint
    url = f"{base_url}/"
    print(f"\nTesting GET {url}")
    try:
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")
        
        try:
            data = response.json()
            print(f"Response: {json.dumps(data, indent=2)}")
        except:
            print(f"Response: {response.text[:500]}")
    except Exception as e:
        print(f"Error: {str(e)}")
    
    # Test getting patients
    url = f"{base_url}/patients"
    print(f"\nTesting GET {url}")
    try:
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")
        
        try:
            data = response.json()
            print(f"Found {data.get('count', 0)} patients")
            print(f"Status: {data.get('status', 'unknown')}")
        except:
            print(f"Response: {response.text[:500]}")
    except Exception as e:
        print(f"Error: {str(e)}")
    
    # Test creating a patient
    url = f"{base_url}/patients"
    test_patient = {
        "name": "Standalone API Test Patient",
        "age": 40,
        "gender": "Homme",
        "condition": "Test Standalone",
        "status": "Active",
        "phone": "5555555555",
        "email": "standalone.test@example.com",
        "notes": "Standalone API Test",
        "assignedDoctor": "Dr. Standalone",
        "identifier": "S12345",
        "avatar": "/avatars/default.jpg",
        "lastVisit": "01/01/2025",
        "nextAppointment": "01/02/2025"
    }
    
    print(f"\nTesting POST {url}")
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.post(url, json=test_patient, headers=headers)
        print(f"Status Code: {response.status_code}")
        
        try:
            data = response.json()
            print(f"Response: {json.dumps(data, indent=2)}")
        except:
            print(f"Response: {response.text[:500]}")
    except Exception as e:
        print(f"Error: {str(e)}")
    
    print("\nStandalone API testing completed")

if __name__ == "__main__":
    test_standalone_api() 