
cover:
	make lint
	make cover_tests

lint:
	flake8 --max-line-length=120 tree tests

cover_tests:
	py.test -s  --cov-config .coveragerc --cov tree \
	--no-cov-on-fail \
	--cov-fail-under=80 \
	tests
