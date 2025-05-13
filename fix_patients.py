import asyncio
from pymongo import MongoClient

async def fix_patients():
    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client["medical_db"]  # Adjust if needed
    patients_collection = db["patients"]
    
    print("Starting patient database fix...")
    
    # Get all patients
    patients = list(patients_collection.find())
    print(f"Found {len(patients)} patients to check")
    
    fixed_count = 0
    
    # Required fields with default values
    required_fields = {
        "name": "Unknown",
        "age": 0,
        "gender": "Unknown",
        "condition": "Unknown",
        "status": "Unknown",
        "phone": "0000000000",
        "email": "unknown@example.com",
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
    
    # Fix each patient
    for patient in patients:
        patient_id = patient["_id"]
        needs_update = False
        update_data = {}
        
        # Check and fix each required field
        for field, default_value in required_fields.items():
            if field not in patient or patient[field] is None:
                update_data[field] = default_value
                needs_update = True
                print(f"Patient {patient_id}: Missing field '{field}', setting to default")
        
        # Update if needed
        if needs_update:
            result = patients_collection.update_one(
                {"_id": patient_id},
                {"$set": update_data}
            )
            if result.modified_count > 0:
                fixed_count += 1
    
    print(f"Fixed {fixed_count} patients out of {len(patients)}")
    
    # Close connection
    client.close()

if __name__ == "__main__":
    asyncio.run(fix_patients()) 