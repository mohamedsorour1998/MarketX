import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Category } from '../models/category.model';

@Injectable({
  providedIn: 'root',
})
export class CategoryService {
  private readonly API_URL = 'https://your-api.example.com/categories/';

  constructor(private http: HttpClient) {}

  getAllCategories(): Observable<Category[]> {
    return this.http.get<Category[]>(this.API_URL);
  }

  getCategory(categoryId: number): Observable<Category> {
    return this.http.get<Category>(`${this.API_URL}${categoryId}/`);
  }
}
