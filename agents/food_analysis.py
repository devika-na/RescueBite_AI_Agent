from agents.state import FoodDonationState

from langchain_core.messages import SystemMessage, HumanMessage
import re


FOOD_ANALYSIS_PROMPT = """
You are a Food Analysis AI Agent.

Analyze the food information provided by Vision AI.

Find:
1. Food name
2. Food type (Vegetarian or Non-Vegetarian)
3. Estimated servings
4. Reason

Use Vision AI result as the main source.

Always return exactly in this format:

Food Name:
Food Type:
Estimated Servings:
Reason:
"""


def food_analysis_node(state: FoodDonationState, llm) -> FoodDonationState:

    response = llm.invoke([

        SystemMessage(content=FOOD_ANALYSIS_PROMPT),

        HumanMessage(
            content=f"""
Vision AI Result:

{state.get('vision_result', '')}


User Entered Food Name:

{state.get('food_name', '')}


Quantity:

{state.get('quantity', '')}


Preparation Time:

{state.get('prep_time', '')}
"""
        )

    ])


    result = response.content


    print("========== FOOD ANALYSIS AGENT ==========")
    print(result)
    print("=========================================")


    # Default values

    food_name = state.get("food_name", "Unknown")
    food_type = "Unknown"
    servings = "Unknown"



    # -------------------------
    # Extract Food Name
    # -------------------------

    name_match = re.search(
        r"Food Name:\s*(.*)",
        result,
        re.IGNORECASE
    )

    if name_match:
        food_name = name_match.group(1).strip()



    # -------------------------
    # Extract Food Type
    # -------------------------

    if re.search(
        r"non[-\s]?vegetarian",
        result,
        re.IGNORECASE
    ):
        food_type = "Non-Vegetarian"


    elif re.search(
        r"vegetarian",
        result,
        re.IGNORECASE
    ):
        food_type = "Vegetarian"



    # -------------------------
    # Extract Servings
    # -------------------------

    servings_match = re.search(
        r"Estimated Servings:\s*(.*)",
        result,
        re.IGNORECASE
    )


    if servings_match:
        servings = servings_match.group(1).strip()



    return {

        **state,

        "food_name": food_name,

        "food_type": food_type,

        "servings": servings,

        "reasoning": result

    }