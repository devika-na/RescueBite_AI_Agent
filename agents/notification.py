from agents.state import FoodDonationState

from langchain_core.messages import SystemMessage, HumanMessage


NOTIFICATION_PROMPT = """
You are a Notification AI Agent.

Generate notifications for:

1. Food Donor
2. NGO Receiver
3. Delivery Volunteer

Use the donation details.

Keep messages short and clear.
"""


def notification_node(state: FoodDonationState, llm) -> FoodDonationState:

    response = llm.invoke([

        SystemMessage(content=NOTIFICATION_PROMPT),

        HumanMessage(
            content=f"""
Donor:
{state['donor_name']}

Food:
{state['food_name']}

Quantity:
{state['quantity']}

NGO:
{state['matched_ngo']}

Route:
{state['route']}
"""
        )
    ])

    result = response.content

    print("=== Notification Agent ===")
    print(result)

    return {
        **state,
        "notification": result
    }