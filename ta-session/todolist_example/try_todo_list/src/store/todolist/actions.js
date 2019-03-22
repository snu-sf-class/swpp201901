let nextTodoId = 0
export const addTodo = (text) => {
    return {
	type: 'ADD_TODO',
	id: nextTodoId++,
	text
    }
}

export const toggleTodo = (id) => {
    return {
	type: 'TOGGLE_TODO',
	id
    }
}

export const POST_TODO_REQUEST = 'POST_TODO_REQUEST'

export const postTodoRequest = (text) => {
    return {
	type: POST_TODO_REQUEST,
	text
    }

}
