TOOL = python manage.py
run:
	@$(TOOL) runserver

migrate:
	@$(TOOL) makemigrations
	@$(TOOL) migrate

test:
	@$(TOOL) test

coverage:
	@coverage manage.py test
	@coverage report
