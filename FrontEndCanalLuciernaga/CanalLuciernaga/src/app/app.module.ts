import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { VideoComponent } from './video/video.component';
import { AppRoutingModule } from './app-routing.componen';
import { NotFound404Component } from './not-found404/not-found404.component'

@NgModule({
  declarations: [
    AppComponent,
    VideoComponent,
    NotFound404Component
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
