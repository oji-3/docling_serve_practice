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



# 結果jsonの構造
```
{
  "schema_name": "string",          // スキーマ名
  "version": "string",              // バージョン
  "name": "string",                 // ドキュメント名
  "origin": {                       // 元ファイル情報
    "mimetype": "string",
    "binary_hash": number,
    "filename": "string",
    "uri": "string|null"
  },
  "furniture": {                    // ドキュメント構造ツリーのルートノード
    "self_ref": "string",
    "parent": null,
    "children": [ /* ノード配列 */ ],
    "content_layer": "string",
    "name": "string",
    "label": "string"
  },
  "body": {                         // 本文に相当する構造ツリー
    "self_ref": "string",
    "parent": null,
    "children": [ /* ノード配列 */ ],
    "content_layer": "string",
    "name": "string",
    "label": "string"
  },
  "groups": [ /* グルーピング情報（空配列の場合も）*/ ],
  "texts": [                        // テキスト要素の配列
    {
      "self_ref": "string",
      "parent": { /* 親ノード情報 */ },
      "children": [ /* 子ノード */ ],
      "content_layer": "string",
      "label": "string",
      "prov": [                     // 各テキストの所在位置など
        {
          "page_no": number,
          "bbox": {
            "l": number,
            "t": number,
            "r": number,
            "b": number,
            "coord_origin": "string"
          },
          "charspan": [start, end]
        },
        …
      ],
      "orig": "string",            // 元のテキスト（フォーマット込み）
      "text": "string",            // プレーンテキスト
      "formatting": {…}|null,
      "hyperlink": {…}|null
    },
    …
  ],
  "pictures": [                     // 画像要素の配列
    {
      "self_ref": "string",
      "parent": {…},
      "children": [ … ],
      "content_layer": "string",
      "label": "string",
      "prov": [                    // 画像の所在ページや座標
        {
          "page_no": number,
          "bbox": { … },
          "charspan": […]
        },
        …
      ],
      "captions": [ … ],          // キャプション要素の参照等
      "references": [ … ],
      "footnotes": [ … ],
      "image": "base64文字列"|null, // 画像そのもの（base64）または null
      "annotations": [ … ]
    },
    …
  ],
  "tables":    [ /* テーブル要素リスト */ ],
  "key_value_items": [ /* キー・バリュー抽出 */ ],
  "form_items":      [ /* フォーム要素抽出 */ ],
  "pages": {                        // ページごとのメタデータ
    "1": {
      "size": {                     // ページサイズ（ポイント単位）
        "width": number,
        "height": number
      },
      "image": {                    // ページ画像（PDFレンダリングなど）
        "mimetype": "string",       // 例: "image/png"
        "dpi": number,              // 解像度
        "size": {                   // 画像ピクセル寸法
          "width": number,
          "height": number
        },
        "uri": "data:image/...;base64,……" // base64 Data URI
      },
      "page_no": number             // ページ番号
    },
    "2": { … },
    …
  }
}
```