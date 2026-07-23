import os
import pandas as pd

from dotenv import load_dotenv

from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware

from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI

from workflow.graph import build_graph


# Load environment variables
load_dotenv()


# Create FastAPI app

app = FastAPI(
    title="RescueBite AI API",
    description="AI Food Rescue Network using Agentic AI",
    version="1.0"
)



# Enable React frontend communication

app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173",
        "https://rescue-bite-frontend.vercel.app"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)



# -----------------------------
# Initialize Groq LLM
# Used by text-based agents
# -----------------------------

groq_api_key = os.getenv("GROQ_API_KEY")


llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    api_key=groq_api_key
)


print("Groq LLM initialized successfully")



# -----------------------------
# Initialize Gemini Vision LLM
# Used by Vision Agent
# -----------------------------

google_api_key = os.getenv("GOOGLE_API_KEY")


vision_llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    google_api_key=google_api_key
)


print("Gemini Vision initialized successfully")



# -----------------------------
# Load NGO dataset
# -----------------------------

ngos_df = pd.read_csv(
    "data/ngos.csv"
)


print("NGO dataset loaded successfully")



# -----------------------------
# Build LangGraph Workflow
# -----------------------------

graph = build_graph(
    llm,
    vision_llm,
    ngos_df
)


print("RescueBite AI Workflow Created Successfully 🚀")




# Home API

@app.get("/")
def home():

    return {
        "message": "RescueBite AI Backend Running 🚀"
    }




# -----------------------------
# Donation API
# -----------------------------

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


    image_path = ""


    # Save uploaded image

    if image:

        os.makedirs(
            "uploads",
            exist_ok=True
        )


        image_path = (
            f"uploads/{image.filename}"
        )


        with open(
            image_path,
            "wb"
        ) as f:

            f.write(
                await image.read()
            )


        print(
            "Image saved:",
            image_path
        )



    # LangGraph State

    state = {


        "donor_name": donor_name,

        "organization": organization,


        "food_name": food_name,

        "quantity": quantity,

        "prep_time": prep_time,

        "location": location,


        "image_path": image_path,

        "vision_result": "",



        "food_type": "",

        "servings": "",



        "safety_status": "",

        "safe_until": "",

        "risk_level": "",



        "matched_ngo": "",

        "ngo_location": "",



        "route": "",



        "notification": "",



        "impact": "",



        "reasoning": ""

    }



    result = graph.invoke(state)


    return result