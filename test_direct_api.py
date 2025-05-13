import requests
import json

def test_direct_api():
    # Base URL
    base_url = "http://localhost:8000"
    
    # Test direct endpoints
    endpoints = [
        "/direct-patients"
    ]
    
    print("Testing direct FastAPI endpoints:")
    
    for endpoint in endpoints:
        url = f"{base_url}{endpoint}"
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
    
    # Test creating a patient directly
    create_url = f"{base_url}/direct-add-patient"
    test_patient = {
        "name": "Direct API Test Patient",
        "age": 35,
        "gender": "Femme",
        "condition": "Test Direct",
        "status": "Active",
        "phone": "9876543210",
        "email": "direct.test@example.com",
        "notes": "Direct API Test",
        "assignedDoctor": "Dr. Direct",
        "identifier": "D98765",
        "avatar": "/avatars/default.jpg",
        "lastVisit": "01/01/2025",
        "nextAppointment": "01/02/2025"
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
        
    print("\nDirect API testing completed")

if __name__ == "__main__":
    test_direct_api() 