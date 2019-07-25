import { Injectable } from '@angular/core';
import { Global} from './global';
import { HttpClient} from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable()
export class CategoriaVideoTecaService{

    private url: string;

    constructor( private _http: HttpClient){
        this.url = Global.url;
    }

    getCategoriaById(IdCategoria): Observable<any>{
        return this._http.get(this.url + 'categoria-video/' + IdCategoria);
    }

    getCategorias(): Observable<any>{
        return this._http.get(this.url + 'categoria-video');
    }
}