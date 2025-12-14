from reprolock.fingerprint import capture_environment

def test_capture_environment():
    env = capture_environment()
    assert "python_version" in env
    assert "hash" in env
