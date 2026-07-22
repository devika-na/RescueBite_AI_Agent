from agents.state import FoodDonationState

from langchain_core.messages import SystemMessage, HumanMessage

import re


MATCHING_PROMPT = """
You are an NGO Matching AI Agent.

Your job is to select the best NGO for food donation.

Consider:
- Available food quantity
- NGO capacity
- Food preference
- Location

Return exactly:

Selected NGO:
Reason:
"""


def matching_node(state: FoodDonationState, llm, ngos_df) -> FoodDonationState:


    ngo_data = ngos_df.to_string(index=False)


    response = llm.invoke([

        SystemMessage(content=MATCHING_PROMPT),


        HumanMessage(
            content=f"""

Food Detected by Vision AI:

{state['vision_result']}


Quantity:

{state['quantity']}


Food Type:

{state['food_type']}


Donor Location:

{state['location']}



Available NGOs:

{ngo_data}

"""
        )
    ])



    result = response.content


    print("=== NGO Matching Agent ===")
    print(result)



    ngo_match = re.search(
        r"Selected NGO:\s*(.*)",
        result
    )


    if ngo_match:

        selected_ngo = ngo_match.group(1).strip()

    else:

        selected_ngo = "No NGO found"




    # Find NGO location from dataset

    ngo_location = "Unknown"


    ngo_row = ngos_df[
        ngos_df["ngo_name"].str.contains(
            selected_ngo,
            case=False,
            na=False
        )
    ]


    if not ngo_row.empty:

        ngo_location = ngo_row.iloc[0]["location"]




    return {

        **state,

        "matched_ngo": selected_ngo,

        "ngo_location": ngo_location,

        "reasoning": result

    }