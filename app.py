import os
import pandas as pd

from dotenv import load_dotenv

from langchain_groq import ChatGroq

from workflow.graph import build_graph

load_dotenv()

# Load API key
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    api_key=groq_api_key
)

print("Groq LLM initialized successfully")

# Load NGO dataset
ngos_df = pd.read_csv("data/ngos.csv")

print("NGO dataset loaded successfully")

# Build workflow
graph = build_graph(llm, ngos_df)

print("RescueBite AI Workflow Created Successfully 🚀")

# Run workflow
graph.invoke({})