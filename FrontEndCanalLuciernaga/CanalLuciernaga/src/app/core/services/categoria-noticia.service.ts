import { Injectable} from '@angular/core';
import { Global } from './global';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable()
export class CategoriaNoticiaService{

    private url: string;

    constructor(private _http: HttpClient ){
        this.url = Global.url;
    }

    getCategoriaById(IdClasificacion): Observable<any>{
        return this._http.get(this.url + 'categoria-noticia/' + IdClasificacion);
    }

    getCategorias(): Observable<any>{
        return this._http.get(this.url + 'categoria-noticia');
    }
}