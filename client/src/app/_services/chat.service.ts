import { Injectable } from '@angular/core';
import { Http, Headers, Response } from '@angular/http';
import { Observable } from 'rxjs/Observable';

import { SocketService } from './socket.service';
import { Room } from '../_models/room';
import { Chat } from '../_models/chat';
import { AppSetting } from '../app.settings';

@Injectable()
export class ChatService {
  public rooms: Room[];
  private cur_room: Room;
  private connection;

  constructor(private http: Http, private socket: SocketService) {
    this.connection = this.socket.connect().subscribe(data => {
      this.cur_room.addChat({
        'username': data['writer']['username'],
        'nickname': data['writer']['nickname'],
        'message': data['message'],
        'created_at': data['created_at']
      });
    });
  }

  getRoomList() {
    const token = localStorage.getItem('access_token');
    const headers = new Headers();
    headers.set('Authorization', 'JWT ' + token);
    return this.http.get(`${AppSetting.API_ENDPOINT}/room/`, {
      headers: headers
    }).toPromise()
    .then(data => {
      this.rooms = data.json().map(r => new Room(r.id, r.users, r.last_log, r.last_log_at));
      return this.rooms;
    });
  }

  changeRoom(room: Room) {
    const token = localStorage.getItem('access_token');
    const headers = new Headers();
    headers.set('Authorization', 'JWT ' + token);
    this.cur_room = room;
    this.http.get(`${AppSetting.API_ENDPOINT}/room/${this.cur_room.id}/logs`, {
      headers: headers
    }).subscribe(data => {
      this.cur_room.replaceChatList(data.json());
    });
  }

  addChat(message: string) {
    this.socket.send_message(this.cur_room.id, message);
    this.rooms.sort((a, b) => a.last_log_at > b.last_log_at ? 1 : -1);
  }

  makeRoom(usernames: string[]) {
    const token = localStorage.getItem('access_token');
    const headers = new Headers();
    headers.set('Authorization', 'JWT ' + token);
    headers.set('Content-Type', 'application/x-www-form-urlencoded')
    return this.http.post(`${AppSetting.API_ENDPOINT}/room/make`,
    `usernames=${usernames}`, {
      headers: headers
    }).map(res => res.json())
    .subscribe(data => {
      const res = data.json();
      this.rooms.unshift(new Room(res['room_id'], res['users'], '', res['created_at']));
      this.changeRoom(this.rooms[0]);
    }, (err: Response) => {
      if (err.status === 301) {
        this.changeRoom(this.rooms.filter(r => r.id === err.json()['room_id'])[0]);
      } else {
        return err;
      }
    });
  }
}
