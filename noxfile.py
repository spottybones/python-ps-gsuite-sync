import nox

locations = "ps_gsuite_sync", "tests", "noxfile.py"


@nox.session
def tests(session):
    args = session.posargs or ["--cov"]
    session.run("poetry", "install", external=True)
    session.run("pytest", *args)


@nox.session
def lint(session):
    args = session.posargs or locations
    session.install("flake8")
    session.run("flake8", *args)
