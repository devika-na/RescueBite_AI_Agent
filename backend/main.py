from fastapi.middleware.cors import CORSMiddleware
import os
import pandas as pd

from fastapi import FastAPI
from pydantic import BaseModel
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
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
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


# Request model
class DonationRequest(BaseModel):

    donor_name: str
    organization: str
    food_name: str
    quantity: str
    prep_time: str
    location: str



@app.get("/")
def home():

    return {
        "message": "RescueBite AI Backend Running 🚀"
    }



@app.post("/donate")
def create_donation(donation: DonationRequest):

    initial_state = {

        "donor_name": donation.donor_name,
        "organization": donation.organization,

        "food_name": donation.food_name,
        "quantity": donation.quantity,
        "prep_time": donation.prep_time,
        "location": donation.location,

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