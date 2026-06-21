from fastapi import FastAPI, UploadFile, File
from torchvision import transforms, models
import torch
import torch.nn as nn
from PIL import Image
import json

app = FastAPI()

DEVICE = torch.device("cpu")

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])


CROPS = ["Potato", "Tomato"]

crop_model = models.resnet18(weights=None)
crop_model.fc = nn.Linear(crop_model.fc.in_features, len(CROPS))
crop_model.load_state_dict(
    torch.load("models/crop_classifier.pth", map_location=DEVICE)
)
crop_model.eval()


TOMATO_DISEASES = ["Early_Blight", "Healthy", "Late_Blight"]

tomato_model = models.resnet18(weights=None)
tomato_model.fc = nn.Linear(tomato_model.fc.in_features, len(TOMATO_DISEASES))
tomato_model.load_state_dict(
    torch.load("models/tomato_disease.pth", map_location=DEVICE)
)
tomato_model.eval()


POTATO_DISEASES = ["Early_Blight", "Healthy", "Late_Blight"]

potato_model = models.resnet18(weights=None)
potato_model.fc = nn.Linear(potato_model.fc.in_features, len(POTATO_DISEASES))
potato_model.load_state_dict(
    torch.load("models/potato_disease.pth", map_location=DEVICE)
)
potato_model.eval()


@app.post("/predict")
async def predict(image: UploadFile = File(...)):
    img = Image.open(image.file).convert("RGB")
    tensor = transform(img).unsqueeze(0)

    
    with torch.no_grad():
        crop_idx = torch.argmax(crop_model(tensor)).item()
    crop = CROPS[crop_idx]

    
    # Tomato Prediction
    
    if crop == "Tomato":
        with torch.no_grad():
            disease_idx = torch.argmax(tomato_model(tensor)).item()
        disease = TOMATO_DISEASES[disease_idx]

        with open("knowledge_base/tomato.json", "r") as f:
            knowledge = json.load(f)

        return {
            "crop": crop,
            "disease": disease,
            "details": knowledge.get(disease, {})
        }

    
    # Potato Prediction
    
    if crop == "Potato":
        with torch.no_grad():
            disease_idx = torch.argmax(potato_model(tensor)).item()
        disease = POTATO_DISEASES[disease_idx]

        with open("knowledge_base/potato.json", "r") as f:
            knowledge = json.load(f)

        return {
            "crop": crop,
            "disease": disease,
            "details": knowledge.get(disease, {})
        }
    return {
        "crop": crop,
        "message": "Disease detection not available for this crop"
    }