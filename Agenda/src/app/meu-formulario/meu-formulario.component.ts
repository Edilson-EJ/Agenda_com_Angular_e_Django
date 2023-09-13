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

    constructor(private crud:CrudService){
      this.ListarAgendamento();

    }

    itens: Item[] = [];
    novoItem: Item = new Item ('','', '', '', '');

    ListarAgendamento = () => {
      this.crud.getAgendaBanco().subscribe(
        data =>{
          this.itens =data;
        }
      )
    }

    CreateAgendamento = () => {
      this.crud.addAgendaBanco(1).subscribe(
        data =>{

        }
      )
    }



}
