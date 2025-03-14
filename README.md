# mlops-deployment

- `api/`: Contains the FastAPI application for serving the model.
  - `app.py`: The FastAPI application code.
  - `requirements.txt`: Dependencies for the FastAPI application.
- `model/`: Contains the model training code and the trained model.
  - `model.pkl`: The trained model file.
  - `requirements.txt`: Dependencies for the model training code.
  - `train.py`: The script to train the model.
- `README.md`: Project documentation.

## Setup

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install dependencies for the FastAPI application:
    ```sh
    cd api
    pip install -r requirements.txt
    ```

3. Install dependencies for the model training:
    ```sh
    cd ../model
    pip install -r requirements.txt
    ```

## Training the Model

To train the model, run the following command:
```sh
python model/train.py
```
Once trained it genrated model.pkl file

To start the FastAPI application, run the following command:
```sh
uvicorn api.app:app --host 0.0.0.0 --port 8000
```

Test:
You can test by running test.py
Or
By using swagger UI by visiting  http://localhost:8000/docs
Sample Input:
```python
{
    "MedInc": 3.2,
    "HouseAge": 20.0,
    "AveRooms": 5.4,
    "AveBedrms": 1.2,
    "Population": 1200.0,
    "AveOccup": 2.5,
    "Latitude": 37.0,
    "Longitude": -122.0
}
```