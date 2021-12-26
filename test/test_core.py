def test_version():
    from ApiTest import __version__
    assert isinstance(__version__,str)