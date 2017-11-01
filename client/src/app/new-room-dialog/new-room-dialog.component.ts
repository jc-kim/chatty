import { Component, OnInit, Inject } from '@angular/core';
import { Http, Headers } from '@angular/http';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material';

import { AppSetting } from '../app.settings';

@Component({
  selector: 'app-new-room-dialog',
  templateUrl: './new-room-dialog.component.html',
  styleUrls: ['./new-room-dialog.component.css']
})
export class NewRoomDialogComponent implements OnInit {
  users: any[] = [];

  constructor(private http: Http,
    private dialogRef: MatDialogRef<NewRoomDialogComponent>,
    @Inject(MAT_DIALOG_DATA) public data) { }

  ngOnInit() {
    const token = localStorage.getItem('access_token');
    const headers = new Headers();
    headers.set('Authorization', 'JWT ' + token);
    this.http.get(`${AppSetting.API_ENDPOINT}/user/list`, {
      headers: headers
    }).subscribe(data => {
      this.users = data.json();
    });
  }

  onNoClick() {
    this.dialogRef.close();
  }
}
