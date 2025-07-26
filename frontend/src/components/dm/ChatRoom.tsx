import React, { useState } from 'react';
import { ChatMessage } from "./ChatMessage.tsx";
import type { Message } from '../../types/dm'; // TypeScriptの厳密モードでは、型のimportにはtypeを付ける


// ChatRoomコンポーネントのpropsの型定義
interface ChatRoomProps {
    currentUserId: string; // 現在ログインしているユーザーのID
    recipientId: string; // メッセージを送る相手のID
}

export const ChatRoom = ({ currentUserId, recipientId }: ChatRoomProps) => {
    // useState Hook: メッセージ一覧を管理する状態
    const [messages, setMessages] = useState<Message[]>([]);

    // useState Hook: 入力中のメッセージを管理する状態
    const [inputMessage, setInputMessage] = useState<string>('');

    // メッセージ送信関数
    const sendMessage = () => {
        if (inputMessage.trim()){
            const newMessage: Message = {
                id: Date.now().toString(), // 一意のIDを生成
                senderId: currentUserId, // 現在のユーザーID
                receiverId: recipientId, // 受信者のユーザーID
                content: inputMessage, // 入力されたメッセージ内容
                timestamp: new Date(), // 現在の日時を設定
            };
            setMessages(prev => [...prev, newMessage]); // 既存のメッセージに新しいメッセージを追加
            setInputMessage('') // 入力フィールドをクリア
        }
    };

    // Enterキーでメッセージを送信する関数
    const handleKeyPress = (event: React.KeyboardEvent) => {
        if (event.key === 'Enter') {
            sendMessage();
        }
    };

    return (
        <div style={{ height: '400px', display: 'flex', flexDirection: 'column'}}>
            {/* メッセージ一覧を表示 */}
            <div style={{
                flex: 1, // 残りの空間をすべて使用
                overflow: 'auto', // 縦スクロール有効
                padding: '10px',
                border: '1px solid #ccc',
                marginBottom: '10px',
            }}>
                {messages.map((message) => (
                    <ChatMessage
                        key={message.id} // Reactでリスト要素には必須のkey属性
                        message={message}
                        isOwnMessage={message.senderId === currentUserId} // 自分のメッセージかどうかを判定
                    />
                ))}
            </div>

            {/* メッセージ入力フィールド */}
            <div style={{ display: 'flex', gap: '10px'}}>
                <input
                    type="text"
                    value={inputMessage}
                    onChange={(e) => setInputMessage(e.target.value)}  //onChange: 入力値が変わるたびに呼ばれる // e.target.valueで入力値を取得
                    onKeyDown={handleKeyPress}
                    placeholder="メッセージを入力..."
                    style={{ flex: 1, padding: '8px'}}
                />
                <button onClick={sendMessage} style={{ padding: '8px 12px'}}>
                    送信
                </button>
            </div>
        </div>
    );
}