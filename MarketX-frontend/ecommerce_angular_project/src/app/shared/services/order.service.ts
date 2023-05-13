import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';
import { Order } from '../models/order.model';
import { Checkout } from '../models/checkout.model';
@Injectable({
  providedIn: 'root',
})
export class OrderService {
  private apiUrl = 'http://10.52.13.195:8000/my_ecommerce_api';
  // orderSource is a BehaviorSubject that will hold the current order
  // BehaviorSubject is a type of Subject that allows us to set the initial value of the observable
  private orderSource = new BehaviorSubject<Order | null>(null);
  // currentOrder$ is an observable that will be used by the components to subscribe to the current order
  // $ is a naming convention for observables
  currentOrder$ = this.orderSource.asObservable();

  constructor(private http: HttpClient) {}

  createOrder(userId: number, productId: number): Observable<Order> {
    const orderData: Order = {
      id: 0,
      quantity: 1,
      is_complete: true,
      user: userId,
      product: productId,
    };

    return this.http.post<Order>(
      `${this.apiUrl}/users/${userId}/orders/`,
      orderData
    );
  }

  getUserOrders(userId: number): Observable<Order[]> {
    return this.http.get<Order[]>(`${this.apiUrl}/users/${userId}/orders/`);
  }
  setOrder(order: Order): void {
    this.orderSource.next(order);
  }
  getCheckout(userId: number): Observable<Checkout[]> {
    return this.http.get<Checkout[]>(
      `${this.apiUrl}/users/${userId}/orders/checkout/`
    );
  }
}
