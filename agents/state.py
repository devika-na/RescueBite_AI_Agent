from typing import TypedDict


class FoodDonationState(TypedDict):

    donor_name: str
    organization: str

    food_name: str
    quantity: str
    prep_time: str
    location: str

    food_type: str
    servings: str

    safety_status: str
    safe_until: str

    decision: str   # ✅ New field

    matched_ngo: str

    route: str

    notification: str

    impact: str

    reasoning: str