from agents.state import FoodDonationState

from langchain_core.messages import SystemMessage, HumanMessage

import re



FOOD_ANALYSIS_PROMPT = """
You are a Food Analysis AI Agent.

Analyze the donated food.

Rules:
- The user entered food name is the primary source.
- Do not replace a valid food name with "Not specified" or "Unknown".
- Determine food type as Vegetarian or Non-Vegetarian.
- Estimate servings based on quantity.

Return exactly in this format:

Food Name:
Food Type:
Estimated Servings:
Reason:
"""



def food_analysis_node(state: FoodDonationState, llm) -> FoodDonationState:


    user_food_name = state.get(
        "food_name",
        "Unknown"
    )


    response = llm.invoke([


        SystemMessage(
            content=FOOD_ANALYSIS_PROMPT
        ),



        HumanMessage(
            content=f"""
User Entered Food Name:

{user_food_name}


Quantity:

{state.get('quantity','')}


Preparation Time:

{state.get('prep_time','')}


Vision Information:

{state.get('vision_result','')}
"""
        )

    ])



    result = response.content



    print("========== FOOD ANALYSIS AGENT ==========")
    print(result)
    print("=========================================")



    # -------------------------
    # Default values
    # -------------------------

    food_name = user_food_name

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

        extracted_name = (
            name_match.group(1)
            .strip()
        )


        if extracted_name.lower() not in [
            "",
            "unknown",
            "not specified",
            "not detected",
            "none"
        ]:

            food_name = extracted_name



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

        extracted_servings = (
            servings_match.group(1)
            .strip()
        )


        if extracted_servings.lower() not in [
            "",
            "unknown",
            "not specified"
        ]:

            servings = extracted_servings



    return {


        **state,


        "food_name": food_name,


        "food_type": food_type,


        "servings": servings,


        "reasoning": result

    }