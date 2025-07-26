import { Message } from '../../types/dm'


interface ChatMessageProps {
    message: Message;
    isOwnMessage: boolean;
}


export const ChatMessage = ({ message, isOwnMessage}: ChatMessageProps) => {
    return (
        <div style={{
            display: 'flex',
            justifyContent: isOwnMessage ? 'flex-end' : 'flex-start',
            marginBottom: '10px',
        }}>
            <div style={{
                background: isOwnMessage ? '#007bff' : '#f1f1f1',
                color: isOwnMessage ? 'white' : 'black',
                padding: '8px 12px',
                borderRadius: '8px',
                maxWidth: '70%',
            }}>
                {message.content}
            </div>
        </div>
    )
}