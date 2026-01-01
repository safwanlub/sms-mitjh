import { ReactNode } from 'react'
import { NavLink, useNavigate } from 'react-router-dom'
import { useAuth } from '../../auth/AuthContext'
import { MENU_BY_ROLE } from './menu'

export default function MainLayout({ children }: { children: ReactNode }) {
  const { user, logout } = useAuth()
  const navigate = useNavigate()

  const menus = MENU_BY_ROLE[user?.role || ''] || []

  const handleLogout = () => {
    logout()
    navigate('/login', { replace: true })
  }

  return (
    <div className="flex min-h-screen w-full">
      {/* Sidebar */}
      <aside className="w-64 bg-slate-900 text-white p-6 flex flex-col">
        <div>
          <div className="text-xl font-bold mb-8">SMS-MITJH</div>

          <nav className="space-y-2">
            {menus.map((m) => (
              <NavLink
                key={m.path}
                to={m.path}
                className={({ isActive }) =>
                  `block px-4 py-2 rounded-lg transition ${
                    isActive ? 'bg-slate-800' : 'hover:bg-slate-800'
                  }`
                }
              >
                {m.label}
              </NavLink>
            ))}
          </nav>
        </div>

        <button
          onClick={handleLogout}
          className="mt-auto bg-red-600 hover:bg-red-700 text-white px-4 py-2 rounded-lg transition"
        >
          Keluar
        </button>
      </aside>

      {/* CONTENT */}
      <main className="flex-1 w-full p-6">
        {/* 🔹 HEADER USER INFO */}
        <div className="flex justify-between items-center mb-6">
          <div>
            <h2 className="text-lg font-semibold">
              Selamat datang, {user?.guru?.nama_lengkap ?? user?.username}
            </h2>
            <p className="text-sm text-slate-500 capitalize">
              Role: {user?.role}
            </p>
          </div>
        </div>
        {children}
      </main>
    </div>
  )
}
