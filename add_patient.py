import asyncio
from pymongo import MongoClient
import sys

async def add_patient(name, age, gender, condition):
    # Connect to MongoDB directly
    client = MongoClient("mongodb://localhost:27017/")
    db = client["medical_db"]  # Adjust database name if needed
    patients_collection = db["patients"]
    
    # Create patient
    patient = {
        "name": name,
        "age": int(age),
        "gender": gender,
        "condition": condition,
        "status": "Nouveau",
        "phone": "0000000000",
        "email": f"{name.lower().replace(' ', '.')}@example.com",
        "notes": "",
        "assignedDoctor": "",
        "avatar": "/avatars/default.jpg",
        "lastVisit": "",
        "nextAppointment": "",
        "bloodSugar": None,
        "bloodPressure": None,
        "enzymesHépatiques": None,
        "bilirubine": None
    }
    
    # Insert the patient
    result = patients_collection.insert_one(patient)
    
    # Print result
    if result.inserted_id:
        print(f"SUCCESS: Added patient {name} with ID: {result.inserted_id}")
        print(f"Patient data: {patient}")
    else:
        print(f"FAILED: Could not add patient {name}")
    
    # Close connection
    client.close()

# Run the function
if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python add_patient.py \"Patient Name\" 25 \"Gender\" \"Condition\"")
    else:
        name = sys.argv[1]
        age = sys.argv[2]
        gender = sys.argv[3]
        condition = sys.argv[4]
        asyncio.run(add_patient(name, age, gender, condition)) 