import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Global } from './global';
import { Observable } from 'rxjs';

@Injectable()
export class CategoriaBibliotecaService{

    private url:string;

    constructor(private _http: HttpClient){
        this.url = Global.url;
    }

    getCategoriaBiblioById(IdCategoriaBiblio): Observable<any>{
        return this._http.get(this.url + 'categoria-biblioteca/' + IdCategoriaBiblio);
    }

    getCategoriaBiblio(): Observable<any>{
        return this._http.get(this.url + 'categoria-biblioteca');
    }
}