import { take, put, call, fork } from 'redux-saga/effects'
import api from 'services/api'
import * as actions from './actions'


const url = 'http://127.0.0.1:8000/todos/'

export function* postTodo(text) {
		console.log(text)
    const data = yield call(api.post, url, {done: true, contents: text})
}

export function* watchPostTodoRequest() {
    while (true) {
	const { text } = yield take(actions.POST_TODO_REQUEST)
	yield call(postTodo, text)
    }
}


export default function* () {
    yield fork(watchPostTodoRequest)    
}
