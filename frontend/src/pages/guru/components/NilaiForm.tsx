import { useState } from 'react'

export default function NilaiForm({
  initial,
  onSubmit,
  onCancel,
}: {
  initial?: any
  onSubmit: (payload: any) => void
  onCancel: () => void
}) {
  const [form, setForm] = useState(
    initial || {
      siswa: '',
      kelas: '',
      mapel: '',
      nilai_sumatif: '',
      semester: 'Ganjil',
    }
  )

  return (
    <div className="card space-y-3">
      <div className="grid grid-cols-1 md:grid-cols-4 gap-3">
        <input
          className="input"
          placeholder="Siswa ID"
          value={form.siswa}
          onChange={(e) => setForm({ ...form, siswa: e.target.value })}
        />
        <input
          className="input"
          placeholder="Kelas ID"
          value={form.kelas}
          onChange={(e) => setForm({ ...form, kelas: e.target.value })}
        />
        <input
          className="input"
          placeholder="Mapel ID"
          value={form.mapel}
          onChange={(e) => setForm({ ...form, mapel: e.target.value })}
        />
        <input
          className="input"
          placeholder="Nilai"
          value={form.nilai_sumatif}
          onChange={(e) => setForm({ ...form, nilai_sumatif: e.target.value })}
        />
      </div>

      <div className="flex gap-2">
        <button className="btn-primary" onClick={() => onSubmit(form)}>
          Simpan
        </button>
        <button className="btn-secondary" onClick={onCancel}>
          Batal
        </button>
      </div>
    </div>
  )
}
