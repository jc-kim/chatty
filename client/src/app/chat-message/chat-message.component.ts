import { Component, OnInit, Input } from '@angular/core';
import { Chat } from '../_models/chat';
@Component({
  selector: 'app-chat-message',
  templateUrl: './chat-message.component.html',
  styleUrls: ['./chat-message.component.css']
})
export class ChatMessageComponent implements OnInit {
  @Input() chat: Chat;
  @Input() isMine: boolean;

  constructor() { }

  ngOnInit() {
  }

}
