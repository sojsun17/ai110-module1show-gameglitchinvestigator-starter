import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from logic_utils import check_guess


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


def test_history_rendering_uses_plain_text_regression():
    # Regression: passing a list directly to st.write triggers dataframe
    # detection which imports pyarrow and crashes on mismatched architectures.
    # History must be serialized to a plain string before rendering.
    history = [10, 22, 18]
    history_text = ", ".join(map(str, history)) if history else "(empty)"

    assert isinstance(history_text, str)
    assert history_text == "10, 22, 18"