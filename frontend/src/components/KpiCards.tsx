type Props = {
  total_siswa: number;
  total_kelas: number;
  absensi_hari_ini: number;
  pelanggaran: number;
};

export default function KpiCards({
  total_siswa,
  total_kelas,
  absensi_hari_ini,
  pelanggaran,
}: Props) {
  const items = [
    { label: "Total Siswa", value: total_siswa },
    { label: "Total Kelas", value: total_kelas },
    { label: "Absen Hari Ini", value: absensi_hari_ini },
    { label: "Pelanggaran", value: pelanggaran },
  ];

  return (
    <div style={{ display: "grid", gridTemplateColumns: "repeat(4, 1fr)", gap: 16 }}>
      {items.map((it) => (
        <div
          key={it.label}
          style={{
            padding: 16,
            borderRadius: 12,
            background: "#ffffff",
            boxShadow: "0 4px 12px rgba(0,0,0,.08)",
          }}
        >
          <div style={{ fontSize: 14, color: "#666" }}>{it.label}</div>
          <div style={{ fontSize: 28, fontWeight: 700 }}>{it.value}</div>
        </div>
      ))}
    </div>
  );
}
