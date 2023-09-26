Implementation of an api to deploy my trained ResNet18 model in [my past project](https://github.com/Hazem-Ahmed-Abdelraouf/resnet18-from-scratch) using FastAPI and containerizing it with Docker.<br>I have pushed the image on the Docker hub, so you can test the API by pulling it from [here](https://hub.docker.com/r/hazemamn/res18-api) or you can build it locally by:
1. Cloning the GitHub repo.
```git clone https://github.com/Hazem-Ahmed-Abdelraouf/API-for-ML-model.git```
```cd API-for-ML-model```
1. Building and running the image locally
```docker build -t myimage .```
```docker run -d --name mycontainer -p 8000:8000 myimage```
1. Testing the API
go to [https://localhost:8000/docs](https://localhost:8000/docs), you will find insha'Allah the path operations implenented. The main functionality is ```/predict``` where you send a post request with an image and it returns predictions - a nested JSON with keys as class names and values as the probabilities.