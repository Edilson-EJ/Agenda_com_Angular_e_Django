import { Component } from '@angular/core';
import { Item } from './../item.model';

@Component({
  selector: 'app-meu-formulario',
  templateUrl: './meu-formulario.component.html',
  styleUrls: ['./meu-formulario.component.css']
})
export class MeuFormularioComponent {
    itens: Item[] = [];
    novoItem: Item = new Item ('','', '', '', '');
  
    adicionarItem(): void {
      this.itens.push(this.novoItem);
      this.novoItem = new Item('', '', '', '', ''); // Limpa o novoItem
    }
  
    excluirItem(index: number): void {
      this.itens.splice(index, 1);
  }

  concluirTarefa(){
    const element = document.querySelector('li')
    element?.classList.add("riscaTarefa")    
  }
}