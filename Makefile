bot:
	uvicorn main:app

production:
	gunicorn --workers 1 main:app --bind 0.0.0.0:8000 --timeout 120 --keep-alive 5 --max-requests 1000 --max-requests-jitter 100

# production:
# 	uvicorn main:app --host 0.0.0.0 --port 8000 --timeout-keep-alive 6