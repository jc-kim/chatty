import { Component, OnInit, AfterViewChecked, Input, ViewChild, ElementRef } from '@angular/core';
import { ChatService } from '../_services/chat.service';

@Component({
  selector: 'app-chat-window',
  templateUrl: './chat-window.component.html',
  styleUrls: ['./chat-window.component.css']
})
export class ChatWindowComponent implements OnInit, AfterViewChecked {
  @Input() nickname: string;
  @ViewChild('chatList') private chatListElem: ElementRef;

  constructor(private chat: ChatService) { }

  ngOnInit() {
    this.scrollToBottom();
  }

  ngAfterViewChecked() {
    this.scrollToBottom();
  }

  scrollToBottom() {
    if (this.chatListElem) {
      this.chatListElem.nativeElement.scrollTop = this.chatListElem.nativeElement.scrollHeight;
    }
  }
}
