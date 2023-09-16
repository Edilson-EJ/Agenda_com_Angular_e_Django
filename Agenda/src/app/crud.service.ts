
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
    return this.http.get<any[]>(this.APIUrl + '/bancoAgenda/');
  }

  addAgendaBanco(){
    return this.http.post(this.APIUrl + '/bancoAgenda/create/');
  }


  updateAgendaBanco(index: number){
    return this.http.put(this.APIUrl + '/bancoAgenda/update/',index);
  }

  deleteAgendaBanco(index: number){
    return this.http.delete(this.APIUrl + '/bancoAgenda/delete/' + index);
  }

}

//addAgendaBanco(val:any){
  //return this.http.post(this.APIUrl + '/bancoAgenda/create/',val);
//}
