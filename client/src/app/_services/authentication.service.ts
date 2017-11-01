import { Injectable } from '@angular/core';
import { Http, Headers, Response } from '@angular/http';
import { AppSetting } from '../app.settings';
import 'rxjs/add/operator/map';

@Injectable()
export class AuthenticationService {

  constructor(private http: Http) { }

  login(username: string, password: string) {
    return this.http.post(`${AppSetting.API_ENDPOINT}/user/login`, {
      'username': username,
      'password': password
    }).map((response: Response) => {
      const res = response.json();
      if (res && res.access_token) {
        localStorage.setItem('access_token', res.access_token);
        localStorage.setItem('username', res.username);
        localStorage.setItem('nickname', res.nickname);
      }
    });
  }

  logout() {
    localStorage.removeItem('access_token');
  }

  register(username: string, password: string, nickname: string) {
    const headers = new Headers({
      'Content-Type': 'application/x-www-form-urlencoded'
    });
    return this.http.post(`${AppSetting.API_ENDPOINT}/user/register`,
      `username=${username}&password=${password}&nickname=${nickname}`, {
      headers: headers
    });
  }
}
