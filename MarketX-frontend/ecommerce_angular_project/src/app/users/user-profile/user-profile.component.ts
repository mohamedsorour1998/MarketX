import { Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/shared/services/auth.service';
import { take } from 'rxjs/operators';


@Component({
  selector: 'app-user-profile',
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.css'],
})
export class UserProfileComponent implements OnInit {
  user: any;

  constructor(private authService: AuthService) {}

  ngOnInit() {
    this.authService
      .isLoggedIn()
      .pipe(take(1))
      .subscribe((loggedIn) => {
        if (loggedIn) {
          this.authService.getProfile()?.subscribe(
            (response: any) => {
              this.user = response;
            },
            (error) => {
              console.error(error);
            }
          );
        }
      });
  }
}
