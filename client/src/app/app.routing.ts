import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from './login/login.component';

const appRoute: Routes = [
  { path: '', redirectTo: 'login', pathMatch: 'prefix' },
  { path: 'login', component: LoginComponent },

  { path: '**', redirectTo: '' }
];

export const routing = RouterModule.forRoot(appRoute);
