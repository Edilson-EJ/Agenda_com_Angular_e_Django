import { Component } from '@angular/core';
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
export class MeuFormularioComponent {

    constructor(private crud:CrudService,private http:HttpClient){
      this.ListarAgendamento();

    }

    itens: Item[] = [];
    novoItem: Item = new Item ('','','', '', '', '',);

    ListarAgendamento = () => {

      this.crud.getAgendaBanco().subscribe(
        data =>{
          this.itens =data;
          console.log(data)

        }
      )

    }

    CreateAgendamento = () => {
      this.crud.addAgendaBanco().subscribe(
        data => {
          data = this.itens

        }
      )

    }

    EditarAgendamento = (index: number) =>{
      this.crud.updateAgendaBanco(index).subscribe(
        data =>{

        }
      )
    }

    DeleteAgendamento(index: number){
      console.log(index)
      this.crud.deleteAgendaBanco(index).subscribe(
        data =>{
          data = this.itens[index]
          console.log(index)
          //location.reload();
        }
      )
    }


}
