bot:
	uvicorn main:app

production:
	gunicorn -k uvicorn.workers.UvicornWorker --workers 1 main:app