# Development Setup

How to prepare a local environment and confirm it works. Supported on macOS and Linux.

## Requirements

- **Python 3.12 or newer.** The project pins 3.12 in `Code/.python-version`; uv downloads it automatically if it is not installed.
- **uv** for environments and dependencies.
- **git**

## 1. Install uv

macOS or Linux:

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Or on macOS with Homebrew:

```sh
brew install uv
```

Open a new terminal, then check it works:

```sh
uv --version
```

## 2. Get the code

```sh
git clone https://github.com/DevPYadav/financial-fraud-detection-tool.git
cd financial-fraud-detection-tool/Code
```

All commands below run from the `Code/` folder.

## 3. Install dependencies

```sh
uv sync
```

This creates `Code/.venv` with the right Python version and installs everything in `pyproject.toml` and `uv.lock`.

## 4. Run the tests

- `uv run pytest` - the whole suite
- `uv run pytest tests/test_home.py` - one test file

Setup is complete when `uv run pytest` reports all tests passed.

## Local configuration

Local settings go in a `Code/.env` file. `.env` files are git-ignored and must never be committed. Do not put real credentials in any tracked file.

The settings and an example file are defined in the configuration conventions (issue [#3](https://github.com/DevPYadav/financial-fraud-detection-tool/issues/3), `Code/docs/configuration.md`). No configuration is needed to run the tests.

## Troubleshooting

**Wrong Python version** (for example `requires-python >=3.12` errors)

uv normally fetches the right version. If it fails, install it and re-sync:

```sh
uv python install 3.12
uv sync
```

Check with `uv run python --version`.

**`uv: command not found`**

The installer puts uv in `~/.local/bin`. Open a new terminal, or add it to your PATH:

```sh
export PATH="$HOME/.local/bin:$PATH"
```

Add that line to `~/.zshrc` (macOS) or `~/.bashrc` (Linux) to make it permanent.

**Stale or broken `.venv`** (import errors, missing packages, or the project folder was moved)

Delete the environment and rebuild it:

```sh
rm -rf .venv
uv sync
```

**Slow or failing sync in a OneDrive/Dropbox folder**

Cloud sync can lock files inside `.venv`. Pause syncing during `uv sync`, or exclude `.venv` from sync.
