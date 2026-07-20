from PIL import Image
from transformers import pipeline

from agents.state import FoodDonationState

print("Loading Food Recognition Model...")

classifier = pipeline(
    "image-classification",
    model="nateraw/food"
)

print("Food Vision Model Loaded Successfully 🚀")


def analyze_food_image(image_path):

    image = Image.open(image_path).convert("RGB")

    predictions = classifier(image)

    top = predictions[0]

    food = top["label"].replace("_", " ").title()
    confidence = round(top["score"] * 100, 2)

    result = f"""
Food Name: {food}
Confidence: {confidence}%

Food Type: Detected from image

Estimated Freshness:
Manual verification required

Safety Suggestion:
Check preparation time before donation
"""

    return result


def vision_node(state: FoodDonationState):

    print("=== Vision AI Agent ===")

    image_path = state.get("image_path", "")

    if image_path:

        print("Analyzing image:", image_path)

        try:

            result = analyze_food_image(image_path)

        except Exception as e:

            print("Vision Error:", e)

            result = f"""
Food Name: {state.get('food_name','Unknown')}

Food Type: Unknown

Estimated Freshness:
Manual verification required

Safety Suggestion:
Follow food safety guidelines
"""

    else:

        result = "No image provided"

    print(result)

    return {
        **state,
        "vision_result": result
    }