from langgraph.graph import StateGraph, END

from agents.state import FoodDonationState

from agents.intake import intake_node
from agents.food_analysis import food_analysis_node
from agents.food_safety import food_safety_node
from agents.matching import matching_node
from agents.route import route_node
from agents.notification import notification_node
from agents.impact import impact_node


def build_graph(llm, ngos_df):

    builder = StateGraph(FoodDonationState)

    # Add all agents
    builder.add_node("intake", intake_node)

    builder.add_node(
        "food_analysis",
        lambda state: food_analysis_node(state, llm)
    )

    builder.add_node(
        "food_safety",
        lambda state: food_safety_node(state, llm)
    )

    builder.add_node(
        "matching",
        lambda state: matching_node(state, llm, ngos_df)
    )

    builder.add_node(
        "route",
        lambda state: route_node(state, llm)
    )

    builder.add_node(
        "notification",
        lambda state: notification_node(state, llm)
    )

    builder.add_node(
        "impact",
        lambda state: impact_node(state, llm)
    )

    # Workflow
    builder.set_entry_point("intake")

    builder.add_edge("intake", "food_analysis")
    builder.add_edge("food_analysis", "food_safety")
    builder.add_edge("food_safety", "matching")
    builder.add_edge("matching", "route")
    builder.add_edge("route", "notification")
    builder.add_edge("notification", "impact")
    builder.add_edge("impact", END)

    graph = builder.compile()

    return graph