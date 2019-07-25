import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common'

//Servicios
import { 
    VideoTecaService,  
    CategoriaVideoTecaService,
    TipoVideoTecaService,
    SerieService,
    ProgramacionService,
    PaisService,
    NoticiaService,
    ClasificacionNoticiaService,
    CategoriaBibliotecaService,
    CategoriaNoticiaService,
    BibliotecaService,
 
} from './service.index';

@NgModule({
    imports: [ CommonModule],
    providers: [
        VideoTecaService,
        CategoriaVideoTecaService,
        TipoVideoTecaService,
        SerieService,
        ProgramacionService,
        PaisService,
        NoticiaService,
        ClasificacionNoticiaService,
        CategoriaBibliotecaService,
        CategoriaNoticiaService,
        BibliotecaService,
            
    ]
})
export class CoreModule{

}