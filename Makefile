bot:
	uvicorn main:app

production:
	uvicorn main:app --host 0.0.0.0 --port 10000 --timeout-keep-alive 5