import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthenticationService } from '../_services/authentication.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
  model: any = {};
  constructor(private auth: AuthenticationService,
  private router: Router ) { }

  ngOnInit() {
  }

  register() {
    this.auth.register(this.model.username, this.model.password, this.model.nickname)
      .subscribe((data) => {
        this.router.navigate(['/login']);
      },
      error => {
        // TODO
      });
  }
}
