import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Product } from '../models/product.model';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ProductService {
  private baseUrl = 'http://35.239.65.151:8000/my_ecommerce_api/products/';
  products: Product[] = [];

  // Add BehaviorSubject to store the products
  private productsSource = new BehaviorSubject<Product[]>([]);
  productsSubject = this.productsSource.asObservable();

  constructor(private http: HttpClient) {}
  setProducts(products: Product[]): void {
    this.productsSource.next(products);
  }
  getProducts(): Observable<Product[]> {
    return this.http.get<Product[]>(this.baseUrl);
  }

  getProduct(id: number): Observable<Product> {
    return this.http.get<Product>(`${this.baseUrl}${id}/`);
  }
  filterProducts(category: any = ''): Observable<Product[]> {
    return this.http.get<Product[]>(`${this.baseUrl}?category=${category}`);
  }

  searchProducts(keyword = ''): Observable<Product[]> {
    return this.http.get<Product[]>(`${this.baseUrl}search/?search=${keyword}`);
  }
}
