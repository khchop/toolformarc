import { describe, it, expect } from 'vitest'
import { render, screen } from '@testing-library/react'
import LoadingSpinner from './LoadingSpinner'

describe('LoadingSpinner', () => {
  it('renders with correct role', () => {
    render(<LoadingSpinner />)
    const spinner = screen.getByRole('status')
    expect(spinner).toBeDefined()
  })

  it('renders the spinner element', () => {
    render(<LoadingSpinner />)
    const spinner = screen.getByRole('status')
    expect(spinner.innerHTML).toContain('animate-spin')
  })
})
