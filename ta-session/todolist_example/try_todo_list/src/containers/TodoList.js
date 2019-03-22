import { connect } from 'react-redux'
import { toggleTodo } from '../store/todolist/actions'
import { TodoList } from '../components/molecules/TodoList'

const mapStateToProps = (state) => {
  return {
    todoliststate: state.todolist
  }
}


const mapDispatchToProps = (dispatch) => {
  return {
    onTodoClick: (id) => {
      dispatch(toggleTodo(id))
    }
  }
}

export default connect(mapStateToProps, mapDispatchToProps)(TodoList)
