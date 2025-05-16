# DriveShareSNS アプリ API設計ドキュメント

このドキュメントは、DriveShareSNS アプリケーションにおける REST API の設計方針と仕様を記述したものです。

---

## 📘 記述フォーマット（テンプレート）

### [HTTPメソッド] /エンドポイント

#### 概要
このAPIが何をするかを簡潔に記述。

#### リクエスト
Content-Type: application/json

```json
{
  "項目1": "値",
  "項目2": "値"
}
```

#### レスポンス（\[HTTPステータスコード]）

```json
{
  "項目1": "値",
  "項目2": "値"
}
```

#### 使用スキーマ

* リクエスト: `スキーマ名`
* レスポンス: `スキーマ名`




## 🧪 実装予定API一覧

### 🔹 ユーザー関連
- POST /users （新規ユーザー登録）
- GET /users/<id> （ユーザー詳細取得）

### 🔹 投稿（Post）関連
- POST /posts （新規投稿）
- GET /posts （投稿一覧取得）
- GET /posts/<id> （投稿詳細）

### 🔹 ルート（Route）関連
- POST /routes （ルート登録）
- GET /posts/<post_id>/routes （投稿に紐づくルート一覧）


## 🧱 実装済み / 設計中 API

### POST /users
#### 概要
新規ユーザーを登録する。

#### リクエスト
Content-Type: application/json
```json
{
"username": "akihiro",
"email": "aki@example.com",
"password": "secret123"
}
```

#### レスポンス（201 Created）

```json
{
  "id": 1,
  "username": "akihiro",
  "email": "aki@example.com",
  "created_at": "2023-10-01T12:00:00Z",
  "updated_at": "2023-10-01T12:00:00Z"
}
```

#### 使用スキーマ
* リクエスト: `UserCreate`
* レスポンス: `UserBase`



### GET /users/<id>
#### 概要
指定したユーザーの詳細情報を取得する。
#### リクエスト
パラメータでユーザーIDを指定。
#### レスポンス(200 OK)
```json
{
  "id": 1,
  "username": "akihiro",
  "email": "aki@example.com",
  "created_at": "2023-10-01T12:00:00Z",
  "updated_at": "2023-10-01T12:00:00Z"
}
```
#### 使用スキーマ
* レスポンス: `UserBase`


### POST /posts
#### 概要
新規投稿を作成する。
#### リクエスト
Content-Type: application/json
```json
{
  "title": "My First Post",
  "content": "This is the content of my first post.",
  "user_id": 1
}
```
#### レスポンス（201 Created）
```json
{
  "id": 1,
  "title": "My First Post",
  "content": "This is the content of my first post.",
  "user_id": 1,
  "created_at": "2023-10-01T12:00:00Z",
  "updated_at": "2023-10-01T12:00:00Z"
}
```
#### 使用スキーマ
* リクエスト: `PostCreate`
* レスポンス: `PostBase`


### GET /posts
#### 概要
全ての投稿を取得する。
#### リクエスト
クエリパラメータでページネーションを指定可能。
#### レスポンス（200 OK）
```json
[
  {
    "id": 1,
    "title": "My First Post",
    "content": "This is the content of my first post.",
    "user_id": 1,
    "created_at": "2023-10-01T12:00:00Z",
    "updated_at": "2023-10-01T12:00:00Z"
  },
  {
    "id": 2,
    "title": "My Second Post",
    "content": "This is the content of my second post.",
    "user_id": 1,
    "created_at": "2023-10-02T12:00:00Z",
    "updated_at": "2023-10-02T12:00:00Z"
  }
]
```
#### 使用スキーマ
* レスポンス: `List[PostBase]`


### GET /posts/<id>
#### 概要
指定した投稿の詳細情報を取得する。
#### リクエスト
パラメータで投稿IDを指定。
#### レスポンス（200 OK）
```json
{
  "id": 1,
  "title": "My First Post",
  "content": "This is the content of my first post.",
  "user_id": 1,
  "created_at": "2023-10-01T12:00:00Z",
  "updated_at": "2023-10-01T12:00:00Z"
}
```
#### 使用スキーマ
* レスポンス: `PostBase`


### POST /routes
#### 概要
新規ルートを登録する。
#### リクエスト
Content-Type: application/json
```json
{
  "post_id": 1,
  "start_location": "Tokyo",
  "end_location": "Osaka",
  "distance": 500,
  "duration": 300
}
```
#### レスポンス（201 Created）
```json
{
  "id": 1,
  "post_id": 1,
  "start_location": "Tokyo",
  "end_location": "Osaka",
  "distance": 500,
  "duration": 300,
  "created_at": "2023-10-01T12:00:00Z",
  "updated_at": "2023-10-01T12:00:00Z"
}
```
#### 使用スキーマ
* リクエスト: `RouteCreate`
* レスポンス: `RouteBase`


### GET /posts/<post_id>/routes
#### 概要
指定した投稿に紐づくルート一覧を取得する。
#### リクエスト
パラメータで投稿IDを指定。
#### レスポンス（200 OK）
```json
[
  {
    "id": 1,
    "post_id": 1,
    "start_location": "Tokyo",
    "end_location": "Osaka",
    "distance": 500,
    "duration": 300,
    "created_at": "2023-10-01T12:00:00Z",
    "updated_at": "2023-10-01T12:00:00Z"
  },
  {
    "id": 2,
    "post_id": 1,
    "start_location": "Kyoto",
    "end_location": "Hiroshima",
    "distance": 300,
    "duration": 180,
    "created_at": "2023-10-02T12:00:00Z",
    "updated_at": "2023-10-02T12:00:00Z"
  }
]
```
#### 使用スキーマ
* レスポンス: `List[RouteBase]`


