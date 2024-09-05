bot:
	uvicorn main:app

stop:
    pkill -f "uvicorn"

production:
	gunicorn --workers 4 main:app