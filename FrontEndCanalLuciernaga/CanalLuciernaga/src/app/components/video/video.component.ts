import { Component, OnInit } from '@angular/core';
import { VideoTecaService } from '../../core/service.index';
import { VideoTeca } from '../../models/VideoTeca';

@Component({
  selector: 'app-video',
  templateUrl: './video.component.html',
  styleUrls: ['./video.component.css']
})
export class VideoComponent implements OnInit {

  public videoteca: VideoTeca;

  constructor(private _videotecaService: VideoTecaService,
    ) { 

    }

  ngOnInit() {
    this.getVideoTecas();
  }

  getVideoTecas(){
    this._videotecaService.getVideoTecas().subscribe( response => {
      if(response){
        this.videoteca = response;   
        console.log(this.videoteca.categoria)
      }
    });
  }
  
}
