TOOL = python manage.py
run:
	@$(TOOL) runserver

migrate:
	@$(TOOL) makemigrations
	@$(TOOL) migrate

test:
	@$(TOOL) test

coverage:
	@coverage run manage.py test
	@coverage report

clean:
	@rm -rf htmlcov */**/**/**/__pycache__/
