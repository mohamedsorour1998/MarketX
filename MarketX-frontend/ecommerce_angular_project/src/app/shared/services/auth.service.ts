import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { BehaviorSubject } from 'rxjs';
import { tap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  private readonly apiUrl = 'http://127.0.0.1:8000/my_ecommerce_api';
  private loggedIn = new BehaviorSubject<boolean>(false);

  constructor(private http: HttpClient, private router: Router) {
    this.loggedIn.next(!!localStorage.getItem('access_token'));
  }

  register(user: any) {
    return this.http.post(`${this.apiUrl}/register/`, user);
  }

  login(credentials: { email: string; password: string }) {
    return this.http
      .post<{ access: string; refresh: string }>(
        `${this.apiUrl}/token/`,
        credentials
      )
      .pipe(
        tap((response) => {
          localStorage.setItem('access_token', response.access);
          localStorage.setItem('refresh_token', response.refresh);
          this.loggedIn.next(true);
        })
      );
  }

  logout() {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    this.loggedIn.next(false);
    this.router.navigate(['/']);
  }
  private getAccessToken(): string | null {
    return localStorage.getItem('access_token');
  }
  getProfile() {
    const accessToken = this.getAccessToken();
    if (!accessToken) {
      console.error('Access Token not available.');
      return;
    }

    const headers = new HttpHeaders().set(
      'Authorization',
      `Bearer ${accessToken}`
    );

    return this.http.get(`${this.apiUrl}/profile/`, { headers });
  }

  updateProfile(data: any) {
    return this.http.put(`${this.apiUrl}/profile/`, data);
  }

  isLoggedIn() {
    return this.loggedIn.asObservable();
  }
}
