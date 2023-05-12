import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './auth/login/login.component';
import { RegisterComponent } from './auth/register/register.component';
import { CategoryListComponent } from './categories/category-list/category-list.component';
import { ProductListComponent } from './products/product-list/product-list.component';
import { ProductCardComponent } from  './products/product-card/product-card.component';
import { UserProfileComponent } from './users/user-profile/user-profile.component';
import { OrderComponent } from './order/order/order.component';
import { HomeComponent } from './shared/home/home.component';

const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'categories', component: CategoryListComponent },
  { path: 'products', component: ProductListComponent },
  { path: 'products/:id', component: ProductCardComponent},
  // add child routes for the products e.g. /products/1/orders
  { path: 'products/:id/orders', component:  OrderComponent},
  {
    path: 'profile',
    component: UserProfileComponent,

  },
  { path: 'login', component: LoginComponent },
  { path: 'register', component: RegisterComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
