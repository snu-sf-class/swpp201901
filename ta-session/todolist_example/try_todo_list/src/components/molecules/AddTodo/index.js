import React, { PropTypes } from 'react'
import styled from 'styled-components'
import { font, palette } from 'styled-theme'
import Button from '../../../components/atoms/Button'

const Wrapper = styled.div`
font-family: ${font('primary')};
color: ${palette('grayscale', 0)};
`

export const AddTodo = ({ statefunction, onAddTodo, onPostTodo }) => {
    let input;
    console.log(onAddTodo);
    console.log('asdf')
    const onSubmit = () => {
	console.log('outer scope of if');
	if (input != undefined) {
	    console.log('inner scope of if');
	    onAddTodo(input.value);
	    input.value = '';
	}
    };

    const onPost = () => {
	if (input != undefined) {
	    onPostTodo(input.value);	
	    input.value = '';
	}
    };

    return (  
	    <div>
   	    <input ref={node => {input = node;}} />
  	    <Button type="submit" onClick={onSubmit}>ADD Todo</Button>
	    <Button type="submit" onClick={onPost}>POST Todo</Button>
	    </div>
    ); 
};

AddTodo.propTypes = {
    reverse: PropTypes.bool,
    children: PropTypes.node,
}

/*export default AddTodo*/
