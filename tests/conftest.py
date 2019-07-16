import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--skipslow", action="store_true", default=False, help="skip slow tests"
    )


def pytest_configure(config):
    config.addinivalue_line("markers", "slow: mark test as slow to run")


def pytest_collection_modifyitems(config, items):
    if not config.getoption("--skipslow"):
        # --runslow given in cli: do not skip slow tests
        return
    skip_slow = pytest.mark.skip(reason="--skipslow passed")
    for item in items:
        if "slow" in item.keywords:
            item.add_marker(skip_slow)
