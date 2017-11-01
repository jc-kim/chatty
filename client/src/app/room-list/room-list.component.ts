import { Component, OnInit } from '@angular/core';
import { MatDialog, MatDialogRef } from '@angular/material';
import { ChatService } from '../_services/chat.service';
import { NewRoomDialogComponent } from '../new-room-dialog/new-room-dialog.component';

import { Room } from '../_models/room';

@Component({
  selector: 'app-room-list',
  templateUrl: './room-list.component.html',
  styleUrls: ['./room-list.component.css']
})
export class RoomListComponent implements OnInit {
  constructor(private chat: ChatService, private dialog: MatDialog) { }

  ngOnInit() {
    this.chat.getRoomList();
  }

  openNewRoomDialog() {
    const dialogRef = this.dialog.open(NewRoomDialogComponent, {
      width: '30em',
      data: { usernames: '' } // TODO: prepare multi user chat
    });
    dialogRef.afterClosed().subscribe(data => {
      this.chat.makeRoom([data]);
    });
  }
}
