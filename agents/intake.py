from agents.state import FoodDonationState


def intake_node(state: FoodDonationState) -> FoodDonationState:

    print("=== Food Donation Intake Agent ===")


    return {

        # User details
        "donor_name": state["donor_name"],
        "organization": state["organization"],


        # IMPORTANT:
        # Do not trust manually entered food name.
        # Vision AI will detect the food from image.
        "food_name": "",


        # Donation details
        "quantity": state["quantity"],
        "prep_time": state["prep_time"],
        "location": state["location"],



        # Vision AI output
        "vision_result": "",


        # Food analysis
        "food_type": "",
        "servings": "",



        # Safety Agent
        "safety_status": "",
        "safe_until": "",



        # Decision
        "decision": "",



        # NGO Matching Agent
        "matched_ngo": "",



        # Logistics Agent
        "route": "",



        # Notification Agent
        "notification": "",



        # Sustainability
        "impact": "",



        # Agent reasoning
        "reasoning": ""

    }