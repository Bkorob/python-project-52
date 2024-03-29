start:
	python3 -m gunicorn task_manager.asgi:application -k uvicorn.workers.UvicornWorker

lint:
	poetry run flake8 task_manager --exclude migrations	