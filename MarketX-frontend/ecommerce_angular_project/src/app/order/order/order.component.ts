import { Component, OnInit, OnDestroy } from '@angular/core';
import { Router } from '@angular/router';
import { Order } from '../../shared/models/order.model';
import { Subscription } from 'rxjs';
import { OrderService } from '../../shared/services/order.service';

@Component({
  selector: 'app-order',
  templateUrl: './order.component.html',
  styleUrls: ['./order.component.css'],
})
export class OrderComponent implements OnInit, OnDestroy {
  order: Order | null = null;
  // orderSubscription is a Subscription that will hold the subscription to the currentOrder$ observable
  orderSubscription: Subscription;

  constructor(private orderService: OrderService, private router: Router) {}

  ngOnInit(): void {
    this.orderSubscription = this.orderService.currentOrder$.subscribe(
      (order) => {
        if (!order) {
          this.router.navigate(['/']);
          return;
        }
        this.order = order;
      }
    );
  }

  ngOnDestroy() {
    this.orderSubscription.unsubscribe();
  }

  checkout() {
    this.router.navigate(['/checkout']);
  }
}
