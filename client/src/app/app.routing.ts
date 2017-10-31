import { Routes, RouterModule } from '@angular/router';

import { LoginComponent } from './login/login.component';
import { HomeComponent } from './home/home.component';
import { RegisterComponent } from './register/register.component';
import { AuthOnly } from './auth';

const appRoute: Routes = [
  { path: '', component: HomeComponent, canActivate: [AuthOnly] },
  { path: 'login', component: LoginComponent },
  { path: 'register', component: RegisterComponent },

  { path: '**', redirectTo: '' }
];

export const routing = RouterModule.forRoot(appRoute);
