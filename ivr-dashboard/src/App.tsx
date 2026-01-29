import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import { createBrowserRouter, RouterProvider, Outlet } from 'react-router-dom'
import { lazy, Suspense } from 'react'
import ErrorBoundary from './components/ErrorBoundary'
import LoadingSpinner from './components/LoadingSpinner'
import Navigation from './components/Navigation'

const Dashboard = lazy(() => import('./pages/Dashboard'))
const Logs = lazy(() => import('./pages/Logs'))
const Settings = lazy(() => import('./pages/Settings'))
const Dialers = lazy(() => import('./pages/Dialers'))

function Layout() {
  return (
    <div className="min-h-screen bg-gray-50">
      <Navigation />
      <main>
        <Suspense fallback={<LoadingSpinner />}>
          <Outlet />
        </Suspense>
      </main>
    </div>
  )
}

const router = createBrowserRouter([
  {
    path: '/',
    element: <Layout />,
    children: [
      {
        path: '/',
        element: <Dashboard />,
      },
      {
        path: '/logs',
        element: <Logs />,
      },
      {
        path: '/settings',
        element: <Settings />,
      },
      {
        path: '/dialers',
        element: <Dialers />,
      },
    ],
  },
])

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
        <RouterProvider router={router} />
      </ErrorBoundary>
    </QueryClientProvider>
  )
}

export default App
