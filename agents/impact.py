from agents.state import FoodDonationState

from langchain_core.messages import SystemMessage, HumanMessage


IMPACT_PROMPT = """
You are an Impact Analytics AI Agent.

Calculate the sustainability impact of a food donation.

Calculate:

- Meals rescued
- Food waste prevented (kg)
- Estimated CO2 reduction (kg)
- SDG contribution

Assume:
1 meal = 0.25 kg food
1 kg food waste prevented = 1.5 kg CO2 reduction

Return a clear report.
"""


def impact_node(state: FoodDonationState, llm) -> FoodDonationState:

    response = llm.invoke([

        SystemMessage(content=IMPACT_PROMPT),

        HumanMessage(
            content=f"""
Food:
{state['food_name']}

Quantity:
{state['quantity']}

Food Type:
{state['food_type']}
"""
        )
    ])

    result = response.content

    print("=== Impact Analytics Agent ===")
    print(result)

    return {
        **state,
        "impact": result
    }