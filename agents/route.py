from agents.state import FoodDonationState

from langchain_core.messages import SystemMessage, HumanMessage


ROUTE_PROMPT = """
You are a Route Planning AI Agent.

Plan the delivery route.

Return:

Pickup Location:
Destination NGO:
Estimated Delivery Time:
Route Explanation:

Keep it concise.
"""


def route_node(state: FoodDonationState, llm) -> FoodDonationState:

    response = llm.invoke([

        SystemMessage(content=ROUTE_PROMPT),

        HumanMessage(
            content=f"""
Pickup Location:
{state['location']}

NGO:
{state['matched_ngo']}

NGO Location:
{state['ngo_location']}
"""
        )

    ])

    result = response.content

    print("=== Route Planning Agent ===")
    print(result)

    return {
        **state,
        "route": result
    }