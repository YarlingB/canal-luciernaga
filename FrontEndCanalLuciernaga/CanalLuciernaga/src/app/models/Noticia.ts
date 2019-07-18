import { Categoria } from './Categoria';
import { Clasificacion } from './Clasificacion'
import { TipoNoticia } from './TipoNoticia'
import { Pais } from './Pais'

export class Noticia{

    public IdNoticia: number;
    public Tipo: TipoNoticia;
    public UltimoMomento: boolean;
    public Titulo: string; 
    public Clasificacion: Clasificacion;
    public Categoria: Categoria;
    public Autor: string;
    public Fecha: Date;
    public Foto: string;
    public Descripcion: string;
    public Pais: Pais
    public Fuente: string;
    public Tags: string;

    constructor(){}
}