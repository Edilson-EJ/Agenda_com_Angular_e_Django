import { Component } from '@angular/core';
import { Item } from '../item.model';

@Component({
  selector: 'app-editar-agendamento',
  templateUrl: './editar-agendamento.component.html',
  styleUrls: ['./editar-agendamento.component.css']
})
export class EditarAgendamentoComponent {

  itens: Item[] = [];
  atualizarItem: Item = new Item ('','','', '', '', '',);



}
