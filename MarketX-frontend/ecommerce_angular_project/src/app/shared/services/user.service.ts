import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { User } from '../models/user.model';

@Injectable({
  providedIn: 'root',
})
export class UserService {
  private readonly API_URL_USER_PROFILE =
    'http://10.52.11.103:8000/my_ecommerce_api/profile/';
  // private readonly API_URL_USER_PROFILE = 'http://127.0.0.1:8000/my_ecommerce_api/profile/';

  constructor(private http: HttpClient) {}

  getUserProfile(): Observable<User> {
    const httpOptions = {
      withCredentials: true, // Include cookies in the request
    };

    return this.http.get<User>(this.API_URL_USER_PROFILE, httpOptions);
  }
}
