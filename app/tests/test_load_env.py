import os

def test_env_loaded():
    ret = os.getenv("API_KEY", "")
    assert ret is not None, "API_KEY not loaded!"
    print(ret)