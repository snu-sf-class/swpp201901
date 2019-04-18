import React from 'react'
import AddTodo from '../../../containers/AddTodo'
import TodoList from '../../../containers/TodoList'
import { PageTemplate } from 'components'

const HomePage = () => {
  return (
  	  <div>
			<AddTodo/>
			<TodoList/>
	  </div>
  )
}

export default HomePage
