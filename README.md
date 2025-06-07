https://github.com/docling-project/docling-serve/tree/main?tab=readme-ov-file

# Build
**プロジェクト初期化:**

```bash
uv init
```

**仮想環境の作成:**

```bash
uv venv
```

**特定のPythonバージョンで仮想環境を作成:**

```bash
uv venv --python 3.12
```

**アクティベート**
Linux/macOS:
```
source .venv/bin/activate
```

**ディアクティベート**
```
deactivate
```

**requirements.txtからのインストール:**

```bash
uv pip install -r requirements.txt
```

**インストール済みパッケージの一覧表示:**

```bash
uv pip list
```

# Build One Liner

**プロジェクト初期化（Python 3.12使用）:**

```bash
uv init && uv venv --python 3.12 && source .venv/bin/activate
```


# Run doclind-serve
```
docling-serve run
```
```
docling-serve run --enable-ui
```

API http://127.0.0.1:5001
API documentation http://127.0.0.1:5001/docs
Demonstration UI http://127.0.0.1:5001/ui
