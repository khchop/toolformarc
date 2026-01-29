import { createBrowserRouter } from 'react-router-dom';
import { lazy, Suspense } from 'react';
import LoadingSpinner from '../components/LoadingSpinner';

const Dashboard = lazy(() => import('../pages/Dashboard'));
const Logs = lazy(() => import('../pages/Logs'));
const Settings = lazy(() => import('../pages/Settings'));
const Dialers = lazy(() => import('../pages/Dialers'));

export const router = createBrowserRouter([
  {
    path: '/',
    element: (
      <Suspense fallback={<LoadingSpinner />}>
        <Dashboard />
      </Suspense>
    ),
  },
  {
    path: '/logs',
    element: (
      <Suspense fallback={<LoadingSpinner />}>
        <Logs />
      </Suspense>
    ),
  },
  {
    path: '/settings',
    element: (
      <Suspense fallback={<LoadingSpinner />}>
        <Settings />
      </Suspense>
    ),
  },
  {
    path: '/dialers',
    element: (
      <Suspense fallback={<LoadingSpinner />}>
        <Dialers />
      </Suspense>
    ),
  },
]);
