import { Component, OnInit } from '@angular/core';
import { ProviderService } from '../shared/services/provider.service';
import { ITaskList, ITask } from '../shared/models/models';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.scss']
})
export class MainComponent implements OnInit {

  public taskLists: ITaskList[] = [];
  public tasks: ITask[] = [];

  public name: any = '';

  constructor(private provider: ProviderService) { }

  ngOnInit() {
    this.provider.getTaskLists().then(res => {
      this.taskLists = res;
    });
  }

  getTasks(taskList: ITaskList) {
    this.provider.getTasks(taskList).then(res => {
      this.tasks = res;
    });
  }

  createTaskList() {
    if (this.name !== '') {
      this.provider.createTaskList(this.name).then(res => {
        this.name = '';
        this.taskLists.push(res);
      });
    }
  }

  editTaskList(list: ITaskList) {
    this.provider.updateTaskList(list).then(res => {

    });
  }

  deleteTaskList(list: ITaskList) {
    this.provider.deleteTaskList(list.id).then(res => {
      this.provider.getTaskLists().then(r => {
        this.taskLists = r;
      });
    });
  }
}
