# DoclingDocument JSON構造解説

## 概要
このJSONファイルは `DoclingDocument` というスキーマに基づくPDF解析結果で、日本語コンテンツが含まれています。バージョン1.4.0のスキーマを使用しており、PDFドキュメントの内容を構造化されたデータとして表現しています。

## ルートレベル構造

### 基本メタデータ
```json
{
  "schema_name": "DoclingDocument",
  "version": "1.4.0", 
  "name": "81494_223002_misc",
  "origin": {
    "mimetype": "application/pdf",
    "binary_hash": 13865287516323724997,
    "filename": "81494_223002_misc.pdf",
    "uri": null
  }
}
```

- **schema_name**: ドキュメントスキーマの名称
- **version**: スキーマのバージョン
- **name**: ドキュメント名
- **origin**: 元ファイルの情報（MIMEタイプ、ハッシュ値、ファイル名）

### 主要セクション構造

#### 1. furniture（ファニチャー）
```json
"furniture": {
  "self_ref": "#/furniture",
  "parent": null,
  "children": [],
  "content_layer": "furniture",
  "name": "_root_",
  "label": "unspecified"
}
```
ドキュメントの装飾要素や構造的な部分を表す。現在は空の状態。

#### 2. body（本文）
```json
"body": {
  "self_ref": "#/body",
  "parent": null,
  "children": [
    {"$ref": "#/texts/0"},
    {"$ref": "#/pictures/0"},
    ...
  ],
  "content_layer": "body",
  "name": "_root_",
  "label": "unspecified"
}
```
ドキュメントのメインコンテンツを表す。テキストと画像への参照を子要素として持つ。

#### 3. groups（グループ）
```json
"groups": []
```
要素のグループ化情報。現在は空配列。

#### 4. texts（テキスト要素）
テキスト要素の配列。各要素の構造：
```json
{
  "self_ref": "#/texts/0",
  "parent": {"$ref": "#/body"},
  "children": [],
  "content_layer": "body",
  "label": "text",
  "prov": [
    {
      "page_no": 1,
      "bbox": {
        "l": 43.333333333333336,
        "t": 677.8400268554688,
        "r": 398.0,
        "b": 661.1733601888021,
        "coord_origin": "BOTTOMLEFT"
      },
      "charspan": [0, 31]
    }
  ],
  "orig": "わかりやすく伝えるために「食育ピクトグラム」を作成しました",
  "text": "わかりやすく伝えるために「食育ピクトグラム」を作成しました",
  "formatting": null,
  "hyperlink": null
}
```

##### テキスト要素の詳細プロパティ
- **self_ref**: 自己参照パス
- **parent**: 親要素への参照
- **label**: 要素タイプ（"text"）
- **prov**: プロバナンス情報（位置情報）
  - **page_no**: ページ番号
  - **bbox**: バウンディングボックス（位置座標）
    - **l**: 左端座標
    - **t**: 上端座標
    - **r**: 右端座標
    - **b**: 下端座標
    - **coord_origin**: 座標系の原点（"BOTTOMLEFT"）
  - **charspan**: 文字の範囲
- **orig**: 元のテキスト内容
- **text**: 処理後のテキスト内容
- **formatting**: フォーマット情報（現在はnull）
- **hyperlink**: ハイパーリンク情報（現在はnull）

#### 5. pictures（画像要素）
画像要素の配列。各要素の構造：
```json
{
  "self_ref": "#/pictures/0",
  "parent": {"$ref": "#/body"},
  "children": [],
  "content_layer": "body",
  "label": "picture",
  "prov": [
    {
      "page_no": 1,
      "bbox": {
        "l": 44.24418640136719,
        "t": 610.6952362060547,
        "r": 137.68173217773438,
        "b": 518.3146209716797,
        "coord_origin": "BOTTOMLEFT"
      },
      "charspan": [0, 0]
    }
  ],
  "captions": [],
  "references": [],
  "footnotes": [],
  "image": null,
  "annotations": []
}
```

##### 画像要素の詳細プロパティ
- **label**: 要素タイプ（"picture"）
- **captions**: キャプション配列
- **references**: 参照配列
- **footnotes**: 脚注配列
- **image**: 画像データ（現在はnull）
- **annotations**: 注釈配列

#### 6. tables（テーブル）
```json
"tables": []
```
テーブル要素の配列。現在は空。

#### 7. key_value_items（キー・バリューアイテム）
```json
"key_value_items": []
```
キー・バリューペアの配列。現在は空。

#### 8. form_items（フォームアイテム）
```json
"form_items": []
```
フォーム要素の配列。現在は空。

#### 9. pages（ページ情報）
```json
"pages": {
  "1": {
    "size": {
      "width": 595.3200073242188,
      "height": 759.8400268554688
    },
    "image": {
      "mimetype": "image/png",
      "dpi": 144,
      "size": {
        "width": 1191.0,
        "height": 1520.0
      },
      "uri": "data:image/png;base64,..."
    }
  }
}
```

##### ページ情報の詳細
- **size**: ページサイズ（ポイント単位）
- **image**: ページ画像情報
  - **mimetype**: 画像のMIMEタイプ
  - **dpi**: 解像度
  - **size**: 画像サイズ（ピクセル単位）
  - **uri**: Base64エンコードされた画像データ

## 座標系について
- 座標原点は左下（BOTTOMLEFT）
- 座標はポイント単位
- バウンディングボックスは要素の位置と大きさを示す

## 参照システム
JSONPath形式の参照（`#/texts/0`など）を使用して要素間の関係を表現。親子関係や構造的な関連性を維持。

## データ特徴
- 日本語テキストを含む食育関連のドキュメント
- 複数の画像要素（12個の画像参照）
- テキストと画像が混在したレイアウト
- ページ画像がBase64形式で埋め込まれている