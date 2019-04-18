import { initialState } from './selectors'

const toggleTodo = (todo, action) => {
  if (todo.id != action.id) {
    return todo
  }
  return {
    ...todo,
    completed: !todo.completed
  }
}

const todolist_reducer = (state=initialState, action) => {
  switch (action.type) {
    case 'ADD_TODO':
      return [
        ...state,
	{
	  id: action.id,
	  text: action.text,
	  completed: false
	}
      ]
    case 'TOGGLE_TODO':
      return state.map(t => toggleTodo(t, action))
    default:
      return state
  }
}

export default todolist_reducer
