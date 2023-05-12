import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CategoryListComponent } from './category-list/category-list.component';
import { FormsModule } from '@angular/forms';
import { RouterModule, Routes } from '@angular/router';

@NgModule({
  declarations: [CategoryListComponent],
  imports: [CommonModule, RouterModule, FormsModule],
  exports: [CategoryListComponent],
})
export class CategoriesModule {}
