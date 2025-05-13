import requests
import json

def test_patients_api():
    # Base URL
    base_url = "http://localhost:8000"  # Adjust port if needed
    
    # Test endpoints
    endpoints = [
        "/",
        "/test",
        "/patients",
        "/patients/"
    ]
    
    print("Testing FastAPI endpoints:")
    
    for endpoint in endpoints:
        url = f"{base_url}{endpoint}"
        print(f"\nTesting GET {url}")
        
        try:
            response = requests.get(url)
            print(f"Status Code: {response.status_code}")
            print(f"Headers: {dict(response.headers)}")
            
            try:
                # Try to parse as JSON
                data = response.json()
                print(f"Response (JSON): {json.dumps(data, indent=2)}")
            except:
                # If not JSON, show as text
                print(f"Response (Text): {response.text[:500]}")
                
        except Exception as e:
            print(f"Error: {str(e)}")
    
    # Test creating a patient
    create_url = f"{base_url}/patients/"
    test_patient = {
        "name": "API Test Patient",
        "age": 30,
        "gender": "Homme",
        "condition": "Test Condition",
        "status": "Test",
        "phone": "1234567890",
        "email": "test.api@example.com",
        "notes": "API Test",
        "assignedDoctor": "Dr. Test",
        "identifier": "T54321",
        "avatar": "/avatars/default.jpg",
        "lastVisit": "",
        "nextAppointment": "",
        "bloodSugar": None,
        "bloodPressure": None,
        "enzymesHépatiques": None,
        "bilirubine": None
    }
    
    print(f"\nTesting POST {create_url}")
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.post(create_url, json=test_patient, headers=headers)
        print(f"Status Code: {response.status_code}")
        
        try:
            data = response.json()
            print(f"Response: {json.dumps(data, indent=2)}")
        except:
            print(f"Response: {response.text[:500]}")
            
    except Exception as e:
        print(f"Error: {str(e)}")
        
    print("\nAPI testing completed")

if __name__ == "__main__":
    test_patients_api() 