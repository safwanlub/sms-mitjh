import { useEffect, useState } from "react";
import api from "../../services/api";
import MainLayout from "../../components/layout/MainLayout";
import KpiCards from "../../components/KpiCards";
import AbsensiChart from "../../components/charts/AbsensiChart";
import NilaiChart from "../../components/charts/NilaiChart";
import PelanggaranChart from "../../components/charts/PelanggaranChart";

type KpiData = {
  total_siswa: number;
  total_kelas: number;
  absensi_hari_ini: number;
  pelanggaran: number;
};

export default function KepsekDashboard() {
  // ✅ INI YANG KURANG
  const [kpi, setKpi] = useState<KpiData | null>(null);
  const [chart, setChart] = useState<any[]>([]);
  const [nilaiChart, setNilaiChart] = useState<any[]>([]);
  const [pelanggaranChart, setPelanggaranChart] = useState<any[]>([]);

  useEffect(() => {
    api.get("/dashboard/kepsek/").then((res) => setKpi(res.data));
    api.get("/dashboard/kepsek/absensi-chart/").then((res) => setChart(res.data));
    api.get("/dashboard/kepsek/").then(res => setKpi(res.data));
    api.get("/dashboard/kepsek/nilai-chart/").then((res) => setNilaiChart(res.data));
    api.get("/dashboard/kepsek/pelanggaran-chart/").then((res) => setPelanggaranChart(res.data));
  }, []);

  if (!kpi) return <p>Loading dashboard...</p>;

  return (
    <MainLayout>
      <h1 className="page-title">Dashboard Kepala Sekolah</h1>

      <KpiCards {...kpi} />

      <div className="mt-6 grid grid-cols-1 xl:grid-cols-2 gap-6">
        <div className="card">
          <div className="card-title">Grafik Absensi (7 Hari)</div>
          <AbsensiChart data={chart} />
        </div>

        <div className="card">
          <div className="card-title">Rata-rata Nilai per Kelas</div>
          <NilaiChart data={nilaiChart} />
        </div>

        <div className="card xl:col-span-2">
          <div className="card-title">Pelanggaran Bulanan</div>
          <PelanggaranChart data={pelanggaranChart} />
        </div>
      </div>
    </MainLayout>
  );
}

