import { Chat } from './chat';

export class Room {
  public logs: Chat[] = [];

  constructor(public id: number, public users: string[], public last_log: string, public last_log_at: Date) { }

  addChat(newChat: Chat) {
    this.logs.push(newChat);
    this._sortLog();
  }

  addChatList(newChats: Chat[]) {
    this.logs = this.logs.concat(newChats);
    this._sortLog();
  }

  replaceChatList(newChats: Chat[]) {
    this.logs = newChats;
    this._sortLog();
  }

  _sortLog() {
    this.logs.sort((a, b) => a.created_at > b.created_at ? 1 : -1);
    if (this.logs && this.logs.length >= 1) {
      this.last_log = this.logs[this.logs.length - 1].message;
      this.last_log_at = this.logs[this.logs.length - 1].created_at;
    }
  }
}
