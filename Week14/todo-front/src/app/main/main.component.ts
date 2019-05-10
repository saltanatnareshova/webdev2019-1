import { Component, OnInit } from '@angular/core';
import { ProviderService } from '../shared/services/provider.service';
import { ITaskList, ITask } from '../shared/models/models';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.scss']
})
export class MainComponent implements OnInit {

  public headTasks = 'Tasks';
  public currentTaskList = -1;

  public taskLists: ITaskList[] = [];
  public tasks: ITask[] = [];

  public taskListName: any = '';
  public taskName: any = '';

  public isLogged = false;

  public login: any = '';
  public password: any = '';

  constructor(private provider: ProviderService) { }

  ngOnInit() {
    const token = localStorage.getItem('token');
    if (token) {
      this.isLogged = true;
    }
    if (this.isLogged) {
      this.getTaskLists();
    }
  }

  getTaskLists() {
    this.provider.getTaskLists().then(res => {
      this.taskLists = res;
    });
  }

  getTasks(taskList: ITaskList) {
    this.provider.getTasks(taskList).then(res => {
      this.tasks = res;
      this.headTasks = taskList.name;
      this.currentTaskList = taskList.id;
    });
  }

  createTaskList() {
    if (this.taskListName !== '') {
      this.provider.createTaskList(this.taskListName).then(res => {
        this.taskListName = '';
        this.taskLists.push(res);
      });
    }
  }

  editTaskList(list: ITaskList) {
    this.provider.updateTaskList(list).then(res => {
      this.currentTaskList = -1;
    });
  }

  deleteTaskList(list: ITaskList) {
    this.provider.deleteTaskList(list.id).then(res => {
      this.provider.getTaskLists().then(r => {
        this.taskLists = r;
      });
      this.currentTaskList = -1;
    });
  }

  createTask() {
    if (this.currentTaskList !== -1 && this.taskName !== '') {
      this.provider.createTask(this.currentTaskList, this.taskName).then(res => {
        this.taskName = '';
        this.tasks.push(res);
      });
    }
  }

  auth() {
    if (this.login !== '' && this.password !== '') {
      this.provider.auth(this.login, this.password).then(res => {
        localStorage.setItem('token', res.token);
        this.isLogged = true;
        this.getTaskLists();
      });
    }
  }

  logout() {
    this.provider.logout().then(res => {
      this.isLogged = false;
      localStorage.clear();
    });
  }
}
