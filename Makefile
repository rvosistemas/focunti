test_coverage_api_rest_postgres:
	@echo "Running tests with coverage..."
	@coverage run --source=rest_postgres manage.py test
	@coverage report -m
	@coverage html
	@echo "Done."

clean_pycache:
	@echo "Cleaning pycache..."
	@find . -name "*.pyc" -exec rm -rf {} \;
	@find . -name "__pycache__" -exec rm -rf {} \;
	@echo "Done."