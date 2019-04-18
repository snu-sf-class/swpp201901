import React from 'react'
import { storiesOf } from '@kadira/storybook'
import Button from '.'

storiesOf('Button', module)
  .add('default', () => (
    <Button>Hello</Button>
  ))
  .add('reverse', () => (
    <Button reverse>Hello</Button>
  ))
