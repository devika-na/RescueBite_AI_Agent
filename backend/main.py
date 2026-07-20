from fastapi.middleware.cors import CORSMiddleware
import os
import pandas as pd

from fastapi import FastAPI, Form, UploadFile, File
from dotenv import load_dotenv

from langchain_groq import ChatGroq

from workflow.graph import build_graph


# Load environment variables
load_dotenv()


# Initialize FastAPI
app = FastAPI(
    title="RescueBite AI API",
    description="AI Food Rescue Network using Agentic AI",
    version="1.0"
)


# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Initialize Groq LLM
groq_api_key = os.getenv("GROQ_API_KEY")


llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    api_key=groq_api_key
)


# Load NGO dataset
ngos_df = pd.read_csv("data/ngos.csv")


# Build LangGraph workflow
graph = build_graph(llm, ngos_df)


print("RescueBite AI Graph Loaded 🚀")



@app.get("/")
def home():

    return {
        "message": "RescueBite AI Backend Running 🚀"
    }



@app.post("/donate")
async def create_donation(

    donor_name: str = Form(...),
    organization: str = Form(...),
    food_name: str = Form(...),
    quantity: str = Form(...),
    prep_time: str = Form(...),
    location: str = Form(...),
    image: UploadFile = File(None)

):


    image_path = None


    if image:

        os.makedirs("uploads", exist_ok=True)

        image_path = f"uploads/{image.filename}"

        with open(image_path, "wb") as f:

            f.write(await image.read())



    initial_state = {


        "donor_name": donor_name,

        "organization": organization,

        "food_name": food_name,

        "quantity": quantity,

        "prep_time": prep_time,

        "location": location,


        "image_path": image_path,


        "food_type": "",

        "servings": "",


        "safety_status": "",

        "safe_until": "",


        "decision": "",


        "matched_ngo": "",


        "route": "",


        "notification": "",


        "impact": "",


        "reasoning": ""

    }



    result = graph.invoke(initial_state)



    return result