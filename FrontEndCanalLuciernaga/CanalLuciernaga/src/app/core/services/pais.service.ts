import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Global } from './global';
import { Pais } from '../../models/Pais' 
import { Observable } from 'rxjs';

@Injectable()
export class PaisService{
    
    private url: string;

    constructor(private _http:HttpClient){
        this.url = Global.url;
    }

    getPaisById(IdPais): Observable<Pais>{
        return this._http.get<Pais>(this.url + 'pais/' + IdPais);
    }

    getPaises(): Observable<Pais[]>{
        return this._http.get<Pais[]>(this.url + 'pais');
    }
} 