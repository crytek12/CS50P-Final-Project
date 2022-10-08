from project import genre, runtime, option


def test_genre():
    # Override the Python built-in input method
    input = lambda: "action"
    # Call the function you would like to test (which uses input)
    output = genre()
    assert output == "action"


def test_runtime():
    # Override the Python built-in input method
    input = lambda: "short"
    # Call the function you would like to test (which uses input)
    output = runtime()
    assert output == "short"


def test_option():
    # Override the Python built-in input method
    input = lambda: "series"
    # Call the function you would like to test (which uses input)
    output = option()
    assert output == "series"
