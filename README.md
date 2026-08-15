# SuperKart Sales Forecast Deployment

Public source repository for the SuperKart low-code AIML project deployment.

## Structure
- `backend/`: Flask API, Dockerfile, requirements, and serialized tuned Random Forest pipeline.
- `frontend/`: Streamlit application and requirements.

## Verified test performance
- R²: 0.9265
- RMSE: 290.0
- MAE: 116.98
- MAPE: 5.17%

## Hugging Face deployment
Create two **public** Hugging Face Spaces:
1. Backend: Docker SDK, upload contents of `backend/`
2. Frontend: Streamlit SDK, upload contents of `frontend/`

Set the frontend environment variable `BACKEND_URL` to the public backend Space URL.
