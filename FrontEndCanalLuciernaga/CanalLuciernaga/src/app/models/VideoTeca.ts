import {Categoria} from "./Categoria";
import {TipoVideo} from "./TipoVideo";
import { Pais } from "./Pais";
import { Director } from './Director';

export class VideoTeca{

    public VideoTeca: number;
    public Tipo: TipoVideo;
    public Categorias: Categoria[];
    public Nombre: string;
    public Sinopsis: string;
    public Fecha: Date;
    public Director: Director;
    public Produccion: string; 
    public Pais: Pais;
    public Duracion: number;
    public URL: string;

    constructor(){}
}