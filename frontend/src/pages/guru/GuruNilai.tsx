import { useEffect, useState } from 'react'
import api from '../../services/api'
import MainLayout from '../../components/layout/MainLayout'
import NilaiForm from './components/NilaiForm'

export default function GuruNilai() {
  const [data, setData] = useState<any[]>([])
  const [editing, setEditing] = useState<any | null>(null)
  const [showForm, setShowForm] = useState(false)

  const load = () => {
    api.get('/nilai/').then((res) => setData(res.data.results))
  }

  useEffect(load, [])

  const save = async (payload: any) => {
    if (editing) {
      await api.put(`/nilai/${editing.id}/`, payload)
    } else {
      await api.post('/nilai/', payload)
    }
    setEditing(null)
    setShowForm(false)
    load()
  }

  const remove = async (id: number) => {
    if (confirm('Hapus nilai ini?')) {
      await api.delete(`/nilai/${id}/`)
      load()
    }
  }

  return (
    <MainLayout>
      <h1 className="page-title">Nilai Siswa</h1>

      {!showForm && (
        <button className="btn-primary mb-4" onClick={() => setShowForm(true)}>
          + Tambah Nilai
        </button>
      )}

      {showForm && (
        <NilaiForm
          initial={editing}
          onSubmit={save}
          onCancel={() => {
            setEditing(null)
            setShowForm(false)
          }}
        />
      )}

      <div className="card overflow-x-auto mt-4">
        <table className="w-full text-sm">
          <thead>
            <tr>
              <th>Siswa</th>
              <th>Kelas</th>
              <th>Mapel</th>
              <th>Nilai</th>
              <th>Aksi</th>
            </tr>
          </thead>
          <tbody>
            {data.map((n) => (
              <tr key={n.id}>
                <td>{n.siswa_nama}</td>
                <td>{n.kelas_nama}</td>
                <td>{n.mapel_nama}</td>
                <td>{n.nilai_sumatif}</td>
                <td className="space-x-2">
                  <button
                    className="btn-secondary"
                    onClick={() => {
                      setEditing(n)
                      setShowForm(true)
                    }}
                  >
                    Edit
                  </button>
                  <button className="btn-danger" onClick={() => remove(n.id)}>
                    Hapus
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </MainLayout>
  )
}
