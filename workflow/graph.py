from langgraph.graph import StateGraph, END

from agents.state import FoodDonationState

from agents.intake import intake_node
from agents.vision import vision_node
from agents.food_analysis import food_analysis_node
from agents.food_safety import food_safety_node
from agents.matching import matching_node
from agents.route import route_node
from agents.notification import notification_node
from agents.impact import impact_node



def build_graph(llm, ngos_df):


    builder = StateGraph(FoodDonationState)



    # -------------------------
    # Add Agents
    # -------------------------


    # Intake Agent

    builder.add_node(
        "intake",
        intake_node
    )



    # Vision Agent
    # Manual mode - uses user food input

    builder.add_node(
        "vision",
        vision_node
    )



    # Food Analysis Agent

    builder.add_node(
        "food_analysis",
        lambda state:
            food_analysis_node(
                state,
                llm
            )
    )



    # Food Safety Agent

    builder.add_node(
        "food_safety",
        lambda state:
            food_safety_node(
                state,
                llm
            )
    )



    # NGO Matching Agent

    builder.add_node(
        "matching",
        lambda state:
            matching_node(
                state,
                llm,
                ngos_df
            )
    )



    # Route Planning Agent

    builder.add_node(
        "route",
        lambda state:
            route_node(
                state,
                llm
            )
    )



    # Impact Analytics Agent

    builder.add_node(
        "impact",
        impact_node
    )



    # Notification Agent

    builder.add_node(
        "notification",
        lambda state:
            notification_node(
                state,
                llm
            )
    )



    # -------------------------
    # Workflow Sequence
    # -------------------------


    builder.set_entry_point(
        "intake"
    )



    builder.add_edge(
        "intake",
        "vision"
    )



    builder.add_edge(
        "vision",
        "food_analysis"
    )



    builder.add_edge(
        "food_analysis",
        "food_safety"
    )



    builder.add_edge(
        "food_safety",
        "matching"
    )



    builder.add_edge(
        "matching",
        "route"
    )



    builder.add_edge(
        "route",
        "impact"
    )



    builder.add_edge(
        "impact",
        "notification"
    )



    builder.add_edge(
        "notification",
        END
    )



    graph = builder.compile()


    return graph