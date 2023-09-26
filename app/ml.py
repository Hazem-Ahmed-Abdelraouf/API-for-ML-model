import torch
from PIL import Image
import torchvision.transforms as T

# image preprocessing transformations
tfms = T.Compose([
    T.Resize((224, 224)),
    T.ToTensor()
])
model = torch.load('resnet18-pets.pth',
                   map_location=torch.device('cpu')).eval()
categories = ['Dog', 'Cat']


def classify(img: Image) -> dict:
    """
    Classify the image into dog or cat and assigns the probabilities.
    params:
        img: image to predict on.
    returns:
        dictionary with keys as class names and values as the probabilities
    """
    img = tfms(img).unsqueeze(0)
    with torch.no_grad():
        preds = model(img).softmax(dim=1).squeeze()
    return dict(zip(categories, map(float, preds)))
