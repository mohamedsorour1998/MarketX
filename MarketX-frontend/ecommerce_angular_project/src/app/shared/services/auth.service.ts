// auth.service.ts
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';
import { tap, switchMap } from 'rxjs/operators';
import { User } from '../models/user.model';
import { JwtHelperService } from '@auth0/angular-jwt';

interface AuthResponse {
  access: string;
  refresh: string;
}

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  private readonly API_URL = 'https://your-api.example.com/token/';
  private readonly API_URL_CREATE_USER =
    'http://34.171.161.166:8000/my_ecommerce_api/users/';
  private access: string | null = null;
  private refresh: string | null = null;
  private userSubject = new BehaviorSubject<User | null>(null);
  public user$ = this.userSubject.asObservable();
  private jwtHelper = new JwtHelperService();

  constructor(private http: HttpClient) {
    const userData = JSON.parse(localStorage.getItem('user') || 'null');
    if (userData) {
      this.userSubject.next(userData);
    }
  }
  /*When the user submits the login form,
  the login method in the AuthService is called with the user's entered username and password.
  The login method sends a POST request to the server with the provided username and password.
  If the server verifies that the submitted credentials are correct,
  it will generate and return a JWT access token and a refresh token.
  The AuthService will then call the handleAuthResponse method,
  which stores the tokens and decodes the user data from the access token.
  The user data will be stored locally and set in the userSubject BehaviorSubject.
  If the server determines that the submitted credentials are incorrect,
  it should return an error response (e.g., with a 401 Unauthorized status).
  In this case, the AuthService will not call the handleAuthResponse method,
  and the user will not be authenticated.*/
  login(email: string, password: string): Observable<AuthResponse> {
    return this.http.post<AuthResponse>(this.API_URL, { email, password }).pipe(
      tap((response) => {
        this.handleAuthResponse(response);
      })
    );
  }

  register(user: User): Observable<any> {
    return this.http.post(this.API_URL_CREATE_USER, user);
  }

  refreshToken(): Observable<{ access: string }> {
    return this.http
      .post<{ access: string }>(`${this.API_URL}refresh/`, {
        refresh: this.refresh,
      })
      .pipe(
        tap((response) => {
          this.access = response.access;
        })
      );
  }

  private handleAuthResponse(response: AuthResponse): void {
    this.access = response.access;
    this.refresh = response.refresh;
    this.getUserDataFromToken(response.access);
  }

  private getUserDataFromToken(token: string): void {
    const decodedToken: any = this.jwtHelper.decodeToken(token);

    const userData: User = {
      id: decodedToken.user_id,
      first_name: decodedToken.first_name,
      last_name: decodedToken.last_name,
      email: decodedToken.email,
      password: undefined,
      phone: decodedToken.phone,
      address: decodedToken.address,
      city: decodedToken.city,
      state: decodedToken.state,
      zip_code: decodedToken.zip_code,
      country: decodedToken.country,
      date_joined: new Date(decodedToken.date_joined),
      last_login: new Date(decodedToken.last_login),
      is_staff: decodedToken.is_staff,
    };

    this.userSubject.next(userData);
    localStorage.setItem('user', JSON.stringify(userData));
  }

  logout(): void {
    this.access = null;
    this.refresh = null;
    this.userSubject.next(null);
    localStorage.removeItem('user');
  }

  getAccessToken(): string | null {
    return this.access;
  }

  isAuthenticated(): boolean {
    return this.access != null;
  }
}
