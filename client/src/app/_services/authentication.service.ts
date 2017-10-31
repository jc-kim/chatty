import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';
import 'rxjs/add/operator/map';

@Injectable()
export class AuthenticationService {

  constructor(private http: Http) { }

  login(username: string, password: string) {
    return this.http.post('/user/login', JSON.stringify({
      'username': username,
      'password': password
    })).map((response: Response) => {
      const res = response.json();
      if (res && res.access_token) {
        localStorage.setItem('access_token', res.access_token);
      }
    });
  }

  logout() {
    localStorage.removeItem('access_token');
  }

  register(username: string, password: string, nickname: string) {
    return this.http.post('/user/register', JSON.stringify({
      'username': username,
      'password': password,
      'nickname': nickname
    }));
  }
}
