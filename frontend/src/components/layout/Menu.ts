export type MenuItem = {
  label: string;
  path: string;
};

export const MENU_BY_ROLE: Record<string, MenuItem[]> = {
  kepsek: [
    { label: "Dashboard", path: "/kepsek" },
    { label: "Akademik", path: "/akademik" },
    { label: "Kesiswaan", path: "/kesiswaan" },
  ],
  guru: [
    { label: "Dashboard", path: "/guru" },
    { label: "Nilai", path: "/guru/nilai" },
    { label: "Absensi", path: "/guru/absensi" },
  ],
  tu: [
    { label: "Data Siswa", path: "/tu/siswa" },
    { label: "Kelas", path: "/tu/kelas" },
  ],
  bendahara: [
    { label: "Keuangan", path: "/bendahara/keuangan" },
  ],
  SUPERADMIN: [
    { label: "Dashboard", path: "/admin" },
  ],
};
