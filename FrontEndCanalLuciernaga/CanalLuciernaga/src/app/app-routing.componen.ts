import {NgModule} from '@angular/core';
import {Routes, RouterModule} from '@angular/router';
import {VideoComponent} from './components/video/video.component';
import {MenuComponent} from './components/menu/menu.component';
import {NotFound404Component} from './components/not-found404/not-found404.component';

const routes: Routes = [
    {
        path: 'video', 
        component: VideoComponent,
        data: {
            
            titulo: 'Pagina Principal'
        }
    },
    {
        path:'',
        component: MenuComponent
    },
    {
        path: '**',
        component: NotFound404Component
    }
]

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
})

export class AppRoutingModule{}