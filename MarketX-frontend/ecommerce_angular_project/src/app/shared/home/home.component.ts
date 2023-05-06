import { Component, ViewChild, ElementRef, AfterViewInit } from '@angular/core';
import { Carousel } from 'bootstrap';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
})
export class HomeComponent implements AfterViewInit {
  @ViewChild('carousel') carousel: ElementRef;

  ngAfterViewInit(): void {
    new Carousel(this.carousel.nativeElement);
  }
}
