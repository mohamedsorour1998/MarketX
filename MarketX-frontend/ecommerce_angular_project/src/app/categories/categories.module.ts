import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CategoryListComponent } from './category-list/category-list.component';

@NgModule({
  declarations: [CategoryListComponent],
  imports: [CommonModule],
  exports: [CategoryListComponent],
})
export class CategoriesModule {}
