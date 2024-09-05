bot:
	uvicorn main:app

production:
	uvicorn main:app --host 0.0.0.0 --port $PORT --timeout-keep-alive 5