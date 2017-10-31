import { Injectable } from '@angular/core';
import { Http } from '@angular/http';
import { SocketService } from './socket.service';
import { Room } from '../_models/room';
import { Chat } from '../_models/chat';

@Injectable()
export class ChatService {
  private rooms: Room[];
  private cur_room: Room;

  constructor(private http: Http, private socket: SocketService) {
  }
}
