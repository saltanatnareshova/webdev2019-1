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
  public showTasks = false;

  constructor(private provider: ProviderService) { }

  ngOnInit() {
    this.provider.getTaskLists().then(res => {
      this.taskLists = res;
    });
  }

  getTasks(taskList: ITaskList) {
    this.provider.getTasks(taskList).then(res => {
      this.tasks = res;
      this.showTasks = true;
    });
  }
}
