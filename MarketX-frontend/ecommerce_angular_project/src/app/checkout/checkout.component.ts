import { Component, OnInit } from '@angular/core';
import { OrderService } from '../shared/services/order.service';
import { AuthService } from '../shared/services/auth.service';

@Component({
  selector: 'app-checkout',
  templateUrl: './checkout.component.html',
  styleUrls: ['./checkout.component.css'],
})
export class CheckoutComponent implements OnInit {
  constructor(
    private orderService: OrderService,
    private authService: AuthService
  ) {}
  orderDetails: any;
  userId: number | null = this.authService.getUserIdFromToken();

  ngOnInit(): void {
    if (this.userId !== null) {
      this.orderService.getCheckout(this.userId).subscribe((data) => {
        console.log(data);
        this.orderDetails = data;
      });
    }
    console.log(this.orderDetails);
  }
}
