import { Injectable } from '@angular/core';
import { Subject } from 'rxjs/Subject';
import { Observable } from 'rxjs/Observable';
import * as io from 'socket.io-client';

import { AppSetting } from '../app.settings';

@Injectable()
export class SocketService {
  private url;
  private socket;

  constructor() {
    this.url = AppSetting.CHAT_ENDPOINT;
  }

  access_token() {
    return localStorage.getItem('access_token');
  }

  send_message(room_id, message) {
    this.socket.emit('send_message', {
      room_id: room_id,
      message: message
    });
  }

  connect() {
    if (!this.access_token()) {
      return;
    }

    const observable = new Observable(observer => {
      this.socket = io(this.url, {
        query: {
          token: this.access_token()
        }
      });
      this.socket.on('receive_message', (data) => {
        observer.next(data);
      });
      return () => {
        this.socket.disconnect();
      }
    });
    return observable;
  }

  disconnect() {
    if (this.socket) {
      this.socket.disconnect();
    }
    this.socket = null;
  }
}
