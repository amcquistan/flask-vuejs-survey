// utils/index.js

import Vue from 'vue'

export const EventBus = new Vue()

export function isValidJwt (jwt) {
  if (!jwt || jwt.split('.').length < 3) {
    return false
  }
  const data = JSON.parse(atob(jwt.split('.')[1]))
  const exp = new Date(data.exp * 1000)
  const now = new Date()
  return now < exp
}
