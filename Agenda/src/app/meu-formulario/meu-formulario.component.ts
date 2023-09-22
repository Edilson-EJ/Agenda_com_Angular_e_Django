import { AfterViewInit, Component } from '@angular/core';
import { Item } from './../item.model';
import { CrudService } from '../crud.service';

import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs'


@Injectable({
  providedIn: 'root'
})

@Component({
  selector: 'app-meu-formulario',
  templateUrl: './meu-formulario.component.html',
  styleUrls: ['./meu-formulario.component.css']
})
export class MeuFormularioComponent{

    constructor(private crud:CrudService,private http:HttpClient){
      this.listarAgendamento();

    }

    ngOnInit(): void{
      this.listarAgendamento();

    }

    itens: Item[] = [];
    novoItem: Item = new Item ('','','', '', '', '',);




    listarAgendamento = () => {

      this.crud.getAgendaBanco().subscribe(
        data =>{
          this.itens =data;
          console.log(data)

        }
      )

    }

    createAgendamento = () => {
      window.location.reload()
      this.crud.addAgendaBanco(this.novoItem).subscribe(
        data => {
          data = this.novoItem

        }
      )

    }

    editarAgendamento = (index: number) =>{

      let id = this.itens[index].id

      console.log("update: " + id)

      this.crud.updateAgendaBanco(id).subscribe(
        data =>{

        }
      )
    }

    deleteAgendamento(index: any){

      console.log("inde e: " + index)

      let id = this.itens[index].id

      console.log("id e: " + id)
      window.location.reload()
      this.crud.deleteAgendaBanco(id).subscribe(
        data =>{

        }
      )
    }



}
