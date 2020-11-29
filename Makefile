default: venv docker

run:
	docker-compose up --build

rund:
	docker-compose up -d

ipyshell:
	~/.virtualenvs/kyliecatt.gay/bin/ipython

venv:
	echo "Creating venv ~/.virtualenvs/kyliecatt.gay/kyliecatt.gay"
	python3 -m venv ~/.virtualenvs/kyliecatt.gay
	~/.virtualenvs/kyliecatt.gay/bin/pip install --upgrade pip
	echo "Installing dev dependencies"
	~/.virtualenvs/kyliecatt.gay/bin/pip install -r requirements-dev.txt

docker:
	echo "Building base Docker image (not pushing to remote)"
	./scripts/build_and_push_base_image.sh -v 1.0.0
