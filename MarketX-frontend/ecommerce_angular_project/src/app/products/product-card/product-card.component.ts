import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Product } from '../../shared/models/product.model';
import { ProductService } from '../../shared/services/product.service';
import { AuthService } from '../../shared/services/auth.service';
import { OrderService } from '../../shared/services/order.service';
@Component({
  selector: 'app-product-card',
  templateUrl: './product-card.component.html',
  styleUrls: ['./product-card.component.css'],
})
export class ProductCardComponent implements OnInit {
  product!: Product;
  User_id: number | null;

  constructor(
    private route: ActivatedRoute,
    private productService: ProductService,
    private AuthService: AuthService,
    private orderService: OrderService,
    private router: Router
  ) {}

  ngOnInit(): void {
    const product_id = Number(this.route.snapshot.paramMap.get('id'));
    this.productService.getProduct(product_id).subscribe((product) => {
      this.product = product;
    });
    const userId = this.AuthService.getUserIdFromToken();

    this.User_id = userId;
  }
  buyNow() {
    if (!this.User_id) {
      alert('You are not logged in.');
      this.router.navigate(['/login']);
      return;
    }
    this.orderService.createOrder(this.User_id, this.product.id).subscribe((order) => {
      console.log(order);
      this.orderService.setOrder(order); // Store the order in the shared service
      // adding /order to the current URL as a child route
      this.router.navigate(['orders'], { relativeTo: this.route });
    }
    );






  }
}
