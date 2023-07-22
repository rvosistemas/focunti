SOURCE = employment_portal
DJANGO_SETTINGS_MODULE=focunti.settings

test_coverage:
	@echo "Running tests with coverage..."
	@coverage run --source=${SOURCE} manage.py test --settings=$(DJANGO_SETTINGS_MODULE)
	@coverage report -m
	@coverage html
	@echo "Done."

clean_pycache:
	@echo "Cleaning pycache..."
	@find . -name "*.pyc" -exec rm -rf {} \;
	@find . -name "__pycache__" -exec rm -rf {} \;
	@echo "Done."
