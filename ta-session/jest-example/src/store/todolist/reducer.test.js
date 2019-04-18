import { initialState } from './selectors'
import { addTodo, toggleTodo } from './actions'
import  todolist_reducer from './reducer'

describe('Add todo', () => {
  it('Add todo change state', () => {
    expect(todolist_reducer(
	[],
	addTodo("eat dinner")
    )).toEqual([{ id:0, text:"eat dinner", completed: false}])
  })
})

describe('toggle todo', () => {
  it('toggle todo change state', () => {
    expect(todolist_reducer(
	[{ id:0, text:"eat dinner", completed: false}],
	toggleTodo(0)
    )).toEqual([{ id:0, text:"eat dinner", completed: true}])
  })
})
