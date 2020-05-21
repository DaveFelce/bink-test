# bink-test

## To set up (pipenv)
`pipenv install` to install from Pipfile.lock

Then do `pipenv shell`

## To set up (pip)

`pip install -r requirements.txt` to install from the requirements.txt file

## To run
Get usage with: `python app.py --help`

Then, for example:

`python app.py 1`

Where 1, 2, 3 or 4 correspond to the four test scenarios

## To run tests

(From the project dir) `PYTHONPATH=. pytest`