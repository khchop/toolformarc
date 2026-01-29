import { NavLink } from 'react-router-dom'

export default function Navigation() {
  const navItems = [
    { path: '/', label: 'Dashboard' },
    { path: '/logs', label: 'Logs' },
    { path: '/dialers', label: 'Dialers' },
    { path: '/settings', label: 'Settings' },
  ]

  return (
    <nav className="bg-white shadow-sm border-b border-gray-200">
      <div className="px-6 py-4">
        <div className="flex items-center justify-between">
          <h1 className="text-xl font-bold text-gray-900">IVR Dashboard</h1>
          <div className="flex space-x-6">
            {navItems.map((item) => (
              <NavLink
                key={item.path}
                to={item.path}
                className={({ isActive }) =>
                  `text-sm font-medium transition-colors ${
                    isActive
                      ? 'text-blue-600 border-b-2 border-blue-600'
                      : 'text-gray-600 hover:text-gray-900'
                  }`
                }
              >
                {item.label}
              </NavLink>
            ))}
          </div>
        </div>
      </div>
    </nav>
  )
}
