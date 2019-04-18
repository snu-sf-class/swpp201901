import React from 'react'
import { storiesOf } from '@kadira/storybook'
import { TodoList } from 'components'

storiesOf('TodoList', module)
  .add('default', () => (
    <TodoList>Hello</TodoList>
  ))
  .add('reverse', () => (
    <TodoList reverse>Hello</TodoList>
  ))
