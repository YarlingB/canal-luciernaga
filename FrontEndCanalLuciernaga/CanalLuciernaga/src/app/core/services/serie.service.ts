import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Global } from './global';
import { Observable } from 'rxjs';

@Injectable()
export class SerieService{

    private url:string;

    constructor(private _http: HttpClient){
        this.url = Global.url;
    }

    getSerieById(IdSerie): Observable<any>{
        return this._http.get(this.url + 'episodio/' + IdSerie);
    }

    getSeries(): Observable<any>{
        return this._http.get(this.url + 'episodio');
    }
}