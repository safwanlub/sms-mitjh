import { Routes, Route, Navigate } from 'react-router-dom'
import Login from './pages/Login'
import KepsekDashboard from './pages/dashboard/KepsekDashboard'
import GuruDashboard from './pages/dashboard/GuruDashboard'
import GuruNilai from './pages/guru/GuruNilai'
import GuruAbsensi from './pages/guru/GuruAbsensi'
import RoleRoute from './routes/RoleRoute'
import { useAuth } from './auth/AuthContext'

function RoleRedirect() {
  const { user } = useAuth()

  if (!user) return <Navigate to="/login" replace />

  switch (user.role) {
    case 'kepsek':
      return <Navigate to="/kepsek" replace />
    case 'guru':
      return <Navigate to="/guru" replace />
    case 'tu':
      return <Navigate to="/tu/siswa" replace />
    case 'bendahara':
      return <Navigate to="/bendahara/keuangan" replace />
    default:
      return <Navigate to="/login" replace />
  }
}

export default function App() {
  return (
    <Routes>
      {/* ROOT LANDING */}
      <Route path="/" element={<RoleRedirect />} />

      {/* LOGIN */}
      <Route path="/login" element={<Login />} />

      {/* DASHBOARDS */}
      <Route
        path="/kepsek"
        element={
          <RoleRoute allow={['kepsek']}>
            <KepsekDashboard />
          </RoleRoute>
        }
      />

      <Route
        path="/guru"
        element={
          <RoleRoute allow={['guru']}>
            <GuruDashboard />
          </RoleRoute>
        }
      />

      <Route
        path="/guru/nilai"
        element={
          <RoleRoute allow={['guru']}>
            <GuruNilai />
          </RoleRoute>
        }
      />

      <Route
        path="/guru/absensi"
        element={
          <RoleRoute allow={['guru']}>
            <GuruAbsensi />
          </RoleRoute>
        }
      />
    </Routes>
  )
}
