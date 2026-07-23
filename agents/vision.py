import base64

from agents.state import FoodDonationState
from langchain_core.messages import HumanMessage
print("🔥 USING GEMINI VISION FILE 🔥")

VISION_PROMPT = """
You are a Food Vision AI Agent.

Analyze the uploaded food image.

Identify:
- Food name
- Food type (Vegetarian or Non-Vegetarian)
- Confidence
- Estimated freshness

Return clearly in this format:

Food Name:
Food Type:
Confidence:
Estimated Freshness:
Safety Suggestion:
"""


def vision_node(state: FoodDonationState, llm):

    print("=== Vision AI Agent ===")


    image_path = state.get(
        "image_path",
        ""
    )


    if not image_path:

        return {

            **state,

            "vision_result": """
Food Name: Not detected
Food Type: Unknown
Confidence: Not available
"""
        }



    print(
        "Analyzing image:",
        image_path
    )



    try:


        # Read image

        with open(
            image_path,
            "rb"
        ) as image_file:

            image_bytes = image_file.read()



        # Convert image to base64

        encoded_image = base64.b64encode(
            image_bytes
        ).decode("utf-8")



        message = HumanMessage(

            content=[

                {
                    "type": "text",
                    "text": VISION_PROMPT
                },

                {
                    "type": "image_url",

                    "image_url": {

                        "url":
                        f"data:image/jpeg;base64,{encoded_image}"

                    }

                }

            ]

        )



        response = llm.invoke(
            [message]
        )


        result = response.content



        print(
            "=== Gemini Vision Result ==="
        )

        print(result)



        return {

            **state,

            "vision_result": result,

            "food_name": result

        }



    except Exception as e:


        print(
            "Vision Error:",
            e
        )


        return {

            **state,

            "vision_result": """
Food Name: Not available
Food Type: Unknown
Confidence: Not available
"""
        }