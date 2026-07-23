from agents.state import FoodDonationState


def intake_node(state: FoodDonationState) -> FoodDonationState:

    print("=== Food Donation Intake Agent ===")

    print("Donor:", state.get("donor_name"))
    print("Organization:", state.get("organization"))
    print("Food:", state.get("food_name"))
    print("Quantity:", state.get("quantity"))
    print("Location:", state.get("location"))


    return {


        # -----------------------
        # Donation Intake Details
        # -----------------------

        "donor_name": state.get(
            "donor_name",
            ""
        ),

        "organization": state.get(
            "organization",
            ""
        ),


        # IMPORTANT:
        # Keep user entered food name
        # Vision AI is optional now

        "food_name": state.get(
            "food_name",
            "Unknown"
        ),


        "quantity": state.get(
            "quantity",
            ""
        ),

        "prep_time": state.get(
            "prep_time",
            ""
        ),

        "location": state.get(
            "location",
            ""
        ),



        # -----------------------
        # Vision AI Output
        # -----------------------

        "image_path": state.get(
            "image_path",
            ""
        ),

        "vision_result": "",



        # -----------------------
        # Food Analysis Agent
        # -----------------------

        "food_type": "",

        "servings": "",



        # -----------------------
        # Food Safety Agent
        # -----------------------

        "safety_status": "",

        "safe_until": "",

        "risk_level": "",



        # -----------------------
        # NGO Matching Agent
        # -----------------------

        "matched_ngo": "",

        "ngo_location": "",



        # -----------------------
        # Logistics Agent
        # -----------------------

        "route": "",



        # -----------------------
        # Notification Agent
        # -----------------------

        "notification": "",



        # -----------------------
        # Sustainability Agent
        # -----------------------

        "impact": "",



        # -----------------------
        # Agent Reasoning
        # -----------------------

        "reasoning": ""

    }