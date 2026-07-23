from agents.state import FoodDonationState


def vision_node(state: FoodDonationState):

    print("=== Vision AI Agent (Manual Mode) ===")

    food_name = state.get(
        "food_name",
        "Unknown"
    )


    result = f"""
Food Name: {food_name}

Food Type:
Detected from user input

Confidence:
Manual Entry

Estimated Freshness:
Check preparation time

Safety Suggestion:
Follow food safety guidelines
"""


    print(result)


    return {

        **state,

        "vision_result": result,

        "food_name": food_name

    }