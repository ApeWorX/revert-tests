import pytest


@pytest.fixture(scope="session")
def owner(accounts):
    return accounts[0]


@pytest.fixture(scope="session")
def contract(project, owner):
    return owner.deploy(project.Sample)
