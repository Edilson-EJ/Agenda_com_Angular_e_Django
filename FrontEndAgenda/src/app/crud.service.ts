
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CrudService {

  readonly APIUrl = "http://127.0.0.1:8000"

  constructor(private http:HttpClient) { }

  getAgendaBanco():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl + '/agendamento/');
  }

  addAgendaBanco(data: any){
    return this.http.post(this.APIUrl + '/agendamento/create/', data);
  }


  updateAgendaBanco(index: any, dados: any){
    return this.http.put(this.APIUrl + '/agendamento/update/' + index,dados);
  }

  deleteAgendaBanco(index: any){
    return this.http.delete(this.APIUrl + '/agendamento/delete/'+ index);
  }

}

//addAgendaBanco(val:any){
  //return this.http.post(this.APIUrl + '/bancoAgenda/create/',val);
//}
