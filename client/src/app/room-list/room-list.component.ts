import { Component, OnInit } from '@angular/core';
import { ChatService } from '../_services/chat.service';

import { Room } from '../_models/room';

@Component({
  selector: 'app-room-list',
  templateUrl: './room-list.component.html',
  styleUrls: ['./room-list.component.css']
})
export class RoomListComponent implements OnInit {
  constructor(private chat: ChatService) { }

  ngOnInit() {
    this.chat.getRoomList();
  }

}
