from agents.state import FoodDonationState


def intake_node(state: FoodDonationState) -> FoodDonationState:

    print("=== Food Donation Intake Form ===")

    donor_name = input("Donor name: ")
    organization = input("Organization/Event name: ")

    food_name = input("Food name: ")
    quantity = input("Quantity of food (include unit like kg/packs/plates): ")

    prep_time = input("Preparation time: ")
    location = input("Pickup location: ")

    return {

        "donor_name": donor_name,
        "organization": organization,

        "food_name": food_name,
        "quantity": quantity,
        "prep_time": prep_time,
        "location": location,

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