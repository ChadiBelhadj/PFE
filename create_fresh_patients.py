import asyncio
from pymongo import MongoClient

async def create_fresh_patients():
    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client["medical_db"]  # Adjust if needed
    
    # Drop existing patients collection if it exists
    if "patients" in db.list_collection_names():
        db.patients.drop()
        print("Dropped existing patients collection")
    
    # Create a new patients collection
    patients_collection = db.create_collection("patients")
    print("Created new patients collection")
    
    # Sample patient with all required fields
    sample_patient = {
        "name": "Chadi Belhadj",
        "age": 19,
        "gender": "Homme",
        "condition": "Diabète",
        "status": "Nouveau",
        "phone": "0770651959",
        "email": "belhadjchadi@gmail.com",
        "notes": "Test",
        "assignedDoctor": "Dr. Martin",
        "identifier": "P12345",
        "avatar": "/avatars/default.jpg",
        "lastVisit": "05/05/2025",
        "nextAppointment": "",
        "bloodSugar": None,
        "bloodPressure": None,
        "enzymesHépatiques": None,
        "bilirubine": None
    }
    
    # Insert sample patient
    result = patients_collection.insert_one(sample_patient)
    print(f"Added sample patient with ID: {result.inserted_id}")
    
    # Close connection
    client.close()
    
    print("\nFresh patients collection created successfully!")
    print("You can now try the /patients/ endpoint again.")

if __name__ == "__main__":
    asyncio.run(create_fresh_patients()) 