import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { NavbarComponent } from './navbar/navbar.component';
import { HomeComponent } from './home/home.component';


@NgModule({
  declarations: [NavbarComponent, HomeComponent, NavbarComponent, HomeComponent],
  imports: [CommonModule,RouterModule],
  exports: [NavbarComponent, HomeComponent, CommonModule, RouterModule],
})
export class SharedModule {}
