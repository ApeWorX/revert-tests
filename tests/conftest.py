import pytest


@pytest.fixture(scope="session")
def owner(accounts):
    return accounts[0]


@pytest.fixture(scope="session")
def AssertRaise(project, owner):
    return owner.deploy(project.AssertRaise)


@pytest.fixture(scope="session")
def BadConversion(project, owner):
    return owner.deploy(project.BadConversion)


@pytest.fixture(scope="session")
def InvalidByteArray(project, owner):
    return owner.deploy(project.InvalidByteArray)


@pytest.fixture(scope="session")
def OutOfBounds(project, owner):
    return owner.deploy(project.OutOfBounds)


@pytest.fixture(scope="session")
def Overflow(project, owner):
    return owner.deploy(project.Overflow)


@pytest.fixture(scope="session")
def ReentryError(project, owner):
    return owner.deploy(project.ReentryError)


@pytest.fixture(scope="session")
def ZeroDivision(project, owner):
    return owner.deploy(project.ZeroDivision)
