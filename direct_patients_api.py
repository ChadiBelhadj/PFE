from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pymongo import MongoClient
import traceback
from typing import Dict, Any

# Create standalone FastAPI app
app = FastAPI(title="Direct Patients API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["medical_db"]
patients_collection = db["patients"]

@app.get("/")
async def root():
    return {"message": "Direct Patients API", "status": "running"}

@app.get("/patients")
async def get_patients():
    try:
        # Get all patients
        patients = []
        for doc in patients_collection.find():
            # Convert ObjectId to string
            doc["id"] = str(doc.pop("_id"))
            patients.append(doc)
        
        return {"status": "success", "count": len(patients), "patients": patients}
    except Exception as e:
        return {
            "status": "error",
            "message": f"Error fetching patients: {str(e)}",
            "traceback": traceback.format_exc()
        }

@app.post("/patients")
async def add_patient(patient: Dict[str, Any]):
    try:
        # Insert patient
        result = patients_collection.insert_one(patient)
        
        # Get created patient
        created_patient = patients_collection.find_one({"_id": result.inserted_id})
        
        if created_patient:
            # Convert ObjectId to string
            created_patient["id"] = str(created_patient.pop("_id"))
            return {"status": "success", "patient": created_patient}
        else:
            return {"status": "error", "message": "Failed to create patient"}
    except Exception as e:
        return {
            "status": "error",
            "message": f"Error creating patient: {str(e)}",
            "traceback": traceback.format_exc()
        }

if __name__ == "__main__":
    print("Starting Direct Patients API on port 8001...")
    uvicorn.run("direct_patients_api:app", host="0.0.0.0", port=8001, reload=True) 