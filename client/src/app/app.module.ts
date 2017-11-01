import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { NgModule } from '@angular/core';
import { MatFormFieldModule, MatInputModule, MatButtonModule } from '@angular/material';

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

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    HomeComponent,
    RegisterComponent,
    RoomListComponent,
    RoomComponent,
    ChatWindowComponent,
    ChatMessageComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    FormsModule,
    HttpModule,
    routing,
    MatFormFieldModule,
    MatInputModule,
    MatButtonModule
  ],
  providers: [
    AuthenticationService,
    AuthOnly,
    ChatService,
    SocketService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
