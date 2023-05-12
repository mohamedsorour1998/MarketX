import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Product } from '../../shared/models/product.model';
import { Category } from '../../shared/models/category.model';
import { ProductService } from '../../shared/services/product.service';
import { CategoryService } from '../../shared/services/category.service';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css'],
})
export class ProductListComponent implements OnInit {
  products: Product[] = [];
  categories: Category[] = [];
  selectedCategory = '';
  searchQuery = '';

  constructor(
    private productService: ProductService,
    private router: Router,
    private route: ActivatedRoute,
    private categoryService: CategoryService
  ) {}

  ngOnInit(): void {
    this.productService.productsSubject.subscribe((products) => {
      this.products = products;
    });
    this.fetchCategories();

    // Fetch products based on the current route
    this.route.queryParams.subscribe((params) => {
      if (params.category) {
        this.selectedCategory = params.category;
        this.filterProducts();
      } else {
        this.fetchAllProducts();
      }
    });
  }

  onSelectProduct(product: Product): void {
    this.router.navigate(['/products', product.id]);
  }

  fetchAllProducts(): void {
    this.productService.getProducts().subscribe((products) => {
      this.productService.setProducts(products);
    });
  }

  fetchCategories(): void {
    this.categoryService.getCategories().subscribe((categories) => {
      this.categories = categories;
    });
  }

  searchProducts(): void {
    this.productService
      .searchProducts(this.searchQuery)
      .subscribe((products) => {
        this.products = products;
      });
  }

  filterProducts(): void {
    if (this.selectedCategory) {
      this.productService
        .filterProducts(this.selectedCategory)
        .subscribe((products) => {
          this.productService.setProducts(products);
        });
    }
  }
}
