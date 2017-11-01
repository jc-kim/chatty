import { Component, OnInit } from '@angular/core';
import { ChatService } from '../_services/chat.service';

@Component({
  selector: 'app-add-message-box',
  templateUrl: './add-message-box.component.html',
  styleUrls: ['./add-message-box.component.css']
})
export class AddMessageBoxComponent implements OnInit {
  message: string;
  constructor(private chat: ChatService) { }

  ngOnInit() {
  }

  submit() {
    if (this.message) {
      this.chat.addChat(this.message);
      this.message = '';
    }
  }
}
