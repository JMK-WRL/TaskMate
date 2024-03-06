// src/router/index.js

import { createRouter, createWebHistory } from 'vue-router'
import TaskCreationView from '../views/TaskCreationView.vue'
import TaskListView from '../views/TaskListView.vue'

const routes = [
  {
    path: '/',
    redirect: '/tasks'
  },
  {
    path: '/tasks',
    name: 'TaskList',
    component: TaskListView
  },
  {
    path: '/tasks/create',
    name: 'TaskCreation',
    component: TaskCreationView
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
