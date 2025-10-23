from src import calculator

def test_addition(monkeypatch, capsys):
    inputs = iter(["1", "2", "3", "5"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calculator.main()
    captured = capsys.readouterr()
    assert "Result: 5.0" in captured.out
