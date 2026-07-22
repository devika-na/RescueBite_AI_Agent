from agents.state import FoodDonationState


def impact_node(state: FoodDonationState) -> FoodDonationState:

    print("=== Impact Analytics Agent ===")


    try:
        quantity = float(
            state["quantity"]
            .lower()
            .replace("kg", "")
            .strip()
        )

    except:
        quantity = 0



    # Calculations
    meals_rescued = round(quantity / 0.25)

    co2_reduced = round(quantity * 1.5, 2)



    result = f"""
🍽 Meals Rescued:
{meals_rescued}

♻ Food Saved:
{quantity} kg

🌍 CO₂ Reduced:
{co2_reduced} kg

🎯 SDG Impact:
SDG 2 • Zero Hunger
SDG 12 • Responsible Consumption
SDG 13 • Climate Action
"""


    print(result)



    return {

        **state,

        "impact": result

    }