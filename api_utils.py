import base64
import requests
import json

def analyze_image_with_llava(image_path):
    with open(image_path, "rb") as f:
        img_b64 = base64.b64encode(f.read()).decode("utf-8")

    payload = {
        "model": "llava",
        "prompt": "Describe this satellite image. Mention land, roads, vegetation, water, buildings any other key insights.",
        "images": [img_b64]
    }

    response = requests.post("http://localhost:11434/api/generate", json=payload, stream=True)

    result = ""
    for line in response.iter_lines():
        if line:
            try:
                data = json.loads(line.decode("utf-8"))
                if "response" in data:
                    result += data["response"]
            except Exception as e:
                continue

    return result or "No response generated."
