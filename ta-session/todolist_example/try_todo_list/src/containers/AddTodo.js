import { connect } from 'react-redux'
import { AddTodo } from '../components/molecules/AddTodo'
import { addTodo, postTodoRequest } from '../store/todolist/actions'

const mapStateToProps = (state) => { 
    return {
	statefunction : state
    }
}

const mapDispatchToProps = (dispatch) => {
    return {
	onAddTodo: (text) => {
	    dispatch(addTodo(text))
	},
	onPostTodo: (text) => {
	    dispatch(postTodoRequest(text))	
	}
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(AddTodo)





