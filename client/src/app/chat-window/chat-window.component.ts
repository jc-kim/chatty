import { Component, OnInit, Input } from '@angular/core';
import { ChatService } from '../_services/chat.service';

@Component({
  selector: 'app-chat-window',
  templateUrl: './chat-window.component.html',
  styleUrls: ['./chat-window.component.css']
})
export class ChatWindowComponent implements OnInit {
  @Input() nickname: string;

  constructor(private chat: ChatService) { }

  ngOnInit() {
  }

}
