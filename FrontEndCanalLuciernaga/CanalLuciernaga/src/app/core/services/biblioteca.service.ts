import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Global } from './global';
import { Observable } from 'rxjs';

@Injectable()
export class BibliotecaService{

    private  url:string;

    constructor(private _http: HttpClient){
        this.url = Global.url;
    }

    getBibliotecaById(IdBiblioteca): Observable<any>{
        return this._http.get(this.url + 'biblioteca/' + IdBiblioteca);
    }

    getBiblioteca(): Observable<any>{
        return this._http.get(this.url + 'biblioteca');
    }
}