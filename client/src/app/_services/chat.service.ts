import { Injectable } from '@angular/core';
import { Http } from '@angular/http';
import { Headers } from '@angular/http';
import { Observable } from 'rxjs/Observable';

import { SocketService } from './socket.service';
import { Room } from '../_models/room';
import { Chat } from '../_models/chat';
import { AppSetting } from '../app.settings';

@Injectable()
export class ChatService {
  public rooms: Room[];
  private cur_room: Room;

  constructor(private http: Http, private socket: SocketService) {
  }

  getRoomList() {
    const token = localStorage.getItem('access_token');
    const headers = new Headers();
    headers.set('Authorization', 'JWT ' + token);
    return this.http.get(`${AppSetting.API_ENDPOINT}/room/`, {
      headers: headers
    }).toPromise()
    .then(data => {
      console.log(data.json());
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
      this.cur_room.addChatList(data.json());
    });
  }
}
