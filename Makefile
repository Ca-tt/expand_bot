bot:
	uvicorn main:app

production:
	gunicorn --workers 4 main:app