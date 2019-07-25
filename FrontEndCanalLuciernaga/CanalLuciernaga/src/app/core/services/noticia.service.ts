import { Injectable } from '@angular/core';
import { Global } from './global';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';


@Injectable()
export class NoticiaService{

    private url: string;

    constructor(private _http: HttpClient){
        this.url = Global.url;
    }

    getNoticiaById(IdNoticia): Observable<any>{
        return this._http.get(this.url + 'noticia/' + IdNoticia);
    }


    getNoticias(): Observable<any>{
        return this._http.get(this.url+'');
    }
}