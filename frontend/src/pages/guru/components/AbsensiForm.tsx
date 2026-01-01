import { useState } from 'react'

type Props = {
  siswa: any[]
  onSubmit: (data: any[]) => void
}

export default function AbsensiForm({ siswa, onSubmit }: Props) {
  const [status, setStatus] = useState<{ [key: number]: string }>({})

  const submit = () => {
    const today = new Date().toISOString().slice(0, 10)

    const payload = siswa.map((s) => ({
      siswa: s.id,
      tanggal: today,
      status: status[s.id] || 'H',
    }))

    onSubmit(payload)
  }

  return (
    <div className="card space-y-3">
      {siswa.map((s) => (
        <div key={s.id} className="flex justify-between items-center">
          <span>{s.nama}</span>

          <select
            className="input w-32"
            value={status[s.id] || 'H'}
            onChange={(e) => setStatus({ ...status, [s.id]: e.target.value })}
          >
            <option value="H">Hadir</option>
            <option value="I">Izin</option>
            <option value="S">Sakit</option>
            <option value="A">Alpha</option>
          </select>
        </div>
      ))}

      <button className="btn-primary mt-4" onClick={submit}>
        Simpan Absensi
      </button>
    </div>
  )
}
