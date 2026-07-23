import torch
from PIL import Image
from transformers import pipeline

from agents.state import FoodDonationState


# Lazy loading: model will load only when image analysis is requested
classifier = None


def get_classifier():

    global classifier

    if classifier is None:

        print("Loading Food Recognition Model...")

        classifier = pipeline(
            "image-classification",
            model="nateraw/food"
        )

        print("Food Vision Model Loaded Successfully 🚀")

    return classifier



def analyze_food_image(image_path):

    classifier = get_classifier()

    image = Image.open(image_path).convert("RGB")

    predictions = classifier(image)

    top = predictions[0]

    food = top["label"].replace("_", " ").title()

    confidence = round(top["score"] * 100, 2)


    result = f"""
Food Name: {food}
Confidence: {confidence}%

Food Type:
Detected from image

Estimated Freshness:
Manual verification required

Safety Suggestion:
Check preparation time before donation
"""


    return result, food





def vision_node(state: FoodDonationState):

    print("=== Vision AI Agent ===")


    image_path = state.get("image_path", "")


    # fallback if image is not uploaded
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

Estimated Freshness:
Manual verification required

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

Estimated Freshness:
Manual verification required

Safety Suggestion:
Check preparation time before donation
"""



    print(result)


    return {

        **state,

        "vision_result": result,

        "food_name": detected_food

    }