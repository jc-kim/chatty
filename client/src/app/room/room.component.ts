import { Component, Input, OnInit } from '@angular/core';
import { Room } from '../_models/room';
import { ChatService } from '../_services/chat.service';

@Component({
  selector: 'app-room',
  templateUrl: './room.component.html',
  styleUrls: ['./room.component.css']
})
export class RoomComponent implements OnInit {
  @Input() room: Room;

  constructor(private chat: ChatService) { }

  ngOnInit() {
  }

  select() {
    this.chat.changeRoom(this.room);
  }
}
