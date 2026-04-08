import json

import main as main_module


def test_main_uses_default_output_file(monkeypatch, tmp_path):
    qml_file = tmp_path / "quiz.quiz"
    qml_file.write_text(
        """
<quiz>
    <title> CLI Test Quiz </title>
    <question>
        <text> Is default output used? </text>
        <option correct="true"> Yes </option>
        <option> No </option>
    </question>
</quiz>
""".strip(),
        encoding="utf-8",
    )

    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(
        "sys.argv",
        ["main.py", str(qml_file)],
    )

    main_module.main()

    output_file = tmp_path / "output.json"
    assert output_file.exists()

    parsed = json.loads(output_file.read_text(encoding="utf-8"))
    assert parsed["title"] == "CLI Test Quiz"


def test_main_uses_custom_output_file(monkeypatch, tmp_path):
    qml_file = tmp_path / "quiz.quiz"
    qml_file.write_text(
        """
<quiz>
    <title> Custom Output Quiz </title>
    <question>
        <text> Is custom output used? </text>
        <option correct="true"> Yes </option>
        <option> No </option>
    </question>
</quiz>
""".strip(),
        encoding="utf-8",
    )

    output_file = tmp_path / "custom.json"

    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(
        "sys.argv",
        ["main.py", str(qml_file), str(output_file)],
    )

    main_module.main()

    assert output_file.exists()

    parsed = json.loads(output_file.read_text(encoding="utf-8"))
    assert parsed["title"] == "Custom Output Quiz"
