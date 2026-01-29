import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import { RouterProvider } from 'react-router-dom'
import { router } from './routes'
import ErrorBoundary from './components/ErrorBoundary'
import Navigation from './components/Navigation'

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 60 * 1000,
      refetchOnWindowFocus: false,
      retry: 1,
    },
  },
})

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <ErrorBoundary>
        <div className="min-h-screen bg-gray-50">
          <Navigation />
          <main>
            <RouterProvider router={router} />
          </main>
        </div>
      </ErrorBoundary>
    </QueryClientProvider>
  )
}

export default App
