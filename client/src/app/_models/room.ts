import { Chat } from './chat';

export class Room {
  public id: number;
  public usernames: string[];
  public last_log: string;
  public last_log_at: Date;
  public logs: Chat[] = [];

  addChat(newChat: Chat) {
    this.logs.push(newChat);
    this.logs.sort((a, b) => a.created_at > b.created_at ? 1 : -1);
  }

  addChatList(newChats: Chat[]) {
    this.logs.concat(newChats);
    this.logs.sort((a, b) => a.created_at > b.created_at ? 1 : -1);
  }
}
