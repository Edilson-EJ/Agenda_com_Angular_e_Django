import { Component } from '@angular/core';
import { Item } from './../item.model';

import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})

@Component({
  selector: 'app-meu-formulario',
  templateUrl: './meu-formulario.component.html',
  styleUrls: ['./meu-formulario.component.css']
})
export class MeuFormularioComponent {

    private baseURL = '127.0.0.1:8000/bancoAgenda/'

    constructor(private http: HttpClient){}

    itens: Item[] = [];
    novoItem: Item = new Item ('','', '', '', '');

    ListarAgendamento(){
      return this.http.get(this.baseURL)
    }

    criarAgendamento(Item: any) {
      return this.http.post(this.baseURL + 'create/', Item);
    }

    atualizarAgendamento(index: number, Item: any) {
      return this.http.put(this.baseURL + `update/${index}/`,Item);
    }

    excluirAgendamento(index: number) {
      return this.http.delete(this.baseURL + `delete/${index}/`);
    }

    //pega as informações digitadas pelo usuario salba no array
    //



}
