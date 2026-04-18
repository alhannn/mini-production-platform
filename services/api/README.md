# API Service

This service provides the backend API for the Mini Production Platform.

## Current endpoints

- `GET /`
- `GET /health`
- `GET /ready`

## Run locally

bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload