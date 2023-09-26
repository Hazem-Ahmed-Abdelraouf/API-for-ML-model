from fastapi import FastAPI, UploadFile
from PIL import Image
from ml import classify
app = FastAPI()

@app.get('/')
def root():
    return {'msg':'Server is running.'}

@app.post('/predict/')
def predict(image: UploadFile):
    """Predict if the image passed is a dog or a cat
    params:
        image: uploaded image by user via post method
    returns:
        predictions: a nested dictionary with keys as class names and values as the probabilities
    """
    im_type = image.content_type.split('/')[-1].upper()
    image = Image.open(image.file, formats=[im_type]).convert('RGB')
    predictions = classify(image)
    return {'predictions': predictions} 
    