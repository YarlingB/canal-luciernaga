import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Global } from './global';
import { Observable } from 'rxjs';

@Injectable()
export class ProgramacionService{

    private url:string;

    constructor(private _http: HttpClient){
        this.url = Global.url;
    }

    getPorgramacionById(IdProgramacion): Observable<any>{
        return this._http.get(this.url + 'programacion/' + IdProgramacion);
    }

    getProgramacion(): Observable<any>{
        return this._http.get(this.url + 'programacion');
    }
}