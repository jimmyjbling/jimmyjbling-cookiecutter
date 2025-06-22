import subprocess
import tempfile
from pathlib import Path

from cookiecutter.main import cookiecutter

TEMPLATE_PATH = Path("./")

def test_cookiecutter_template():
    with tempfile.TemporaryDirectory() as tmpdir:
        # Generate a project
        cookiecutter(
            str(TEMPLATE_PATH),
            no_input=True,
            output_dir=tmpdir,
            extra_context={"__repo_name__": "test_project"}
        )
        project_path = Path(tmpdir) / "test_project"
        assert project_path.exists()

        # Check for expected files
        assert (project_path / "pyproject.toml").exists()
        assert (project_path / ".pre-commit-config.yaml").exists()

        # Check Poetry environment setup
        result = subprocess.run(
            ["poetry", "--version"],
            cwd=project_path,
            capture_output=True,
            text=True
        )
        assert result.returncode == 0
        assert "Poetry" in result.stdout

        # Check pre-commit hook installation
        git_hooks = project_path / ".git" / "hooks" / "pre-commit"
        assert git_hooks.exists()

if __name__ == "__main__":
    try:
        test_cookiecutter_template()
        print("Cookiecutter template test passed successfully!")
    except Exception as e:
        subprocess.run(["poetry", "env", "remove", "python"], check=True)
        raise RuntimeError(f"Cookiecutter template test failed: {e}") from e
    subprocess.run(["poetry", "env", "remove", "python"], check=True)
