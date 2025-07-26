export interface Message {
    id: string;
    senderId: string;
    receiverId: string;
    content: string;
    timestamp: Date;
}

export interface User {
    id: string;
    username: string;
}