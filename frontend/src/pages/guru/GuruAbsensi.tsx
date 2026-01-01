import { useEffect, useState } from 'react'
import api from '../../services/api'
import MainLayout from '../../components/layout/MainLayout'
import AbsensiForm from './components/AbsensiForm'

export default function GuruAbsensi() {
  const [siswa, setSiswa] = useState<any[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    api
      .get('/siswa/')
      .then((res) => setSiswa(res.data.results))
      .finally(() => setLoading(false))
  }, [])

  const submitAbsensi = async (data: any[]) => {
    for (const item of data) {
      await api.post('/absensi/', item)
    }
    alert('Absensi berhasil disimpan')
  }

  if (loading) return <p>Loading...</p>

  return (
    <MainLayout>
      <h1 className="page-title">Absensi Hari Ini</h1>

      <AbsensiForm siswa={siswa} onSubmit={submitAbsensi} />
    </MainLayout>
  )
}
