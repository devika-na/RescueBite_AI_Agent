from typing import TypedDict


class FoodDonationState(TypedDict):

    # -----------------------
    # Donation Intake Details
    # -----------------------

    donor_name: str
    organization: str

    # User entered value (optional reference)
    # Final food name comes from Vision AI
    food_name: str

    quantity: str
    prep_time: str
    location: str


    # -----------------------
    # Vision AI Agent Output
    # -----------------------

    image_path: str
    vision_result: str



    # -----------------------
    # Food Analysis Agent
    # -----------------------

    food_type: str
    servings: str



    # -----------------------
    # Food Safety Agent
    # -----------------------

    safety_status: str
    safe_until: str
    risk_level: str



    # -----------------------
    # NGO Matching Agent
    # -----------------------

    matched_ngo: str
    ngo_location: str



    # -----------------------
    # Logistics Agent
    # -----------------------

    route: str



    # -----------------------
    # Notification Agent
    # -----------------------

    notification: str



    # -----------------------
    # Sustainability Agent
    # -----------------------

    impact: str



    # -----------------------
    # Agent Reasoning
    # -----------------------

    reasoning: str