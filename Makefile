bot:
	uvicorn main:app

production:
	gunicorn -k uvicorn.workers.UvicornWorker --workers 4 main:app