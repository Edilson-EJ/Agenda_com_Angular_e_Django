import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MeuFormularioComponent } from './meu-formulario/meu-formulario.component';

const routes: Routes = [
  {path: 'bancoAgenda',component:MeuFormularioComponent},

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
