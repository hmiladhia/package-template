import pytest


@pytest.fixture(scope="session")
def default_config() -> dict[str, int | str | bool]:
    return {
        "project_name": "Test Project",
        "project_description": "A fake project to test the copier template",
        "organisation": "fake-org",
        "author": "ME",
    }


def test_template(copie, default_config):
    res = copie.copy(extra_answers=default_config)

    assert res.exit_code == 0
    assert res.exception is None
    assert res.project_dir.is_dir()
