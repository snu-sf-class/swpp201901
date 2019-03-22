import React, { PropTypes } from 'react'
import styled from 'styled-components'
import { font } from 'styled-theme'

const Styledli = styled.li`
  font-family: ${font('primary')};
`

const Todo = ({ onClick, completed, text }) => (
	<Styledli
    onClick={onClick}
    style={{
	textDecoration: completed ? 'line-through' : 'none'
    }}
	>
	{text}
    </Styledli>
)



Todo.propTypes = {
    onClick: PropTypes.func.isRequired,
    completed: PropTypes.bool.isRequired,
    text: PropTypes.string.isRequired,
    reverse: PropTypes.bool
}

export default Todo
