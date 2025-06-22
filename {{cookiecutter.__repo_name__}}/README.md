# {{cookiecutter.project_name}}

{{cookiecutter.proj_desc}}

## Documentation

This project uses Sphinx for documentation. The documentation is automatically built and published to Read the Docs when a new release is created on GitHub.

### Building Documentation Locally

To build the documentation locally:

```bash
# Install dependencies with documentation extras
poetry install --with docs

# Build the documentation
cd docs
poetry run sphinx-build -b html . _build/html
```

The built documentation will be available in the `docs/_build/html` directory.

### Automatic Documentation Publishing

When a new release is created on GitHub:

1. A GitHub workflow automatically builds the documentation and uploads it as an artifact
2. Read the Docs detects the new release and builds the documentation using the configuration in `.readthedocs.yaml`

### Setting Up Read the Docs Integration

To set up the Read the Docs integration:

1. Go to [Read the Docs](https://readthedocs.org/) and sign in with your GitHub account
2. Import your repository
3. Configure the project settings as needed
4. Read the Docs will automatically build the documentation using the configuration in `.readthedocs.yaml`
