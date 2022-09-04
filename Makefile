venv:
	pyenv install 3.10.5 --skip-existing
	-pyenv uninstall -f cya_venv
	-pyenv virtualenv 3.10.5 cya_venv
	pyenv local cya_venv
	pip install --upgrade pip
	pip install --upgrade pip-tools

lint:
	black .
	isort .

run:
	python main.py

deps-compile:
	pip-compile requirements.in --no-emit-index-url --no-emit-trusted-host

deps-install:
	pip-sync requirements.txt

deps-update:
	pip-compile requirements.in --no-emit-index-url --no-emit-trusted-host
	pip-sync requirements.txt

play:
	python main.py