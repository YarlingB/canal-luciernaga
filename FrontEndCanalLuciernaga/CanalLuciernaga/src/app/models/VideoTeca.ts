import {Categoria} from "./Categoria";

export class VideoTeca{

    public id: number;
    public tipo: string;
    public categoria: Categoria[];
    public nombre: string;
    public sinopsis: string;
    public fecha: Date;
    public director: string;
    public produccion: string; 
    public pais: string;
    public duracion: number;
    public url: string;

    constructor(){}
}