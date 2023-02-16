# Maintainer's build notes

```
git commit 
git clean -fdx --dry-run
poetry run swin
tox
bumpver update --patch
poetry publish --build --username $PYPI_USERNAME --password $PYPI_PASSWORD
```

gpg sign soon!

## test:
```
pip uninstall -y riboswitchinator 
python -m pip cache purge

pip install riboswitchinator 

pip install --force-reinstall dist/*.whl
```
