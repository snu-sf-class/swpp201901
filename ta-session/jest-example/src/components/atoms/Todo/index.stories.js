import React from 'react'
import { storiesOf } from '@kadira/storybook'
import Todo from '.'

storiesOf('Todo', module)
  .add('default', () => (
    <Todo>Hello</Todo>
  ))
  .add('reverse', () => (
    <Todo reverse>Hello</Todo>
  ))
