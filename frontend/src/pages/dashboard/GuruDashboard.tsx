import { useEffect, useState } from "react";
import api from "../../services/api";
import MainLayout from "../../components/layout/MainLayout";
import NilaiChart from "../../components/charts/NilaiChart";

type Ringkasan = {
  total_kelas: number;
  total_mapel: number;
  total_siswa: number;
};

export default function GuruDashboard() {
  const [ringkasan, setRingkasan] = useState<Ringkasan | null>(null);
  const [chart, setChart] = useState<any[]>([]);

  useEffect(() => {
    api.get("/dashboard/guru/").then(res => setRingkasan(res.data));
    api.get("/dashboard/guru/nilai-chart/").then(res => setChart(res.data));
  }, []);

  if (!ringkasan) return <p>Loading...</p>;

  return (
    <MainLayout>
      <h1 className="page-title">Dashboard Guru</h1>

      {/* KPI */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div className="card">
          <div className="card-title">Kelas Diajar</div>
          <div className="text-3xl font-bold">{ringkasan.total_kelas}</div>
        </div>
        <div className="card">
          <div className="card-title">Mapel</div>
          <div className="text-3xl font-bold">{ringkasan.total_mapel}</div>
        </div>
        <div className="card">
          <div className="card-title">Siswa</div>
          <div className="text-3xl font-bold">{ringkasan.total_siswa}</div>
        </div>
      </div>

      {/* Grafik */}
      <div className="mt-6 card">
        <div className="card-title">Rata-rata Nilai per Kelas</div>
        <NilaiChart data={chart} />
      </div>
    </MainLayout>
  );
}
