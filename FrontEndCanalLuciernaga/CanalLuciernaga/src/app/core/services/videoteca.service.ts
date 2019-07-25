import { Injectable } from '@angular/core';
import { Global } from './Global';
import { HttpClient } from '@angular/common/http';
import {Observable, throwError} from 'rxjs';
import { retry, catchError } from 'rxjs/operators';
import { VideoTeca } from '../../models/VideoTeca';

@Injectable({
    providedIn: 'root',
})
export class VideoTecaService{

    public url: string;
    
    constructor(private _http: HttpClient){
        this.url = "http://127.0.0.1:8000/api/v1/";
    }

    getVideoTeca(IdVideoTeca): Observable<any>{
        return this._http.get(this.url + 'videoteca/'+ IdVideoTeca);
    }

    getVideoTecas():Observable<any>{
        return this._http.get(this.url + 'videoteca')
    
    }

}