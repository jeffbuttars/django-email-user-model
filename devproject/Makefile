VENV := . .venv/bin/activate
DP := dp
RUNSERVER := runserver
# RUNSERVER := run_tornado
PYPKG := django-email-user-model
PYMOD := django_email_user_model

SERVER_IP = localhost:8000
.PHONY: reset run rundbg clean

RUNDJDBG := cd $(DP); export DJANGO_DEBUG=True; ./manage.py $(RUNSERVER) $(SERVER_IP)
RUNDJ := cd $(DP); export DJANGO_DEBUG=''; ./manage.py collectstatic -l --noinput; ./manage.py $(RUNSERVER)

.PHONY: $(DP)
$(DP):
	if [ ! -d $(DP) ]; then\
		django-admin startproject $(DP);\
	fi;\
	cp -fr settings.py $(DP)/$(DP)/;\
	cd $(DP);\
	./manage.py syncdb;\
	./manage.py migrate;

# Re-install $(PYPKG)
reset:
	-$(VENV); yes y | pip uninstall --exists-action=w $(PYPKG)
	pip install --exists-action=w --pre --no-deps ../src/

resetpkg:
	-$(VENV); \
	dv=$$(cd ../src; python -c "import $(PYMOD); print($(PYMOD).__version__)");\
	yes y | pip uninstall --exists-action=w $(PYPKG);\
	pip install --exists-action=w --pre --no-deps ../src/dist/$(PYMOD)-$$dv.tar.gz

# run in production mode
run: reset $(DP)
	$(RUNDJ)

runpkg: resetpkg $(DP)
	$(RUNDJ)

# run in debug mode
rundbg:  reset $(DP)
	$(RUNDJDBG)

runpkgdbg: resetpkg $(DP)
	$(RUNDJDBG)

clean:
	@find $(DP) -iname '*.pyc' | xargs rm -fv
	@find $(DP) -name '__pycache__' | xargs rm -fvr

realclean: clean
	rm -fr $(DP)
