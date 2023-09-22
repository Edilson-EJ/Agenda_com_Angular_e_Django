import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MeuFormularioComponent } from './meu-formulario/meu-formulario.component';
import { EditarAgendamentoComponent } from './editar-agendamento/editar-agendamento.component';

const routes: Routes = [
  {path: 'bancoAgenda',component:MeuFormularioComponent},
  {path: 'editar',component: EditarAgendamentoComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
