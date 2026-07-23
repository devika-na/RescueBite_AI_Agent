from PIL import Image
from google import genai
import os

from agents.state import FoodDonationState


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


print("Food Vision Model Ready 🚀")


def analyze_food_image(image_path):

    image = Image.open(image_path).convert("RGB")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            """
            Analyze this food image.

            Give:
            - Food name
            - Food type (Veg/Non-Veg)
            - Estimated quantity
            - Freshness observations
            - Safety suggestion for donation
            """,
            image
        ]
    )

    result = response.text

    # simple extraction fallback
    food = "Unknown"

    if "Food name:" in result:
        food = result.split("Food name:")[1].split("\n")[0].strip()

    return result, food



def vision_node(state: FoodDonationState):

    print("=== Vision AI Agent ===")


    image_path = state.get("image_path", "")


    detected_food = state.get(
        "food_name",
        "Unknown"
    )


    if image_path:

        print("Analyzing image:", image_path)

        try:

            result, detected_food = analyze_food_image(
                image_path
            )


        except Exception as e:

            print("Vision Error:", e)

            result = f"""
Food Name: {detected_food}

Confidence:
Not available

Food Type:
Unknown

Safety Suggestion:
Follow food safety guidelines
"""


    else:

        result = f"""
Food Name: {detected_food}

Confidence:
Not available (image not uploaded)

Food Type:
Detected from user input

Safety Suggestion:
Check preparation time before donation
"""


    print(result)


    return {

        **state,

        "vision_result": result,

        "food_name": detected_food

    }