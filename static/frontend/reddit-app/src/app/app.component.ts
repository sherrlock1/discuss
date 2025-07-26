import { AfterContentChecked, Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { UserService } from './core/services/user/user.service';
import { StorageHandlerService } from './core/services/storage/storage-handler.service';
import { CookieService } from 'ngx-cookie-service';
import { User } from './core/models/user.model';
import { environment } from '@reddit/env/environment';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { DatePipe } from '@angular/common';
import { debounceTime, distinctUntilChanged } from "rxjs/operators";
import { MatDialog } from '@angular/material/dialog';
import { CreateGroupComponent } from './group/create-group/create-group.component';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit, AfterContentChecked {
  title = 'reddit';
  path: string;
  authRoute: boolean = false;
  user: User;
  value = 'Search';
  searchField: FormGroup;
  currentTime: string;

  constructor(
    private router: Router,
    private userService: UserService,
    private cookieService: CookieService,
    private storage: StorageHandlerService,
    private dialog: MatDialog,
    private http: HttpClient
  ) {
    this.router.events.subscribe(
      () => this.path = this.router.url
    );
    this.path = this.router.url;
  }

  ngOnInit(): void {
    console.log('AppComponent ngOnInit called');
    this.currentTime = new Date().toLocaleTimeString();
    this.searchField = new FormGroup({
      search: new FormControl('')
    });
    
    // Test API connectivity
    this.testApiConnectivity();
    
    // Add error handling to prevent initialization issues
    try {
      this.userService.fetchUser((user) => {
        console.log('User fetched:', user);
        this.user = user;
      });
    } catch (error) {
      console.error('Error fetching user:', error);
      this.user = null;
    }
  }

  testApiConnectivity(): void {
    console.log('Testing API connectivity...');
    // Test a simple GET request to see if the API is reachable
    this.http.get('https://work-1-otvuwyhcdtyibpym.prod-runtime.all-hands.dev/api/v1/posts/').subscribe(
      (response) => {
        console.log('✅ API connectivity test successful:', response);
      },
      (error) => {
        console.error('❌ API connectivity test failed:', error);
      }
    );
  }

  ngAfterContentChecked(): void {
    if (this.path.includes('/sign-in')
      || this.path.includes('/sign-up')
      || this.path.includes('logout')) {
        this.authRoute = true;
    } else {
      this.authRoute = false;
    }
  }

  logout() {
    console.log('Logout button clicked');
    this.userService.logout().subscribe(
      (response: any) => {
        console.log('Logout response:', response);
        if(response){
          this.storage.removeItem('user');
          window.location.href = `${environment.loginUrl}`;
        }
      },
      (error) => {
        console.log('Logout error:', error);
      });
  }

  createGroup() {
    console.log('Create group button clicked');
    const dialogRef = this.dialog.open(CreateGroupComponent, {
      data: {
        user: this.user,
      },
      width: '600px',
      minHeight: '300px'
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log(`Dialog result: ${result}`);
    });
  }
  search() {
    console.log('Search button clicked');
    this.router.navigate(['search'], {
      queryParams: {
        query: this.searchField.value.search,
      },
    });
    this.searchField.reset();
  }
}
