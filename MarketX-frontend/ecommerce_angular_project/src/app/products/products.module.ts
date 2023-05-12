import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ProductListComponent } from './product-list/product-list.component';
import { ProductCardComponent } from './product-card/product-card.component';
import { RouterModule, Routes } from '@angular/router';
import { FormsModule } from '@angular/forms';

@NgModule({
  declarations: [ProductListComponent, ProductCardComponent],
  imports: [CommonModule, RouterModule, FormsModule],
  exports: [ProductListComponent, ProductCardComponent],
})
export class ProductsModule {}
