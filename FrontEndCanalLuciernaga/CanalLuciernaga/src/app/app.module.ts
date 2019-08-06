import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { VideoComponent } from './components/video/video.component';
import { AppRoutingModule } from './app-routing.componen';
import { NotFound404Component } from './components/not-found404/not-found404.component';
import { CoreModule } from './core/core.module';
import { HttpClientModule } from '@angular/common/http';
import { MenuComponent } from './components/menu/menu.component';
import { BannerComponent } from './components/banner/banner.component';
import { AlertNewsComponent } from './components/alert-news/alert-news.component';
import { ListaReproduccionComponent } from './components/lista-reproduccion/lista-reproduccion.component';

@NgModule({
  declarations: [
    AppComponent,
    VideoComponent,
    NotFound404Component,
    MenuComponent,
    BannerComponent,
    AlertNewsComponent,
    ListaReproduccionComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    CoreModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
