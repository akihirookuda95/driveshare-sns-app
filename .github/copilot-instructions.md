# チャットアプリ開発のための技術学習優先度
## React (優先度順)

**最優先:**
1. **JSX** - コンポーネントの書き方
2. **Function Components** - 関数コンポーネント
3. **useState Hook** - 状態管理
4. **useEffect Hook** - 副作用処理
5. **Props** - コンポーネント間のデータ受け渡し

**次に重要:**
6. **Event Handling** - onClick, onChangeなど
7. **Conditional Rendering** - 条件付きレンダリング
8. **Lists and Keys** - 配列のレンダリング

## TypeScript (優先度順)

**最優先:**
1. **Basic Types** - string, number, boolean, array
2. **Interface** - オブジェクトの型定義
3. **Type Annotations** - 変数・関数の型指定
4. **Optional Properties** - `?` の使い方

**次に重要:**
5. **Union Types** - `string | number`
6. **Generic Types** - `<T>`の基本

## Flask (優先度順)

**最優先:**
1. **Routes** - `@app.route()`の基本
2. **Request/Response** - データの送受信
3. **JSON handling** - `jsonify()`, `request.json`
4. **Flask-SocketIO** - `emit()`, `on()`の基本

**次に重要:**
5. **Error Handling** - エラーレスポンス
6. **CORS** - フロントエンドとの連携

## Socket.IO (優先度順)

**最優先:**
1. **Client Connection** - サーバーへの接続
2. **emit/on** - イベントの送受信
3. **Room概念** - チャットルーム管理

## その他の重要技術

**CSS:**
- **Flexbox** - レイアウト基本
- **Basic Styling** - 色、フォント、余白

**開発環境:**
- **npm/yarn** - パッケージ管理
- **Vite** - 開発サーバー起動


---
# 機能開発手順 (2025/07/27時点)
## 現在完成している機能

### ✅ **完了済み**
1. **基本的なチャットUI**
   - `ChatMessage`コンポーネント：個別メッセージの表示
   - `ChatRoom`コンポーネント：チャットルーム全体の管理
   - メッセージの送信・表示機能（フロントエンドのみ）

2. **型定義**
   - `Message`型：メッセージの構造定義
   - `User`型：ユーザー情報の構造定義

## 今後実装すべき機能（優先度順）

### 🟡 **Phase 1: バックエンド基盤**
1. **Flaskサーバーセットアップ**
   ```python
   # app.py
   from flask import Flask, jsonify, request
   from flask_cors import CORS
   
   app = Flask(__name__)
   CORS(app)
   ```

2. **メッセージ保存API**
   - `POST /api/messages` - メッセージ送信
   - `GET /api/messages/<user_id>/<recipient_id>` - メッセージ履歴取得

### 🟡 **Phase 2: リアルタイム通信**
3. **Socket.IO統合**
   ```typescript
   // フロントエンド
   import { io } from 'socket.io-client';
   const socket = io('http://localhost:5000');
   ```

4. **リアルタイムメッセージ送受信**
   - メッセージの即座な配信
   - 複数ユーザーでの同時チャット

### 🟡 **Phase 3: ユーザー管理**
5. **ユーザーリストコンポーネント**
   ```typescript
   // UserList.tsx
   const UserList = ({ users, onSelectUser }) => {
     // ユーザー一覧表示
   };
   ```

6. **チャット相手選択機能**
   - サイドバーでユーザー選択
   - アクティブなチャット表示

### 🟠 **Phase 4: 機能拡張**
7. **既読機能**
   - メッセージの既読状態管理
   - 既読マークの表示

8. **オンライン状態表示**
   - ユーザーのオンライン/オフライン状態
   - リアルタイム状態更新

### 🔴 **Phase 5: 高度な機能**
9. **メッセージ削除・編集**
   - 送信済みメッセージの削除
   - メッセージ内容の編集

10. **ファイル共有**
    - 画像・ファイルの送信
    - プレビュー機能