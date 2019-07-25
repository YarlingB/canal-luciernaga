import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Global } from './global';
import { Observable } from 'rxjs'
@Injectable()
export class TipoVideoTecaService{

    private url: string;

    constructor( private _http: HttpClient){
        this.url = Global.url;
    }

    getTipoVideoTecaById(IdTipoVideoTECA): Observable<any>{
        return this._http.get(this.url + 'tipo-videoteca/'+ IdTipoVideoTECA);
    }

    getTipoVideoTeca(): Observable<any>{
        return this._http.get(this.url + 'tipo-videoteca');
    }

}