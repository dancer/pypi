# pypi claimer

check and claim available package names on pypi

## usage

check available names

```bash
uv run --with httpx check.py
```

claim all available names from available.txt

```bash
uv run claim.py
```

## setup

create .env file

```bash
PYPI_TOKEN=your_token_here
```

install dependencies

```bash
uv sync
```

## format

```bash
uv run --with ruff ruff format .
```

---

created by [@nishimiya](https://x.com/nishimiya)
