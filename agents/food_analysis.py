from agents.state import FoodDonationState

from langchain_core.messages import SystemMessage, HumanMessage


FOOD_ANALYSIS_PROMPT = """
You are a Food Analysis AI Agent.

Analyze donated food details.

Find:
- Food type (Vegetarian or Non-Vegetarian)
- Estimated servings
- Reason

Return clearly.

Format:

Food Type:
Estimated Servings:
Reason:
"""


def food_analysis_node(state: FoodDonationState, llm) -> FoodDonationState:

    response = llm.invoke([
        SystemMessage(content=FOOD_ANALYSIS_PROMPT),

        HumanMessage(
            content=f"""
Food Name:
{state['food_name']}

Quantity:
{state['quantity']}

Preparation Time:
{state['prep_time']}
"""
        )
    ])

    result = response.content

    print("=== Food Analysis Agent ===")
    print(result)

    import re

    servings_match = re.search(
        r"Estimated Servings:\s*(.*)",
        result
    )

    if servings_match:
        servings = servings_match.group(1).strip()
    else:
        servings = "Not calculated"


    food_type = (
        "Non-Vegetarian"
        if "Non-Vegetarian" in result
        else "Vegetarian"
    )


    return {
        **state,
        "food_type": food_type,
        "servings": servings,
        "reasoning": result
    }