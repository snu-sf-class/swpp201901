import React, { PropTypes } from 'react'
import styled from 'styled-components'
import { font } from 'styled-theme'
import Todo from '../../../components/atoms/Todo'


const Styledul = styled.ul`
  font-family: ${font('primary')};
`

export const TodoList = ({ todoliststate = [], onTodoClick }) => {
    return (
	    <Styledul>
	    {todoliststate.map(todo =>
			       <Todo key={todo.id}
			       {...todo}
			       onClick={() => onTodoClick(todo.id)}
			       />
			      )}
	    </Styledul>
  );
};

TodoList.propTypes = {
    todoliststate: PropTypes.arrayOf(PropTypes.shape({
	id: PropTypes.number,
	completed: PropTypes.bool,
	text: PropTypes.string
    })),
    reverse: PropTypes.bool,
}


