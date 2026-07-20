from agents.state import FoodDonationState


def intake_node(state: FoodDonationState) -> FoodDonationState:

    print("=== Food Donation Intake Agent ===")

    return {

        "donor_name": state["donor_name"],
        "organization": state["organization"],

        "food_name": state["food_name"],
        "quantity": state["quantity"],
        "prep_time": state["prep_time"],
        "location": state["location"],

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