import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { NgModule, LOCALE_ID } from '@angular/core';
import { MatFormFieldModule, MatInputModule, MatButtonModule, MatDialogModule, MatRadioModule } from '@angular/material';

import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { AuthenticationService } from './_services/authentication.service';
import { ChatService } from './_services/chat.service';
import { SocketService } from './_services/socket.service';
import { routing } from './app.routing';
import { HomeComponent } from './home/home.component';
import { AuthOnly } from './auth';
import { RegisterComponent } from './register/register.component';
import { RoomListComponent } from './room-list/room-list.component';
import { RoomComponent } from './room/room.component';
import { ChatWindowComponent } from './chat-window/chat-window.component';
import { ChatMessageComponent } from './chat-message/chat-message.component';
import { AddMessageBoxComponent } from './add-message-box/add-message-box.component';
import { NewRoomDialogComponent } from './new-room-dialog/new-room-dialog.component';
import { LocalDatePipe } from './_pipes/local-date.pipe';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    HomeComponent,
    RegisterComponent,
    RoomListComponent,
    RoomComponent,
    ChatWindowComponent,
    ChatMessageComponent,
    AddMessageBoxComponent,
    NewRoomDialogComponent,
    LocalDatePipe
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    FormsModule,
    HttpModule,
    routing,
    MatDialogModule,
    MatFormFieldModule,
    MatInputModule,
    MatButtonModule,
    MatRadioModule
  ],
  providers: [
    AuthenticationService,
    AuthOnly,
    ChatService,
    SocketService,
    { provide: LOCALE_ID, useValue: 'ko-KR'}
  ],
  bootstrap: [AppComponent],
  entryComponents: [
    NewRoomDialogComponent
  ]
})
export class AppModule { }
