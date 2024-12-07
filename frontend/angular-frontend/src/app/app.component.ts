import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { QueryComponent } from './query/query.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, QueryComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'angular-frontend';
}
