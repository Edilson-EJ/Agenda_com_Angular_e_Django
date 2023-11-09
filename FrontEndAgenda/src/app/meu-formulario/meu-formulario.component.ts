import { Component } from '@angular/core';
import { Item } from './../item.model';
import { CrudService } from '../crud.service';

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
export class MeuFormularioComponent{

    constructor(private crud:CrudService,private http:HttpClient){
      this.listarAgendamento();

    }

    ngOnInit(): void{
      this.listarAgendamento();

    }

    itens: Item[] = [];
    novoItem: Item = new Item ('','','', '', '', '',);

    itensAtualizar: Item[] = [];
    atualizarItem: Item = new Item ('','','', '', '', '',);

    atualizarAgendamento: boolean = false

    idAgendamento: string = ''

    onAtualizarAgendamento(index: number){

      this.atualizarAgendamento = !this.atualizarAgendamento

      let id = this.itens[index].id

      this.idAgendamento = id

      console.log("item a atualizar: " + this.idAgendamento)

    }

    ofAtualizarAgendamento(){
      this.atualizarAgendamento = false
      let id = this.idAgendamento
      this.editarAgendamento(id)
    }


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

    editarAgendamento = (index: any) =>{
      console.log("update: " + index)

      this.crud.updateAgendaBanco(index,this.atualizarItem).subscribe(
        data =>{

          data = this.atualizarItem
        }
      )
    }

    deleteAgendamento(index: any){
      console.log("inde e: " + index)
      let id = this.itens[index].id
      console.log("id e: " + id)
      this.crud.deleteAgendaBanco(id).subscribe(
        data =>{

        }
      )
      window.location.reload()
    }



}
