import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthenticationService } from '../_services/authentication.service';
import { SocketService } from '../_services/socket.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  model: any = {};
  loading = false;
  constructor(private auth: AuthenticationService,
    private router: Router,
    private socket: SocketService) { }

  ngOnInit() {
    localStorage.removeItem('access_token');
    this.socket.disconnect();
  }

  login() {
    this.auth.login(this.model.username, this.model.password)
      .subscribe(data => {
        this.router.navigate(['/']);
      }, error => {

      });
  }
}
