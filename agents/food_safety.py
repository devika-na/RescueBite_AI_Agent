from agents.state import FoodDonationState

from langchain_core.messages import SystemMessage, HumanMessage


SAFETY_PROMPT = """
You are a Food Safety AI Agent.

Analyze the donated food.

Return ONLY this format:

Safety Status:
Safe or Unsafe

Safe Until:
Mention time

Risk Level:
Low, Medium, or High

Reason:
One short sentence


Rules:
- Cooked food is usually safer within a few hours after preparation.
- Non-vegetarian foods like chicken require more caution.
"""


def food_safety_node(state: FoodDonationState, llm) -> FoodDonationState:

    response = llm.invoke([

        SystemMessage(content=SAFETY_PROMPT),

        HumanMessage(
            content=f"""
Food Name:
{state['food_name']}

Food Type:
{state['food_type']}

Preparation Time:
{state['prep_time']}

Current Location:
{state['location']}
"""
        )
    ])


    result = response.content

    print("=== Food Safety Agent ===")
    print(result)


    import re

    safe_until_match = re.search(
        r"Safe Until:\s*(.*)",
        result
    )

    if safe_until_match:
        safe_until = safe_until_match.group(1).strip()
    else:
        safe_until = "Not specified"


    return {
        **state,
        "safety_status": result,
        "safe_until": safe_until
    }