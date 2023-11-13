import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';


import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { RodapeComponent } from './rodape/rodape.component';

import { FormsModule, } from '@angular/forms';
import { MeuFormularioComponent } from './meu-formulario/meu-formulario.component';
import { HttpClientModule } from '@angular/common/http';

import { CrudService } from './crud.service';
import { EditarAgendamentoComponent } from './editar-agendamento/editar-agendamento.component';
import { LoginComponent } from './login/login.component';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    RodapeComponent,
    MeuFormularioComponent,
    EditarAgendamentoComponent,
    LoginComponent,

  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,

  ],
  providers: [CrudService],
  bootstrap: [AppComponent]
})
export class AppModule { }
