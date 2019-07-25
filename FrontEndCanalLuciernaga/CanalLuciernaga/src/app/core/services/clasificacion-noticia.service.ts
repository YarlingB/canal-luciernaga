import { Injectable} from '@angular/core';
import { Global } from './global';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable()
export class ClasificacionNoticiaService{

    private url: string;

    constructor(private _http: HttpClient ){
        this.url = Global.url;
    }

    getClasificacionById(IdClasificacion): Observable<any>{
        return this._http.get(this.url + 'clasificacion-noticia/' + IdClasificacion);
    }

    getClasificaciones(): Observable<any>{
        return this._http.get(this.url + 'clasificacion-noticia');
    }
}